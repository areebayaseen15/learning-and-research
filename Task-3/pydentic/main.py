
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