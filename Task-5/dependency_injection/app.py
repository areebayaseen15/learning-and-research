
# dependency injection software code likhnay ka tareeka ha just like oop ya hr language ma hota ha hum python ma
#  dekhaingay
# fast api ma built in dependency injection ka concept ha
# ya java ma bhi ha javascript python  and more 

from fastapi import FastAPI, Depends
from typing import Annotated

                                       
app = FastAPI()

class Service: 
    def get_message(self):
        return "Hello from the service!"

def get_service():
    return Service()

@app.get("/")
def read_root(service: Service = Depends(get_service)):
    return {"message": service.get_message()}


# object creation and usage
# goal dependency injection yahi ha k object ka creation alg rha and usage alg

# dependency => db connection bnaya  kuch


# dependency injection  ya dendencies
# fast api ma hum chatay hai code testable ho same code pehla huw na ho ek jaga jama ho
# normal halat ma hum database ka connection krwatay hain 
# database sa connectivuty krwana 


#Example 2

from fastapi import FastAPI , Depends , Querry

app = FastAPI()

#The dependency injection
def user_dep(name : str=Querry(None) , passwaaord : str = Querry(None)) -> dict :
        return {"name" : name , "Valid" : True} 

#The path function / web endpoint
@app.get("/user")
def get_user(user:dict= Depends(user_dep)):
     return user


# kisi bhi normal function ko apnay rout ka sath k sath  munsalik krna wo e  do 3 4 10 function hoskatay hin 

# dependency injection ka mtlb yahin k database s connectivity 
# aesay function jo url pr hit krtay to wo direct call hota ap koi bhi function kisi url pr br br hit krna chah rhay to 
# ya modularity provide krta ha


####Example 3
def dep_login(username : str = Querry(None) , password : str = Querry(None)):
     if username == "admin" and password == "admin":
          return {"message" : "Login successfull"}
     else:
          return {"message" : "Login failed"}
     

@app.get("/sign")
def get_login(user:Annotated[dict, Depends(dep_login)]):
     return user


#################
#example 4

def dep_check(name:str= Querry(None) , password:str = Querry(None)):
     if not name:
          raise
     
@app.get("/login" , dependencies=[Depends(dep_check)])  #aesa function jismay koi value return na ho to usay direct rout k andar  inject kr do
def login():
     return True     

############## example 5
def depfunc1(num:int):
     num = int(num)
     num += 1
     return num

def depfunc2(num:int):
     num = int(num)
     num += 1
     return num

#important bat jb ap saray urls pr ya bohat saray urls pr ek hi deependencies inject krna chahtay hain to object bnatay 
#waqtt app ka instance bnatay waqt pass hoga issay ya faida hoga k hamaray jo bhi routes hongay un sb pr wo dependency
#injection call hogi 

app = FastAPI(dependencies =[Depends(depfunc1) , Depends(depfunc2)])

@app.get("/main/{num}")
def get_main(num:int , num1:int = Depends(depfunc1) , num2 : int = Depends(depfunc2)):
     #Assuming you want to use num1 and num2 in some way
     # 1 , 2 ,2 
     total= num + num1 + num2
     return f"Pakistan{total}"  #output Pakistan 5
#hum multiple dependencies injection function bhi pass kr sktay hain

#Annotated ma
@app.get("/main/{num}")
def get_main(num:int , num1:Annotated[int , Depends(depfunc1)] , num2 : Annotated[int , Depends(depfunc2)]):
     #Assuming you want to use num1 and num2 in some way
     # 1 , 2 ,2 
     total= num + num1 + num2
     return f"Pakistan{total}"  #output Pakistan 5