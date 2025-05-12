#his ka nder hum kia chah rhay ka agay ja kr hmaray pass databasse ho to hum like variable set bhi krwa rha
# usay fetch bhi krna chah rha to hum ek aesi api bna chah rhay k hum kisi bhi blog ki id pass kr den jo iska title ho
# ho to agr wo available ho to wo dict return krday isi trhan user ho to uska username return krday 
# to ya data base consider kr len abhi to hum usay as a dict consider krain lkn agay ja kr ya database sa conectivity 
# ho kr injection dependency k zariya usay access krnay ki koshish kraingay hamaray pass 2 dictionary ha usay ap 
# data base consider kr lain is dect ma hum id pass kraingay agr wo id mojood ha to is ka text return krday or agr id 
# mojood na ho to not found ya koi bhi msg return krday ya error generate krana ha to exception handle kr sktay

# HTTPException => jo hum http url pr exception raise krna chah rhay  
# status code hotay hain hamaray pass like 404 to wo bhi hum use krna chah rhay


from fastapi import FastAPI , Depends , HTTPException , status
from typing import Annotated


blogs ={
    "1" : "Generative Ai",
    "2" : "Machine learning Blogs",
    "3" : "Deep Learning Blogs",
}


Users={
    "8" : "Areeba",
     "9" : "Amna",
}
                ####Dependency through function##########
#blog dep fiunction
def get_blog(id:str):
    name = blogs.get(id)
    if not name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Blog {id} not found")
    
    return name


 # user dep function
def get_user(id:str):
    name = Users.get(id)
    if not name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"User {id} not found")
    return name
    

app = FastAPI(title="Learn Dependency Injection")  #main heading

# #Blog_dependency
@app.get("/blogs/{id}")
def get_blogs(blog_name : Annotated[str, Depends(get_blog)]):
    return blog_name


#User_dependency
@app.get("/users/{id}")
def get_user(user_name : Annotated[str, Depends(get_user)]):
    return user_name


       ####################################
#Call back function ya call jb hum object bna letay hain or object bnanay k bad directly us class k instance object 
# bna rhay uskay agay round bracket open close krtay hain to hamaesha callable function apka backend kr call hota ha
# jo round bracket sa bnta ha 
# python ma hr cheez object ha isliya comparatively dusri languages k ya slow ha lkn power ful zada ha kjo bhi cheez ko 
# ap round bracket ma call krtay hain usmay __call__ aesa functon hoga


                         ####Dependency through Class##########
#class ma bhi kisi cheez ko dependent bna sktay lkn wo uska callable method call kraiga  isay effecient krnay ka maqsad
# ya ha k ap ismay koi bhoi object jesay searching k liya blogs and users hain to hum aesa  function bnanan chah rhay 
# k jo bhi hamaray pass database /model ha uskay against  ja k chek kray means k same cheez ko multiple time 
# check krnay k liya uski class bna di different obj k sath 

class GetObjectOr404():
    def __init__(self , model)->None:   #model databse ko hi keh rha to model yato blog hoga ya user hoga
        self.model = model           #constuctor ma jo model/object pass huwa us model ka attribute bna kr or jo bhi dict pass ki ha model ma uskay sath munsalik krdaiga

    def __call__   (self , id:str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Onject {id} not found")
        return obj
    
app = FastAPI(titlle = "Learn Dependency Injection")    

#Create Obj  blog dependency 
blog_dependency = GetObjectOr404(blogs)

@app.get("/blog/{id}")
def get_blog(blog_name : Annotated[str, Depends(blog_dependency)]):
    return blog_name

#Create obj User Dependency
user_dependency = GetObjectOr404(Users)


@app.get("/user/{id}")
def get_blog(blog_name : Annotated[str, Depends(user_dependency)]):
    return blog_name


#Example connectivity with data base

from fastapi import FastAPI , HTTPException , status , Depends

development_db = ["DB for development"]

def get_db_session():
    return development_db
app = FastAPI()

@app.get("/add_item")
def get_db_session(item:str , db:Annotated[list , Depends(get_db_session)]):
    db.append(item)
    print(db)
    return {"message" : f"added item  {item} , all Items {db}"}
