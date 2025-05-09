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

✅ **Example 1: Basic Pydantic Model**
  checkout pydantic_example_1.py file

🧱 **Example 2: Nested Models**
checkout pydantic_example_1.py file

✅ **Example 3: Custom Validator**
checkout pydantic_example_3.py file

---
💬 **Step 2: Building a FastAPI Application with Complex Pydantic Models**
A chatbot API was built using FastAPI and complex Pydantic models.

📁 File: main.py
checkout main.py

🔍 Explanation of the Code
Metadata: Nested model with a timestamp and a unique session ID

Message: Request model includes user_id, text, metadata, and optional tags

Response: Response model returning user_id, reply, and metadata

🔑 Endpoint Highlights
/chat/: Accepts Message, returns Response with nested metadata

/users/{user_id}: Returns user info with optional role

▶️ **How to Run This Project**

fastapi dev main.py

👩‍💻 Created By
Areeba Yaseen
“Learning FastAPI with real-world examples!”
