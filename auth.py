from fastapi import FastAPI
from pydantic import BaseModel
from passlib.context import CryptContext

app = FastAPI()

pwd_context = CryptContext(
    schemes = ["bcrypt"],
    deprecated = "auto"
)

users = []

class CreateUser(BaseModel):
    username : str
    password : str


class UserLogin(BaseModel):
    username : str
    password : str


@app.post('/register')
def register(user : CreateUser):
    hashed_password = pwd_context.hash(user.password)

    users.append({
        "username" : user.username,
        "password" : hashed_password
    })

    return {"Message" : "User Created"}

@app.post('/login')
def login(user : UserLogin):
    for db_user in users:
        if db_user['username'] == user.username:
            if pwd_context.verify(user.password,db_user["password"]):
                return {"Message" : "Login Successful"}
            return {"Message" : "Password Wrong"}
    return {"Message" : "User Does Not Exist"}