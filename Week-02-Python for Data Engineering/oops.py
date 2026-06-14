# class - example:
#A Class is a blueprint.

"""class student:
    pass

student1 = student()

print(student1)"""

#object - example:
#Object = Instance of a Class.

"""class car:
    pass

car1 = car()
car2 = car()

print(car1)
print(car2)"""

# __init__()
# _init__() is called automatically when an object is created.

#  self example
"""class employee:
    def __init__(self):
        print("employee1 Created")
emp1 = employee()"""

# self,name example
"""class student:
    def __init__(self,name):
        self.name = name

student1 = student("Johnon")
print(student1.name)"""

# self, name, salary example
"""class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

emp1 = employee("Johnson", 15000)
emp2 = employee("Premnath", 20000)

print(emp1.name)
print(emp1.salary)

print(emp2.name)
print(emp2.salary)"""

# def display method

"""class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def display(self):
        print("Name: ", self.name)
        print("Mark: ", self.mark)

stu1 = student("Johnson", 90)
stu2 = student("premnath", 85)

stu1.display()
stu2.display()"""


# Student Management System

class students:
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
    def display_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Mark: ", self.mark)
stu1 = students("John",23,95)
stu2 = students("Prem",25,90)
stu3 = students("Mari",24,85)

stu1.display_details()
stu2.display_details()
stu3.display_details()
