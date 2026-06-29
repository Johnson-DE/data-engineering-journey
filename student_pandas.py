import pandas as pd

students = {
    "Name" : ["John", "Prem", "Kavi", "Maddy", "Kani"],
    "Age" : [23, 20, 24, 21, 19],
    "Mark" : [89, 78, 97, 90, 84],
    "Department" : ["CSC", "ECE", "EEE", "MECH", "IEM"]
}

df = pd.DataFrame(students)

print("Lowest: ", df["Mark"].min())

#print("Highest: ", df["Mark"].max())

#print("Average: ", df["Mark"].mean())

# print(df[df["Mark"]>80])