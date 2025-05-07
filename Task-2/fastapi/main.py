
import random    
from fastapi import FastAPI


app = FastAPI()

#basic greet message
simple_greet = "Hello World"

#greet message in multiplle languages
greet_in_Diffrent_Lang = [
     {"language": "English", "message": "Hello World"},
        {"language": "Spanish", "message": "Hola Mundo"},
        {"language": "French", "message": "Bonjour le monde"},
        {"language": "German", "message": "Hallo Welt"},
        {"language": "Italian", "message": "Ciao Mondo"},
        {"language": "Japanese", "message": "こんにちは世界 (Konnichiwa Sekai)"},
        {"language": "Urdu", "message": "سلام دنیا"},
        {"language": "Hindi", "message": "नमस्ते दुनिया"},
        {"language": "Chinese (Simplified)", "message": "你好，世界"},
        {"language": "Russian", "message": "Привет мир"}
]

@app.get("/simple_greet")
def get_message():
    "Return hello message "
    return {"greet message:" , simple_greet}


@app.get("/greet_in_Diffrent_Lang")
def get_message():
    "Return hello messages in different languages"
    item = random.choice(greet_in_Diffrent_Lang)
    return {
        "greet_in_language": item["language"],
        "message": item["message"]
    }
