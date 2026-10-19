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


def pick(records: list[dict], cols: list[str], **extra) -> list[dict]:
    return [{**{c: r.get(c) for c in cols}, **extra} for r in records]


async def get_courses(client: httpx.AsyncClient) -> list[dict]:
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
    rows = pick(
        teaching,
        [
            "id",
            "name",
            "course_code",
            "sis_course_id",
            "workflow_state",
            # end_at isn't set in CourseWorks
            "start_at",
            "total_students",
        ],
    )
    # the term's start_at isn't set in CourseWorks either, so only the name is kept
    return [{**row, "term": c["term"].get("name")} for row, c in zip(rows, teaching)]


async def get_course_data(
    client: httpx.AsyncClient, course_id: int
) -> dict[str, list[dict]]:
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

    enrollment_rows = pick(
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

    return {
        "sections": pick(
            sections, ["id", "name", "sis_section_id"], course_id=course_id
        ),
        "students": pick(
            [e["user"] for e in enrollments],
            ["id", "name", "sortable_name", "sis_user_id", "login_id"],
        ),
        "enrollments": [
            {**row, **pick([e["grades"]], grade_cols)[0]}
            for row, e in zip(enrollment_rows, enrollments)
        ],
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
) -> list[dict]:
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


async def fetch() -> dict[str, list[dict]]:
    """Fetch the rows for each table. These are combined from all courses before turning them into DataFrames, since concatenating DataFrames with empty or all-null columns is deprecated in pandas."""

    async with client() as c:
        courses = await get_courses(c)
        tables = {"courses": courses}

        print(f"Fetching {len(courses)} courses…", file=sys.stderr)
        course_data = await asyncio.gather(
            *(get_course_data(c, course["id"]) for course in courses)
        )
        for data in course_data:
            for name, rows in data.items():
                tables.setdefault(name, []).extend(rows)

        # unpublished assignments only have placeholder submissions
        published = [a for a in tables["assignments"] if a["published"]]
        print(
            f"Fetching submissions for {len(published)} assignments…", file=sys.stderr
        )
        submissions = await asyncio.gather(
            *(get_submissions(c, a["course_id"], a["id"]) for a in published)
        )
        tables["submissions"] = [row for rows in submissions for row in rows]

    return tables


def load(con: duckdb.DuckDBPyConnection):
    tables = asyncio.run(fetch())
    for name, rows in tables.items():
        df = pd.DataFrame(rows)
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

    # like the Canvas Gradebook, but long rather than wide so that it works across courses: one row per student per assignment
    con.execute("""
        CREATE OR REPLACE VIEW gradebook AS
        WITH course_students AS (
            -- students can be enrolled in multiple sections of a course
            SELECT
                e.course_id,
                e.user_id,
                string_agg(DISTINCT sec.name, ', ' ORDER BY sec.name) AS section
            FROM enrollments e
            LEFT JOIN sections sec ON sec.id = e.course_section_id
            GROUP BY ALL
        )
        SELECT
            c.term,
            c.name AS course,
            cs.section,
            s.name AS student,
            s.sis_user_id AS uni,
            g.name AS assignment_group,
            a.name AS assignment,
            -- a.due_at,
            -- a.points_possible,
            -- sub.score,
            -- sub.grade,
            sub.score / nullif(a.points_possible, 0) AS percent,
            sub.excused,
            sub.late,
            sub.missing,
            sub.workflow_state,
            -- sub.submitted_at,
            c.id AS course_id,
            s.id AS user_id,
            a.id AS assignment_id
        FROM submissions sub
        -- leaves out users who aren't students, such as the test student
        JOIN course_students cs ON cs.course_id = sub.course_id AND cs.user_id = sub.user_id
        JOIN courses c ON c.id = sub.course_id
        JOIN students s ON s.id = sub.user_id
        JOIN assignments a ON a.id = sub.assignment_id
        LEFT JOIN assignment_groups g ON g.id = a.assignment_group_id
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
