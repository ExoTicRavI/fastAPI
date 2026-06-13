from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel

app = FastAPI()

books = []

class Book(BaseModel):
    id : int
    name : str
    
@app.post("/add_books", status_code = status.HTTP_201_CREATED)
def add_book(book:Book):
    books.append(book)
    return {
        "Message" : "Books Has Been Added",
        "data" : books
    }

@app.get("/get_books/{id}")
def get_books(id:int):
    for book in books:
        if book.id == id:
            return book
    
    if book.id != id:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= {
                "Message" : "Book Not Found"
            }
        )
    
@app.delete("/del_books/{id}")
def del_books(id: int):
    for index,book in enumerate(books):
        if book.id == id:
            books.pop(index)
            return Response(status_code = status.HTTP_204_NO_CONTENT)
    
    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail={
            "Message" : "Book Not Found"
        }
    )