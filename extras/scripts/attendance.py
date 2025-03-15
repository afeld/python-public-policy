import pandas as pd

NUM_CLASSES = 7
TOP_SCORE = NUM_CLASSES
FREEBIES = 1

file_path = (
    "~/Downloads/attendance_reports_attendance-264e4d14-1765-4396-b311-4d927b59566d.csv"
)
entries = pd.read_csv(
    file_path,
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

# pull the section number out
entries["Section"] = (
    entries["Section Name"].str.extract(r"INAFU6504_(\d{3})_").astype(int)
)

# TODO deal with students who switch sections

recording_counts = entries.groupby(["Student ID", "Student Name"]).size()
print("Students missing entries:\n")
print(recording_counts[recording_counts < NUM_CLASSES])

total_classes = entries["Class Date"].nunique()
assert total_classes == NUM_CLASSES

attended = entries[entries["Attendance"] == "present"]
attendance_counts = attended.groupby(["Student ID", "Student Name"]).size()
# print("\n-------------------\nAttendance counts:\n")
# print(attendance_counts)

# factor in the freebies
scores = attendance_counts + FREEBIES
scores[scores > TOP_SCORE] = TOP_SCORE
# print(scores)

# TODO write to CSV
# https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-import-grades-in-the-Gradebook/ta-p/807

lowered_scores = scores[scores < TOP_SCORE]
print(
    f"\n-------------------\nScores for students who missed more than {FREEBIES} class(es):\n"
)
print(lowered_scores.sort_values())
