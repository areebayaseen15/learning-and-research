from fastapi import FastAPI 
from pydantic import BaseModel

# rest api wo jo response json ma bhjti ha


app = FastAPI()

# Path Parameter
@app.get("/user/{id}/my/{name}")   #yahan curly braces ka under k variable ma data store hoga
def root_def(id :int , name: str):    #yahan us data ko pass kr sktay  type lgana sa auto convet hoga data us time or agr convertable na hua to error yega
    try:
        return{
            "status": "Ok",
            "data":{
                "name": "Areeba Yaseen",
               " age": "25",
                 "id" : id,   # aesay  us data ko use krsktay 
                 "name" : name,
                "email" : "areebayaseen15@gmail.com"

            }}

    except Exception as e:
        return{
            "message" : str(e),
            "status" : "error",
            "data" : None

        }   
    

    # lkn issay hum koi zada data ni bhj sktay hum just ek value sa zada bji bhj sktay 
    #  ismay fixed value bhi bhj sktay 
    # beech beech ma  lkn is trhan data bhjna safety k hawaly sa acaha ni zada data bhjnna ho tb bhi acha ni

##############################


 #Querry parameter key value pairs ma data dena url k bad ? lgana or queerries dena 

    
@app.get("/student")  
def root_def(id :int , name: str):    #yahan bs querry parameter da adingy
    try:
        return{
            "status": "Ok",
            "data":{
                "name": "Areeba Yaseen",
                 "id" : id,   # aesay  us data ko use krsktay 
                 "name" : name,
                "email" : "areebayaseen15@gmail.com"

            }}

    except Exception as e:
        return{
            "message" : str(e),
            "status" : "error",
            "data" : None

        }   
   #################################3
   #  
# Body paramete ya sb sa secure smjha jata ha ismay ek to koi limition ni upper sa data encrypt ho kr
#  jata k hacker hack bhi kr lay to usany ni pt ki ha ya wohi standard jismay backend frontrnd ko data deta ha wesai hum bhi frontend sa backend ko d rhay
#lkn ab method get ki jaga post lgaiga

class User(BaseModel):
    name: str
    email:str
    id:int
    
@app.post("/new_user")  
def create_user(user:User): 
    try:
        return{
            "status": "Ok",
            "data":{
                "user" :user
               
            }}

    except Exception as e:
        return{
            "message" : str(e),
            "status" : "error",
            "data" : None

        }   
    

    #body parameter ko recieve krnay k liya model bnana paraiga jo hum pydantix sa bnayenfay jb hum parameter ma variable laingay uski type
    #wo class rkhaingay jo basemodel sa inherit ho rhi to uskay key ki value jo hogi to wo smjh jayega frontend ko data bhjana
    #body parameter ma




    #hum 3no path parameters bhi ek ma da sktay hain

       
@app.post("/new_student/{age}")  
def create_user(age:int ,q:str,  user:User): 
    try:
        return{
            "status": "Ok",
            "data":{
                "querry": q,
                "user" :user,
                "age" : age
               
            }}

    except Exception as e:
        return{
            "message" : str(e),
            "status" : "error",
            "data" : None

        }   
    
########################################
