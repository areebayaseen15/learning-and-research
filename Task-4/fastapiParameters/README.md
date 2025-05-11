# FastAPI Parameters Notes

## 📘 What are FastAPI Parameters?

In FastAPI, **parameters** are values sent with the HTTP request which the backend can receive and use for logic, filtering, validation, etc. Parameters can be sent in different ways depending on their **type and usage**, such as:

- **Path parameters**: Passed as part of the URL path
- **Query parameters**: Passed after the `?` in the URL
- **Body parameters**: Sent in the request body (usually as JSON)
- **Header parameters**: Sent in the request headers
- **Cookies**: Sent via the browser’s cookies
- **Form data**: Sent through HTML forms
- **File uploads**: Sent when uploading files

---

## 1️⃣ Path Parameters

These are passed as part of the URL and are commonly used to identify a specific resource.

### ✅ Example:
```
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/user/{id}/my/{name}")
def get_user(
    id: int = Path(..., ge=1, title="User ID"),
    name: str = Path(..., min_length=2, max_length=30, title="User Name")
):
    return {"id": id, "name": name}
```

----
🔍 Explanation:
Path(...) means it's required.

ge=1 ensures the ID is ≥ 1.

min_length and max_length validate the string.

2️⃣ Query Parameters
These come after the ? in the URL and are passed as key-value pairs.
----

✅ Example:
```python
Copy
Edit
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/student")
def get_student(
    id: int = Query(..., ge=1),
    name: str = Query(..., min_length=2, max_length=30)
):
    return {"id": id, "name": name}
🔍 URL Format:
bash
Copy
Edit
/student?id=1&name=Areeba
```
----

3️⃣ Body Parameters
Used to receive structured data like JSON in the request body, usually via a POST request.

----

✅ Example:
```python
Copy
Edit
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    id: int

@app.post("/new_user")
def create_user(user: User = Body(...)):
    return {"user": user}
```

4️⃣ Path + Query + Body Combined
You can combine all three types in a single API.
----

✅ Example:
```python
Copy
Edit
@app.post("/new_student/{age}")
def create_student(
    age: int = Path(..., ge=1, le=120),
    q: str = Query(..., min_length=1),
    user: User = Body(...)
):
    return {
        "age": age,
        "query": q,
        "user": user
    }```

5️⃣ Header Parameters
Headers carry meta-information like tokens, User-Agent, etc.
----

✅ Example:
```python
Copy
Edit
from fastapi import Header

@app.get("/get-header/")
def get_headers(user_agent: str = Header(...), token: str = Header(None)):
    return {
        "User-Agent": user_agent,
        "Token": token
    }
```

6️⃣ Cookie Parameters
Cookies are stored in the browser and sent automatically with requests.
----
✅ Example:
```python
Copy
Edit
from fastapi import Cookie

@app.get("/get-cookie/")
def get_cookie(session_id: str = Cookie(None)):
    return {"Session ID": session_id}
```

7️⃣ Form Data
Form fields submitted using HTML forms with application/x-www-form-urlencoded content type.
----
✅ Example:
```python
Copy
Edit
from fastapi import Form

@app.post("/submit-form/")
def submit_form(name: str = Form(...), email: str = Form(...)):
    return {"name": name, "email": email}```

8️⃣ File Uploads
Used to receive files uploaded via forms using multipart/form-data.
----

✅ Example:
```python
Copy
Edit
from fastapi import File, UploadFile

@app.post("/upload-file/")
def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }```
----
✅ Summary of Parameters
Parameter              Type	WhereIt Comes From	      Use Case Example
Path	               URL path                        /user/10
Query	               URL query string	               ?name=Areeba
Body	               Request body (JSON)	          {"name": "Ali"}
Header                	HTTP headers	                Auth tokens
Cookie               	Browser cookies	              Sessions/login
Form	               HTML form                       fields	name=email
File	                File upload	                   .pdf, .png

📂 Check the main.py file to see example implementations of each parameter type.

