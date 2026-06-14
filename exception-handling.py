#Program 1

"""try:
    num = int(input("Enter a Number: "))
    print(num)
except ValueError:
    print("Please Enter a Valid Number")"""
    
# program  2

"""try:
    a = int(input("A: "))
    b = int(input("B: "))
    print(a/b)
except ZeroDivisionError:
    print("divided by Zero is not allowed" )"""
    
#Program 3

"""try:
    names = ["prem", "john"]
    print(names[5])
except IndexError: 
    print("Index Doesn't Exist")"""
    
# Program 4

"""try:
    student = {
        "name" : "john",
        }
    print(student["age"])
except KeyError:
    print("Key doesn't found")"""
    
# Program 5

"""try:
    file = open("file.txt")
except FileNotFoundError:
    print("File Not Found")"""
    
#Calculator Program

"""try:
    
    num1  = int(input("Enter a number1: "))
    num2  = int(input("Enter a number2: "))
    
    operation = input("choose (+,-,*,/):")
    
    if operation == "+":
        print(num1 + num2)
    
    elif operation == "-":
        print(num1 - num2) 
        
    elif operation == "*":
        print(num1 * num2)
    
    elif operation == "/":
        print(num1 / num2)
        
    else:
        print("Invalid Operation")

except ZeroDivisionError:
    print("Cannot Divided By Zero")

except ValueError:
    print("Enter Numbers Only")"""

# sTUDENTS MARK PROGRAM

"""try:
    name = str(input("Enter a Student Name: "))
    marks = int(input("Enter a Mark: "))
    if marks>100 :
        print("Marks Doesn't Higher than 100")
    else:
        print("Name: ", name)
        print("marks: ", marks)
except ValueError:
    print("Enter Numbers Only")"""