# 🌍 FastAPI Hello World Project

This project demonstrates how to create a basic FastAPI application with two routes:
- `/simple_greet`: Returns a static "Hello World".
- `/greet_in_Diffrent_Lang`: Returns a random hello message in different languages.

---

## ✅ Step 1: Setting Up a FastAPI Project with `uv`

> **FastAPI** is a modern, high-performance web framework for building APIs with Python 3.10+ based on standard Python type hints.  
> **`uv`** is a fast and modern Python package/dependency manager that also handles virtual environments — perfect for quickly setting up clean Python projects.

We'll use the [`uv`](https://github.com/astral-sh/uv) CLI tool to set up our FastAPI project in a clean and modern way.

### 🔧 1. Install `uv`

If you haven't already installed `uv`, you can do so using the following command:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh

Alternatively, for macOS users:

brew install astral-sh/uv/uv

📁 2. Create Project Folder
uv init fastapi

Navigate to the directory where you want your project:
cd fastapi

🌱 3. Initialize Project & Virtual Environment
Run the following command to set up a virtual environment:
uv venv

Activate the virtual environment:

For Linux/macOS:
source .venv/bin/activate

For Windows:
.venv\Scripts\activate

➕ 4. Add FastAPI & Uvicorn
Next, add FastAPI and Uvicorn (ASGI server) to your project:
uv add fastapi[standard] uvicorn

📄 Step 2: Add Your API Code
Create a new file named main.py and add your FastAPI application code (as per the previous setup guide).

🚀 Step 3: Run Your API
Start the development server using Uvicorn:
fastapi dev main.py

🔍 Step 4: API Docs
FastAPI auto-generates interactive API documentation for your project. You can access these docs:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc UI → http://127.0.0.1:8000/redoc

🌐 Supported Languages
The /greet_in_Diffrent_Lang route will return greetings in various languages including:

English

Spanish

French

German

Italian

Japanese

Urdu

Hindi

Chinese (Simplified)

Russian

Happy coding with FastAPI and uv! 🚀



