# 🚀 Building a FastAPI Application with Pydantic Models

This project demonstrates how to build a FastAPI application while practicing various **Pydantic** features, including:

- ✅ Basic Model Validation
- ✅ Nested Models
- ✅ Custom Validators
- ✅ Real-time Chatbot API using FastAPI and Pydantic

---

## 📘 What is Pydantic?

**Pydantic** is a data validation and parsing library used in FastAPI to ensure that the data coming in (usually from API requests) is structured and valid. It uses Python type hints to enforce data types, and automatically throws clear errors if data is invalid.

---

## 🧪 Pydantic Practice Examples

Below are three examples demonstrating core Pydantic features.

---

### 🧩 Example 1: Basic `BaseModel` Usage pydantic_example_1.py

```python
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    fatherName: str
    roll_num: int
    email: str 
    age: int | None = None

Validates incoming fields and types

Automatically serializes and deserializes JSON data

Catches errors if types do not match (e.g., int as string)

🧱 Example 2: Nested Models  pydantic_example_2.py
from pydantic import BaseModel
from typing import List

class Course(BaseModel):
    title: str
    code: str
    credit_hours: int

class Student(BaseModel):
    name: str
    roll_num: int
    courses: List[Course]
Models inside models (nested data)

Useful for real-world relationships like students & courses

🧪 Example 3: Custom Validator      pydantic_example_3.py
from pydantic import BaseModel, EmailStr, field_validator
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

    @field_validator("name")
    def name_must_be_at_least_two_chars(cls, v):
        if len(v.strip()) < 2:
            raise ValueError("Name must be at least 2 characters long.")
        return v
Validates email using EmailStr

Custom validator ensures name has at least 2 characters

Step 2: Building a FastAPI Application with Complex Pydantic Models
💬 Chatbot API with FastAPI
Using all the concepts above, a chatbot API was built using FastAPI and complex Pydantic models.

📁 File: main.py
Endpoints:
GET / → Root message

GET /user/{user_id} → Returns user info with optional role

POST /chat/ → Takes in message and replies back

Models used:
Metadata: Generates timestamp and unique session ID

Message: Takes in text, user ID, metadata, and tags

Response: Returns reply along with metadata

▶️ How to Run This Project
📦 Step-by-step Commands:
Install FastAPI & Uvicorn:

bash
Copy
pip install fastapi uvicorn
Run the FastAPI App:

bash
Copy
uvicorn main:app --reload
Open in Browser:

Visit 👉 http://127.0.0.1:8000/docs to test API in Swagger UI

📄Create the Main Application File

#Import and setup
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel, Field
from datetime import datetime , UTC
from uuid import uuid4        

# FastAPI: Main framework to create APIs.
# HTTPException: to throw Error
# BaseModel & Field: to create Pydantic models .
# datetime & UUID: to create timely based  unique session.


# 2.App initialization
app = FastAPI(
    title="DACA Chatbot APi",
    description="A FastAPI-based API for a chatbot in the DACA tutorial series",
    version="0.1.0",
)

# 3.Pydantic Models
class Metadata(BaseModel):
    timestamp: datetime = Field(default_factory=lambda:datetime.now(tz=UTC))
    session_id : str =Field(default_factory=lambda:str(uuid4()))

#meassage model
class Message(BaseModel):
    text :str
    user_id : str
    metadata : Metadata
    tags : list[str] | None = None  #optional

#response model
class Response(BaseModel):
    user_id: str
    reply: str
    metadata: Metadata


#4.Routes
@app.get("/")
async def root():
    return {"message": "Welcome to the DACA Chatbot API"}


@app.get("/users/{user_id}")
async def get_user(user_id:str ,role:str | None = None):  # user_id: path se aata hai.
# role: optional query param. Agar nahi diya gaya to "guest" ban jata hai.
    user_info= {"user_id": user_id, "role": role if role else "guest"}   
    return user_info


#Post Chat

@app.post("/chat", response_model=Response)
async def Chat(message:Message):
    if not message.text.strip():
        raise HTTPException(status_code=400 , detail = "Message can not be empty")
    reply_text = f"Hello, {message.user_id}! You said: '{message.text}'. How can I assist you today?"
    return Response(user_id=message.user_id, reply=reply_text, metadata=Metadata())

Explanation of the Code
Complex Pydantic Models:

Metadata: A nested model with a timestamp (defaults to current UTC time) and session_id (defaults to a UUID).
Message: The request model, including user_id, text, metadata (nested Metadata), and optional tags.
Response: The response model, returning user_id, reply, and metadata.
Endpoint Updates:

The /chat/ endpoint now accepts a Message with nested Metadata and returns a Response with similar structure.
Run Code
fastapi dev main.py


👩‍💻 Created By
Areeba Yaseen
“Learning FastAPI with real-world examples!”
