"""This is a student record registring in course"""
from fastapi import FastAPI,HTTPException
from core.handler import st_handler
from core.handler.st_handler import Crud
from schema.models import Student,EmailClass



app = FastAPI()
obj = Crud()

@app.post("/add/")
def post_data(student:Student):
    return obj.create(student)
@app.get("/")
def get_data():
    return obj.get_all_data()

@app.put("/update/{id}")
def update_data(id:int,student:Student):
    return obj.update(id,student)

@app.delete("/delete/{id}")
def delete_data(id:int):
    return obj.delete(id)
@app.post("/send_email")
def email_testing(email:EmailClass):
    return obj.send_email(email)


