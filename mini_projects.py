import pandas as pd

df = pd.read_csv("students.csv")

#print(df)

# Print Average

"""print("Average: ", df["Mark"].mean())"""

# Print Highest Mark

"""print("Highest Mark:", df["Mark"].max())"""

# Print Lowest Mark
"""print("Lowest Mark:", df["Mark"].min())"""

# Print only above 80

"""print(df[df["Mark"]>80])"""

# Add Result Column

df["Result"] = df["Mark"].apply(
    lambda mark: "Pass" if mark >= 70 else "Fail"
)

print(df)

#Load (Save New CSV)

df.to_csv("student_report.csv", index=False)

print("Report Generated Successfully")