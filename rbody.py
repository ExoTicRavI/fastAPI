from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name : str
    email : str
    password: str


class UserResponse(BaseModel):
    name : str
    email : str


@app.post("/users", response_model=UserResponse)
def create_user(user:User):
    saved_user = {
        "name" : user.name,
        "email" : user.email,
        "password" : user.password
    }

    return saved_user
