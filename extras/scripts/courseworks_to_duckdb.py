"""
Pull students and grades from all the courses you teach in CourseWorks (Canvas) into DuckDB, for querying across courses and semesters.

To avoid storing private student information, the data is only kept temporarily: the script loads it into a database in a private temporary directory, opens the DuckDB CLI on it, and deletes it when you exit.

See usage in meta/instructor_guide.md.
"""

import asyncio
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import duckdb
import httpx
import pandas as pd
from dotenv import load_dotenv

BASE_URL = "https://courseworks2.columbia.edu/api/v1"
TEACHING_ROLES = {"teacher", "ta"}
# number of concurrent API requests, to stay well within Canvas' rate limit
MAX_CONNECTIONS = 10

load_dotenv()


def client() -> httpx.AsyncClient:
    return httpx.AsyncClient(
        headers={"Authorization": f"Bearer {os.environ['COURSEWORKS_TOKEN']}"},
        limits=httpx.Limits(max_connections=MAX_CONNECTIONS),
        # requests wait for a free connection as long as needed
        timeout=httpx.Timeout(30, pool=None),
    )


async def get_all(
    client: httpx.AsyncClient, path: str, params: dict | None = None
) -> list[dict]:
    """Fetch every page of a Canvas list endpoint."""

    url = f"{BASE_URL}{path}"
    params = {"per_page": 100, **(params or {})}
    results = []
    while url:
        response = await client.get(url, params=params)
        response.raise_for_status()
        results.extend(response.json())
        # the next URL already includes the query parameters
        url = response.links.get("next", {}).get("url")
        params = None
    return results


def pick(records: list[dict], cols: list[str], **extra) -> pd.DataFrame:
    return pd.DataFrame(
        [{**{c: r.get(c) for c in cols}, **extra} for r in records],
        columns=[*cols, *extra],
    )


async def get_courses(client: httpx.AsyncClient) -> pd.DataFrame:
    courses = await get_all(
        client,
        "/courses",
        {
            "state[]": ["available", "completed", "unpublished"],
            "include[]": ["term", "total_students"],
        },
    )
    teaching = [
        c
        for c in courses
        if any(e["type"] in TEACHING_ROLES for e in c.get("enrollments", []))
    ]
    df = pick(
        teaching,
        [
            "id",
            "name",
            "course_code",
            "sis_course_id",
            "workflow_state",
            "start_at",
            "end_at",
            "total_students",
        ],
    )
    df["term"] = [c.get("term", {}).get("name") for c in teaching]
    df["term_start_at"] = [c.get("term", {}).get("start_at") for c in teaching]
    return df


async def get_course_data(
    client: httpx.AsyncClient, course_id: int
) -> dict[str, pd.DataFrame]:
    sections, enrollments, groups, assignments = await asyncio.gather(
        get_all(client, f"/courses/{course_id}/sections"),
        get_all(
            client,
            f"/courses/{course_id}/enrollments",
            {
                "type[]": ["StudentEnrollment"],
                "state[]": ["active", "invited", "inactive", "completed"],
            },
        ),
        get_all(client, f"/courses/{course_id}/assignment_groups"),
        get_all(client, f"/courses/{course_id}/assignments"),
    )

    enrollments_df = pick(
        enrollments,
        [
            "id",
            "user_id",
            "course_section_id",
            "enrollment_state",
            "created_at",
            "last_activity_at",
            "total_activity_time",
        ],
        course_id=course_id,
    )
    grade_cols = [
        "current_score",
        "current_grade",
        "final_score",
        "final_grade",
        "unposted_current_score",
        "unposted_final_score",
    ]
    for col in grade_cols:
        enrollments_df[col] = [e.get("grades", {}).get(col) for e in enrollments]

    return {
        "sections": pick(
            sections, ["id", "name", "sis_section_id"], course_id=course_id
        ),
        "students": pick(
            [e["user"] for e in enrollments],
            ["id", "name", "sortable_name", "sis_user_id", "login_id"],
        ),
        "enrollments": enrollments_df,
        "assignment_groups": pick(
            groups, ["id", "name", "position", "group_weight"], course_id=course_id
        ),
        "assignments": pick(
            assignments,
            [
                "id",
                "assignment_group_id",
                "name",
                "position",
                "points_possible",
                "grading_type",
                "due_at",
                "published",
                "omit_from_final_grade",
            ],
            course_id=course_id,
        ),
    }


async def get_submissions(
    client: httpx.AsyncClient, course_id: int, assignment_id: int
) -> pd.DataFrame:
    # fetched per assignment rather than per course so that they can be done in parallel
    submissions = await get_all(
        client, f"/courses/{course_id}/assignments/{assignment_id}/submissions"
    )
    return pick(
        submissions,
        [
            "id",
            "assignment_id",
            "user_id",
            "score",
            "grade",
            "entered_score",
            "points_deducted",
            "excused",
            "late",
            "missing",
            "late_policy_status",
            "seconds_late",
            "attempt",
            "submission_type",
            "workflow_state",
            "submitted_at",
            "graded_at",
        ],
        course_id=course_id,
    )


async def fetch() -> dict[str, list[pd.DataFrame]]:
    async with client() as c:
        courses = await get_courses(c)
        tables = {"courses": [courses]}

        print(f"Fetching {len(courses)} courses…", file=sys.stderr)
        course_data = await asyncio.gather(
            *(get_course_data(c, course_id) for course_id in courses["id"].tolist())
        )
        for data in course_data:
            for name, df in data.items():
                tables.setdefault(name, []).append(df)

        # unpublished assignments only have placeholder submissions
        assignments = pd.concat(tables["assignments"])
        published = assignments[assignments["published"]]
        print(
            f"Fetching submissions for {len(published)} assignments…", file=sys.stderr
        )
        tables["submissions"] = await asyncio.gather(
            *(
                get_submissions(c, course_id, assignment_id)
                for course_id, assignment_id in zip(
                    published["course_id"].tolist(), published["id"].tolist()
                )
            )
        )

    return tables


def load(con: duckdb.DuckDBPyConnection):
    tables = asyncio.run(fetch())
    for name, dfs in tables.items():
        df = pd.concat(dfs, ignore_index=True)
        if name == "students":
            df = df.drop_duplicates(subset="id")
        con.register("df", df)
        con.execute(f"CREATE OR REPLACE TABLE {name} AS SELECT * FROM df")
    con.unregister("df")

    # convenience view: one row per student per course, with final grades
    con.execute("""
        CREATE OR REPLACE VIEW student_grades AS
        SELECT
            c.term,
            c.term_start_at,
            c.name AS course,
            sec.name AS section,
            s.name AS student,
            s.sis_user_id AS uni,
            e.enrollment_state,
            e.current_score,
            e.current_grade,
            e.final_score,
            e.final_grade,
            c.id AS course_id,
            s.id AS user_id
        FROM enrollments e
        JOIN courses c ON c.id = e.course_id
        JOIN students s ON s.id = e.user_id
        LEFT JOIN sections sec ON sec.id = e.course_section_id
    """)

    for (name,) in con.execute("SHOW TABLES").fetchall():
        [(count,)] = con.execute(f"SELECT COUNT(*) FROM {name}").fetchall()
        print(f"{name}: {count} rows", file=sys.stderr)


def main():
    # the directory is only readable by you, and is deleted on exit
    with tempfile.TemporaryDirectory() as tmp:
        db_path = Path(tmp) / "courseworks.duckdb"
        with duckdb.connect(db_path) as con:
            load(con)
        subprocess.run(["duckdb", str(db_path)], check=False)


if __name__ == "__main__":
    main()
