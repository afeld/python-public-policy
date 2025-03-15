import pandas as pd

file_path = (
    "/content/attendance_reports_attendance-264e4d14-1765-4396-b311-4d927b59566d.csv"
)
df = pd.read_csv(file_path)

df.columns = df.columns.str.strip()
df = df.rename(
    columns={
        "Course ID": "Section Name",
        "Student ID": "Student Name",
        "Class Date": "Date",
        "Attendance": "Status",
    }
)

df = df[["Section Name", "Student Name", "Date", "Status"]]
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
df = df.reset_index(drop=True)
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%y", errors="coerce")
df = df.loc[:, ~df.columns.duplicated()]

total_classes = df["Date"].nunique()


attendance_counts = (
    df.groupby(["Student Name", "Date"])["Status"]
    .apply(lambda x: (x == "present").sum())
    .reset_index()
)

total_attended = attendance_counts.groupby("Student Name")["Status"].sum().reset_index()
total_attended.columns = ["Student Name", "Total Attended"]

students_all_present = total_attended[
    total_attended["Total Attended"] == total_classes
]["Student Name"].tolist()
students_missed_one = total_attended[
    total_attended["Total Attended"] == total_classes - 1
]["Student Name"].tolist()

filtered_students = pd.DataFrame(
    {
        "Student Name": students_all_present + students_missed_one,
        "Attendance Status": ["All Present"] * len(students_all_present)
        + ["Missed One"] * len(students_missed_one),
    }
)

# students who missed more than one class
students_missed_more_than_one = total_attended[
    total_attended["Total Attended"] < total_classes - 1
]["Student Name"].tolist()

missed_more_than_one_df = pd.DataFrame(
    {
        "Student Name": students_missed_more_than_one,
        "Attendance Status": ["Missed More Than One"]
        * len(students_missed_more_than_one),
    }
)

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.expand_frame_repr", False)

print("Students who attended all classes or missed only one:")
print(filtered_students)
print("\nStudents who missed more than one class:")
print(missed_more_than_one_df)
