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

✅ Example 1: Basic Pydantic Model

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

🧱 Example 2: Nested Models

python
Copy
Edit
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

🧪 Example 3: Custom Validator

python
Copy
Edit
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

💬 Step 2: Building a FastAPI Application with Complex Pydantic Models
A chatbot API was built using FastAPI and complex Pydantic models.

📁 File: main.py

🧱 Import and Setup
python
Copy
Edit
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime, UTC
from uuid import uuid4
🚀 App Initialization
python
Copy
Edit
app = FastAPI(
    title="DACA Chatbot APi",
    description="A FastAPI-based API for a chatbot in the DACA tutorial series",
    version="0.1.0",
)
📦 Pydantic Models
python
Copy
Edit
class Metadata(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    session_id: str = Field(default_factory=lambda: str(uuid4()))
python
Copy
Edit
class Message(BaseModel):
    text: str
    user_id: str
    metadata: Metadata
    tags: list[str] | None = None
python
Copy
Edit
class Response(BaseModel):
    user_id: str
    reply: str
    metadata: Metadata
🌐 Routes
python
Copy
Edit
@app.get("/")
async def root():
    return {"message": "Welcome to the DACA Chatbot API"}
python
Copy
Edit
@app.get("/users/{user_id}")
async def get_user(user_id: str, role: str | None = None):
    user_info = {"user_id": user_id, "role": role if role else "guest"}
    return user_info
python
Copy
Edit
@app.post("/chat", response_model=Response)
async def Chat(message: Message):
    if not message.text.strip():
        raise HTTPException(status_code=400, detail="Message can not be empty")
    reply_text = f"Hello, {message.user_id}! You said: '{message.text}'. How can I assist you today?"
    return Response(user_id=message.user_id, reply=reply_text, metadata=Metadata())
🔍 Explanation of the Code
Metadata: Nested model with a timestamp and a unique session ID

Message: Request model includes user_id, text, metadata, and optional tags

Response: Response model returning user_id, reply, and metadata

Endpoint Highlights
/chat/: Accepts Message, returns Response with nested metadata

/users/{user_id}: Returns user info with optional role

▶️ How to Run This Project
Run the app:

bash
Copy
Edit
fastapi dev main.py
👩‍💻 Created By
Areeba Yaseen
“Learning FastAPI with real-world examples!”
