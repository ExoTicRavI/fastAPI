from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    salary:float

@app.post("/create_user")
def user(user:User):
    return{
        "Message" : "User has been Created",
        "Data": user
    }
