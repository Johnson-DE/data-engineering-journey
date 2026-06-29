#Practice 1 – Create DataFrame

"""import pandas as pd

data = {
    "Name" : ["Johnson", "Premnath"],
    "Age" : [23, 25]
}

df = pd.DataFrame(data)

print(df)"""


# Practice 2 – Print Name column

"""import pandas as pd

data = {
    "Name" : ["Johnson", "Premnath"],
    "Age" : [23, 25]
}

df = pd.DataFrame(data)

print(df["Name"])"""

# Practice 3 – Print first row

"""import pandas as pd

data = {
    "Name" : ["Johnson", "Premnath"],
    "Age" : [23, 25]
}

df = pd.DataFrame(data)

print(df.iloc[0])"""

# Practice 4 – Add Salary column

"""import pandas as pd

data = {
    "Name" : ["Johnson", "Premnath"],
    "Age" : [23, 25]
}

df = pd.DataFrame(data)
df["salary"] = [10000,20000]

print(df)
"""
# Mini Project - Employee DataFrame

"""import pandas as pd

employee = {
    "Name" : ["Johnson", "Premnath", "Mathan"],
    "Age" : [22,25,28],
    "salary" : [10000,20000,30000]
}

df = pd.DataFrame(employee)

print(df)"""

# Mini Project - Student DataFrame

"""import pandas as pd

students = {
    "Name" : ["Johnson", "Premnath", "Praveen"],
    "Age" : [23,24,25],
    "Mark" : [87,98,90],
    "Dept" : ["ECE", "EEE", "CSC"]
}

df = pd.DataFrame(students)
df["Results"] = ["Pass", "Pass", "Fail"]

print(df["Name"])
print(df.iloc[1])
print(df)"""

#Special Commonds using DE

"""print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())"""
