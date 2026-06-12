from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    name : str = Field(...,min_length=3, max_length=50)
    age : int = Field(..., gt= 0, le= 100)
    email : str = Field(..., min_length=10, max_length= 60)
    password : str = Field(..., min_length=5, max_length=30)

class UserResponse(BaseModel):
    name : str
    age : int
    email : str

@app.post('/user', response_model=UserResponse)
def create_user(user:User):
    saved_user = {
        "name" : user.name,
        "age" : user.age,
        "email" : user.email
    }

    return saved_user