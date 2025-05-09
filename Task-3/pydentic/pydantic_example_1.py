from pydantic import BaseModel, ValidationError

# Base model class

class Student(BaseModel):
    name : str
    fatherName : str
    roll_num : int
    email : str 
    age: int | None = None #optianal field



#Valid Data Test
student_data = {"name": "Alice","fatherName":"Jhon" , "email": "alice@example.com", "age": 25 , "roll_num":12345}   #valid sample student data for testing model
student = Student(**student_data)     #Create Student instance from dictionary using unpacking
print(student)     #Display Student instance with field values
print(student.model_dump()) #Serialize Student model to dictionary using model_dump()



#Test Invalid Data
try:
    stident_data = Student(**{"name": "Alice", "fatherName": "Jhon", "email": 123, "age": 25, "roll_num": "12345int"})

except Exception as e:
    print(e)


# output for invalid data
# 2 validation errors for Student
# roll_num
#   Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='12345int', input_type=str]
#     For further information visit https://errors.pydantic.dev/2.11/v/int_parsing
# email
#   Input should be a valid string [type=string_type, input_value=123, input_type=int]