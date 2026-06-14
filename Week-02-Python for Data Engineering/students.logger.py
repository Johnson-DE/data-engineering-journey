"""import logging

logging.basicConfig (
    filename = "app.log",
    level = logging.ERROR
)

try:
    
    name = str(input("Enter a Name: "))
    mark = int(input("Enter a Mark: "))

    if mark<0 or mark>100:
        raise ValueError("Mark should be between 0-100")

except Exception as e:
    print("Error: ", e)
    logging.error(f"Error  Occured: {e}")

else:
    print("Student Name: ", name)
    print("Marks: ", mark)

finally:
    print("Student Marks Program Completed")

"""
