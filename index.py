from fastapi import FastAPI, Request
from fastapi import Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/')
def home(request: Request):
    return templates.TemplateResponse(
        request = request,
        name = "index.html",
    ) 
        
@app.post('/submit')
def submit(request : Request, username : str = Form(...), age : int = Form(...)):
    return templates.TemplateResponse(
        request = request,
        name ="result.html",
        context = {
            "username" : username,
            "age" : age
        }
    )