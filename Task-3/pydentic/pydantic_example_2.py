from pydantic import BaseModel
from typing import List


#nested model for Course
class Course(BaseModel):
    title: str
    code: str
    credit_hours: int


# Define the main model Student, which includes a list of Course models
class Student(BaseModel):
    name: str
    roll_num: int
    courses: List[Course]  # List of nested models


#Create test data in dictionary form
student_data = {
    "name": "Areeba",
    "roll_num": 123,
    "courses": [
        {"title": "Python", "code": "PY101", "credit_hours": 3},
        {"title": "Math", "code": "MTH202", "credit_hours": 4}
    ]
}
#Convert dictionary data into Student Pydantic model instance
student = Student(**student_data)
print(student)   #rint the model object (with field validation and formatting)
print(student.model_dump())  #converting the model back to a dictionary
