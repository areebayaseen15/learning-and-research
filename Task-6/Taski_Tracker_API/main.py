
#     3️⃣ Create FastAPI App File
# Create main.py (or app.py)

# Import FastAPI and create an instance of it

# Set up dummy storage (you can use simple dictionaries or lists for now)



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
    


# 4️⃣ Implement User Endpoints
# 🚀 POST /users/
# Accept UserCreate

# Validate input

# Add to dummy database

# Return UserRead

# 🚀 GET /users/{user_id}
# Fetch user from dummy data

# Return UserRead

app = FastAPI()

#. Set Up Dummy Database (as per step)

user_db = {}


@app.post("/users")
def create_user(user:UserCreate ):
    user_id = len(user_db) + 1
    user_db[user_id] = user
    return UserRead(username = user.username)    # Return UserRead model only
 


@app.get("/users/{user_id}")
def get_user(user_id :int):    #Accept user_id
    user = user_db.get(user_id)
    if user:
        return UserRead(username = user.username) 
    return {"error": "User not found"}


# 5️⃣ Implement Task Endpoints
# 🚀 POST /tasks/
# Accept a task creation model

# Validate and store task

# Return full task data

# 🚀 GET /tasks/{task_id}
# Fetch and return task data

# 🚀 PUT /tasks/{task_id}
# Only allow updating status

# Validate that status is within allowed values

# 🚀 GET /users/{user_id}/tasks
# Filter and return all tasks for the given user

# Add this above your endpoints
task_db = {}

# 🚀 POST /tasks/
@app.post("/tasks")
def create_task(task: Tasks):
    task_id = len(task_db) + 1
    task_db[task_id] = task
    return task

# 🚀 GET /tasks/{task_id}
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = task_db.get(task_id)
    if task:
        return task
    return {"error": "Task not found"}

# 🚀 PUT /tasks/{task_id}
@app.put("/tasks/{task_id}")
def update_task(task_id: int, status_update: dict):
    task = task_db.get(task_id)
    if task:
        new_status = status_update.get("status")
        if new_status in ["pending", "in-progress", "done"]:
            task.status = new_status
            return {"message": "Status updated", "task": task}
        return {"error": "Invalid status value"}
    return {"error": "Task not found"}

# 🚀 GET /users/{user_id}/tasks
@app.get("/users/{user_id}/tasks")
def get_user_tasks(user_id: int):
    user_tasks = [task for task in task_db.values() if task.user_id == user_id]
    return user_tasks
