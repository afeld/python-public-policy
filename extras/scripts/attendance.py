import pandas as pd

NUM_CLASSES = 7
TOP_SCORE = NUM_CLASSES
FREEBIES = 1

ROLL_CALL_CSV = (
    "~/Downloads/attendance_reports_attendance-264e4d14-1765-4396-b311-4d927b59566d.csv"
)
# get by clicking into the Assignment and getting from the URL
ASSIGNMENT_ID = 1405957
GRADEBOOK_FILE = "attendance.csv"
STUDENT_UNIQUE_COLS = ["Student ID", "Student Name", "Section Name", "Section"]


def normalize_sections(entries: pd.DataFrame):
    """For students who switch sections, use their final section."""

    student_info = entries.drop_duplicates(subset=["Student ID"], keep="last")
    student_info = student_info[["Student ID", "Section Name"]]

    entries = entries.drop(columns=["Section Name"])
    return entries.merge(student_info, on="Student ID")


def get_entries(filename: str):
    entries = pd.read_csv(
        filename,
        index_col=False,
        usecols=[
            "Section Name",
            "Student Name",
            "Student ID",
            "Class Date",
            "Attendance",
        ],
        parse_dates=["Class Date"],
    )

    entries = normalize_sections(entries)
    # pull the section number out
    entries["Section"] = (
        entries["Section Name"].str.extract(r"INAFU6504_(\d{3})_").astype(int)
    )

    return entries


def print_heading(text: str):
    print(f"-------------------\n\n{text.upper()}:\n")


def print_students(students: pd.Series):
    print(students.droplevel(["Student ID", "Section Name"]))
    print()


def validate(entries: pd.DataFrame):
    recording_counts = entries.groupby(STUDENT_UNIQUE_COLS).size()
    print_heading("Students missing entries")
    print_students(recording_counts[recording_counts < NUM_CLASSES])

    total_classes = entries["Class Date"].nunique()
    assert total_classes == NUM_CLASSES


def compute_scores(entries: pd.DataFrame):
    attended = entries[entries["Attendance"] == "present"]
    attendance_counts = attended.groupby(STUDENT_UNIQUE_COLS).size()
    # print_heading("Attendance counts")
    # print_students(attendance_counts)

    # factor in the freebies
    scores = attendance_counts + FREEBIES
    scores[scores > TOP_SCORE] = TOP_SCORE

    return scores


def write_canvas_csv(scores: pd.Series):
    """https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-import-grades-in-the-Gradebook/ta-p/807"""

    attendance_col = f"Attendance ({ASSIGNMENT_ID})"

    gradebook = (
        scores.reset_index(name=attendance_col)
        .drop(columns=["Section"])
        .rename(
            columns={
                # Roll Call has `FIRST LAST`, gradebook has `LAST, FIRST`. Shouldn't matter.
                "Student Name": "Student",
                "Student ID": "ID",
                "Section Name": "Section",
            }
        )
    )
    gradebook.to_csv(GRADEBOOK_FILE, index=False)

    print(f"Now upload {GRADEBOOK_FILE} to CourseWorks Gradebook.")


def run():
    entries = get_entries(ROLL_CALL_CSV)
    validate(entries)

    scores = compute_scores(entries)
    print_heading("Scores")
    print_students(scores)

    lowered_scores = scores[scores < TOP_SCORE]
    print_heading(f"Scores for students who missed more than {FREEBIES} class(es)")
    print_students(lowered_scores.sort_values())

    write_canvas_csv(scores)


run()
