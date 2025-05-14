
from fastapi import FastAPI 
from pydantic import BaseModel , EmailStr, Field , constr , field_validator
from datetime import date
from typing import Literal

class UserCreate(BaseModel):
    username: constr = Field(min_length=3, max_length=20)
    email : EmailStr


class UserRead(BaseModel):
    username:constr

class Tasks(BaseModel):
    title:str
    description:str 
    due_date : date
    status: Literal["pending", "in-progress", "done"]
    user_id : int

    @field_validator("due_date")
    @classmethod
    def validate_due_date(cls , value):
      if value < date.today():
        raise ValueError("Due Date can not be in the pase")
      return value
    
