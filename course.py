"""This is a student record registring in course"""
from fastapi import FastAPI,HTTPException
from core.handler import st_handler
from core.handler.st_handler import create,get_all_data,update,delete
from schema.models import Student
app = FastAPI()


@app.post("/add/")
def post_data(student:Student):
    return create(student)
@app.get("/")
def get_data():
    return get_all_data()

@app.put("/update/{id}")
def update_data(id:int,student:Student):
    return update(id,student)

@app.delete("/delete/{id}")
def delete_data(id:int):
    return delete(id)
