import pandas as pd

NUM_CLASSES = 7
TOP_SCORE = NUM_CLASSES
FREEBIES = 1

ROLL_CALL_CSV = (
    "~/Downloads/attendance_reports_attendance-264e4d14-1765-4396-b311-4d927b59566d.csv"
)


def normalize_sections(entries: pd.DataFrame):
    """For students who switch sections, use their final section."""

    student_info = entries.drop_duplicates(subset=["Student ID"], keep="last")
    student_info = student_info[["Student ID", "Section Name"]]

    entries = entries.drop(columns=["Section Name"])
    return entries.merge(student_info, on="Student ID")


def print_heading(text: str):
    print(f"\n-------------------\n{text}:\n")


def run():
    entries = pd.read_csv(
        ROLL_CALL_CSV,
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

    STUDENT_UNIQUE_COLS = ["Student ID", "Student Name", "Section Name", "Section"]

    recording_counts = entries.groupby(STUDENT_UNIQUE_COLS).size()
    print("Students missing entries:\n")
    print(recording_counts[recording_counts < NUM_CLASSES])

    total_classes = entries["Class Date"].nunique()
    assert total_classes == NUM_CLASSES

    attended = entries[entries["Attendance"] == "present"]
    attendance_counts = attended.groupby(STUDENT_UNIQUE_COLS).size()
    print_heading("Attendance counts")
    print(attendance_counts)

    # factor in the freebies
    scores = attendance_counts + FREEBIES
    scores[scores > TOP_SCORE] = TOP_SCORE
    print_heading("Scores")
    print(scores)

    # TODO write to CSV
    # https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-import-grades-in-the-Gradebook/ta-p/807

    lowered_scores = scores[scores < TOP_SCORE]
    print_heading(f"Scores for students who missed more than {FREEBIES} class(es)")
    print(lowered_scores.sort_values())


run()
