FastAPI Parameters – Guide

This guide explains different types of parameters used in FastAPI. Each parameter type plays an important role in how data is sent and received in your API.

1. Path Parameters

Sent as part of the URL.

Used for fixed structure paths.

@app.get("/user/{id}/my/{name}")
def read_user(id: int = Path(..., ge=1), name: str = Path(..., min_length=2, max_length=30)):
    return {"id": id, "name": name}

2. Query Parameters

Sent after ? in the URL.

Used for optional or filter data.

@app.get("/student")
def get_student(id: int = Query(..., ge=1), name: str = Query(..., min_length=2, max_length=30)):
    return {"id": id, "name": name}

3. Body Parameters

Sent in the body of a POST or PUT request.

Used for sending structured JSON data.

class User(BaseModel):
    name: str
    email: str
    id: int

@app.post("/new_user")
def create_user(user: User = Body(...)):
    return {"user": user}

4. Combination (Path + Query + Body)

You can combine all parameter types.

@app.post("/new_student/{age}")
def create_student(age: int = Path(..., ge=1, le=120), q: str = Query(...), user: User = Body(...)):
    return {"age": age, "query": q, "user": user}

5. Header Parameters

Sent via HTTP headers.

Used for metadata like tokens or user-agents.

@app.get("/get-header/")
def get_custom_headers(user_agent: str = Header(...), token: str = Header(None)):
    return {"User-Agent": user_agent, "Token": token}

6. Cookie Parameters

Sent in the Cookie header.

Used for session and state management.

@app.get("/get-cookie/")
def get_cookie_value(session_id: str = Cookie(None)):
    return {"Session ID": session_id}

7. Form Data

Sent via application/x-www-form-urlencoded.

Typically used in HTML forms.

@app.post("/submit-form/")
def submit_form(name: str = Form(...), email: str = Form(...)):
    return {"name": name, "email": email}

8. File Uploads

Used to upload files in form submissions.

@app.post("/upload-file/")
def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename, "type": file.content_type}

📁 Checkout main.py to see example code for all parameter types in action.

