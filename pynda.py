from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class address(BaseModel):
    Country:str
    City:str

class User(BaseModel):
    Name:str
    Age:int
    Address:address

@app.post("/create_user")
def create_user(user:User):
    return user
