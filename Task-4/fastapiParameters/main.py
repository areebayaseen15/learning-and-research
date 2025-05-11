from fastapi import Cookie, FastAPI, Path, Query, Body
from pydantic import BaseModel
from fastapi import FastAPI, Header

app = FastAPI()

# -------- PATH PARAMETER VALIDATION --------
@app.get("/user/{id}/my/{name}")
def root_def(
    id: int = Path(..., title="User ID", ge=1),         # id must be >= 1
    name: str = Path(..., title="User Name", min_length=2, max_length=30)
):
    try:
        return {
            "status": "Ok",
            "data": {
                "name": "Areeba Yaseen",
                "id": id,
                "name": name,
                "email": "areebayaseen15@gmail.com"
            }
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": "error",
            "data": None
        }


# -------- QUERY PARAMETER VALIDATION --------
@app.get("/student")
def root_def(
    id: int = Query(..., ge=1, description="Student ID must be greater than 0"),
    name: str = Query(..., min_length=2, max_length=30, description="Student name")
):
    try:
        return {
            "status": "Ok",
            "data": {
                "name": "Areeba Yaseen",
                "id": id,
                "name": name,
                "email": "areebayaseen15@gmail.com"
            }
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": "error",
            "data": None
        }


# -------- BODY PARAMETER VALIDATION --------
class User(BaseModel):
    name: str
    email: str
    id: int

@app.post("/new_user")
def create_user(user: User = Body(...)):
    try:
        return {
            "status": "Ok",
            "data": {
                "user": user
            }
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": "error",
            "data": None
        }


# -------- MIX OF PATH + QUERY + BODY VALIDATION --------
@app.post("/new_student/{age}")
def create_student(
    age: int = Path(..., ge=1, le=120, description="Age must be between 1 and 120"),
    q: str = Query(..., min_length=1, max_length=50),
    user: User = Body(...)
):
    try:
        return {
            "status": "Ok",
            "data": {
                "query": q,
                "user": user,
                "age": age
            }
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": "error",
            "data": None
        }

 ###################################
#header parameter
@app.get("/get-header/")
def get_custom_headers(user_agent: str = Header(...), token: str = Header(None)):
    return {
        "User-Agent Header": user_agent,
        "Custom Token Header": token
    }



#Cookie

@app.get("/get-cookie/")
def get_cookie_value(session_id: str = Cookie(None)):
    return {
        "Your Cookie Session ID": session_id
    }


#form data
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/submit-form/")
def submit_form(name: str = Form(...), email: str = Form(...)):
    return {
        "Name": name,
        "Email": email
    }


#upload files

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/upload-file/")
def upload_file(file: UploadFile = File(...)):
    return {
        "Filename": file.filename,
        "Content Type": file.content_type
    }
