"""import pandas as pd

students = {
    "Name" : ["John", "Prem", "Praveen", "Kavin", "Naveen"],
    "Age" : [23,24,25,26,27],
    "Mark" : [87, 96, 78, 89, 90],
    "Department" : ["ECE", "EEE", "IEM", "MECH", "CSC"]
}

df = pd.DataFrame(students)

print(df)"""

# Practice 1 – Select Multiple Columns

"""import pandas as pd

students = {
    "Name" : ["John", "Prem", "Praveen", "Kavin", "Naveen"],
    "Age" : [23,24,25,26,27],
    "Mark" : [87, 96, 78, 89, 90],
    "Department" : ["ECE", "EEE", "IEM", "MECH", "CSC"]
}

df = pd.DataFrame(students)

print(df[["Name", "Mark"]])"""

# Practice 2 – Filter Data

"""import pandas as pd

students = {
    "Name" : ["John", "Prem", "Praveen", "Kavin", "Naveen"],
    "Age" : [23,24,25,26,27],
    "Mark" : [87, 96, 78, 89, 90],
    "Department" : ["ECE", "EEE", "IEM", "MECH", "CSC"]
}

df = pd.DataFrame(students)

print(df[df["Mark"]>=90])
"""

# Practice 3 – Average Marks

"""import pandas as pd

students = {
    "Name" : ["John", "Prem", "Praveen", "Kavin", "Naveen"],
    "Age" : [23,24,25,26,27],
    "Mark" : [87, 96, 78, 89, 90],
    "Department" : ["ECE", "EEE", "IEM", "MECH", "CSC"]
}

df = pd.DataFrame(students)

print(df["Mark"].mean())"""

# Practice 4 – Highest & Lowest Marks

"""import pandas as pd

students = {
    "Name" : ["John", "Prem", "Praveen", "Kavin", "Naveen"],
    "Age" : [23,24,25,26,27],
    "Mark" : [87, 96, 78, 89, 90],
    "Department" : ["ECE", "EEE", "IEM", "MECH", "CSC"]
}

df = pd.DataFrame(students)

print(df["Mark"].max())
print(df["Mark"].min())"""

# Practice 5 – Sort by Marks

import pandas as pd

students = {
    "Name" : ["John", "Prem", "Praveen", "Kavin", "Naveen"],
    "Age" : [23,24,25,26,27],
    "Mark" : [87, 96, 78, 89, 90],
    "Department" : ["ECE", "EEE", "IEM", "MECH", "CSC"]
}

df = pd.DataFrame(students)

print(df.sort_values(by="Age", ascending=False))