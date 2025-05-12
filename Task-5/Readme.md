# Dependency Injection in FastAPI

## 🔍 What is Dependency Injection?

**Dependency Injection (DI)** is a design pattern used to separate object creation from its usage. Instead of creating objects directly in functions, you "inject" them. This makes your code:

- Easier to test  
- More modular  
- Cleaner and DRY (Don't Repeat Yourself)

FastAPI has built-in support for dependency injection. Just like in other languages (e.g., Java, JavaScript, Python), DI helps keep logic separate and reusable.

---

## 📘 Basic Example

```python
from fastapi import FastAPI, Depends

app = FastAPI()

class Service:
    def get_message(self):
        return "Hello from the service!"

def get_service():
    return Service()

@app.get("/")
def read_root(service: Service = Depends(get_service)):
    return {"message": service.get_message()}
```

✅ In this example:

get_service() is a dependency provider.

FastAPI automatically injects Service into the route handler.

🧪 Input Validation with Dependencies
```python

from fastapi import FastAPI, Depends, Query

app = FastAPI()

def user_dep(name: str = Query(None), password: str = Query(None)) -> dict:
    return {"name": name, "Valid": True}

@app.get("/user")
def get_user(user: dict = Depends(user_dep)):
    return user

```
This shows how to use query parameters as dependencies.
DI makes parameter validation reusable.

✅ Login Example using Dependency Injection
```python

from fastapi import Query, Depends, FastAPI

app = FastAPI()

def dep_login(username: str = Query(None), password: str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message": "Login successful"}
    else:
        return {"message": "Login failed"}

@app.get("/sign")
def get_login(user: dict = Depends(dep_login)):
    return user
```

⛔ Dependency Without Return (Just Check)
```python

from fastapi import FastAPI, Query, Depends, HTTPException

app = FastAPI()

def dep_check(name: str = Query(None), password: str = Query(None)):
    if not name:
        raise HTTPException(status_code=400, detail="Name is required")

@app.get("/login", dependencies=[Depends(dep_check)])
def login():
    return True
```
If a function doesn’t return anything but is still necessary (e.g., validation), you can directly inject it using dependencies=[].

🔁 Global Dependencies (Multiple Routes)
```python

from fastapi import FastAPI, Depends

def depfunc1(num: int):
    return num + 1

def depfunc2(num: int):
    return num + 1

app = FastAPI(dependencies=[Depends(depfunc1), Depends(depfunc2)])

@app.get("/main/{num}")
def get_main(num: int, num1: int = Depends(depfunc1), num2: int = Depends(depfunc2)):
    total = num + num1 + num2
    return f"Pakistan{total}"
```

📚 Injecting from Mock Database (Dict)
```python

from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()

blogs = {
    "1": "Generative AI",
    "2": "Machine Learning Blogs",
    "3": "Deep Learning Blogs",
}

users = {
    "8": "Areeba",
    "9": "Amna",
}

def get_blog(id: str):
    name = blogs.get(id)
    if not name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found")
    return name

def get_user(id: str):
    name = users.get(id)
    if not name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found")
    return name

@app.get("/blogs/{id}")
def get_blogs(blog_name: str = Depends(get_blog)):
    return blog_name

@app.get("/users/{id}")
def get_users(user_name: str = Depends(get_user)):
    return user_name
```

👨‍🏫 Dependency Injection using Classes
```python

from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()

blogs = {
    "1": "Generative AI",
    "2": "Machine Learning Blogs",
    "3": "Deep Learning Blogs",
}

users = {
    "8": "Areeba",
    "9": "Amna",
}

class GetObjectOr404:
    def __init__(self, model):
        self.model = model

    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object {id} not found")
        return obj

blog_dependency = GetObjectOr404(blogs)
user_dependency = GetObjectOr404(users)

@app.get("/blog/{id}")
def get_blog(blog_name: str = Depends(blog_dependency)):
    return blog_name

@app.get("/user/{id}")
def get_user(user_name: str = Depends(user_dependency)):
    return user_name
```

You can use classes to create reusable and efficient dependency handlers.

🗃 Simulated Database Session Example
```python

from fastapi import FastAPI, Depends

app = FastAPI()

development_db = ["DB for development"]

def get_db_session():
    return development_db

@app.get("/add_item")
def add_item(item: str, db: list = Depends(get_db_session)):
    db.append(item)
    return {"message": f"Added item {item}, all items: {db}"}
```

🧠 Summary
✅ Dependency Injection helps write modular, testable, and DRY code.

⚙️ FastAPI makes it easy using Depends().

🧱 You can inject functions, classes, or even connect to a database.

📦 You can reuse the same logic across multiple routes.
