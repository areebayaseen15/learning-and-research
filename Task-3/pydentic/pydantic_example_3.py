from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from typing import List

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class StudentAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: List[Address]

    # custom validator  Name must be at least 2 characters long 
    @field_validator("name")
    def name_must_be_at_least_two_chars(cls, v):
        if len(v.strip()) < 2:
            raise ValueError("Name must be at least 2 characters long.")
        return v

#  Valid input
# student = StudentAddress(
#     id=1,
#     name="Areeba",
#     email="areeba@example.com",
#     addresses=[
#         {"street": "123 Main St", "city": "Lahore", "zip_code": "54000"}
#     ]
# )
# print(student.model_dump())

# Invalid input (uncomment to test)
try:
    invalid_student = StudentAddress(
        id=3,
        name="A",  # Too short
        email="charlieexample.com",  # Invalid due to EmailStr
        addresses=[{"street": "789 Pine Rd", "city": "Chicago", "zip_code": "60601"}],
    )
except ValidationError as e:
    print(e)
