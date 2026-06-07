from fastapi import FastAPI

app = FastAPI()


#this is home route
@app.get("/")
def home():
    return{"Message":"Hello, This is Homepage"}

#this is about route
@app.get("/about")
def about():
    return{"Message":"Hello, This is About page"}


#this is user route
@app.get("/users")
def users():
    return{
        "users":["Sashi", "Sanchit", "Sabin"]
    }
