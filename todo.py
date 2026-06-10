from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

#this is the schema to define what type of data the variables will hold
class Todo(BaseModel):
    id:int
    Name:str
    Completion:bool


#this is the post API to send the data from the user to the backend
@app.post('/todos')
def create_todo(todo:Todo):
    todos.append(todo)
    return {"Message": "TODOs added","data":todos}


#this API will get all the data that is available in the list
@app.get('/todos')
def get_todos():
    return todos


#this API will get the data based on the id provided by the user
@app.get('/todos/{todo_id}')
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return{"Message":"TODO not found!"}


#this API will update the existing TODO available based on the id provided
@app.put('/todo/{todo_id}')
def update_todo(todo_id:int, updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return{
                "Message":"TODOs updated",
                "Data":updated_todo
            }
    return{"TODO not found!"}


#this is to delete the TODO that we have created
@app.delete('/todos/{todo_id}')
def delete_todo(todo_id:int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"Message":"Todo Deleted"}
    return {"Message":"Error TODO not found!"}