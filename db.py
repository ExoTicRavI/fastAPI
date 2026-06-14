#Import all the necessary dependencies
from fastapi import FastAPI
from sqlalchemy import create_engine,inspect
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


app = FastAPI()

#create a database URL
DATABASE_URL = "sqlite:///./test.db"

#start your engine based on your URL
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread" : False}
    )


#this works as class User(BaseModel). This will be the super class of the classes
Base = declarative_base()


#create a class based on your requirements this will define the schema of the database table.
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    name = Column(String)


#this line converts the code to the actual table
Base.metadata.create_all(bind = engine)

@app.get("/tables")
def get_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    return{
        "Tables" : tables,
        "Exists" : len(tables) > 0
    }