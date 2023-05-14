from fastapi import FastAPI,HTTPException
from schema.models import Student
from core.db.mongo_db import lib

def create(student: Student):
    lib.insert_one(student.dict())
    return {"message": "Data inserted successfully"}

def get_all_data():
    students =  lib.find({})
    details = []
    for document in students:
        detail = {'name':document['name'],'registration_no':document['registration_no'],'course_id':document['course_id'],'course_name':document['course_name']}
        details.append(detail)
    return {"details":details}

def update(id:int,student: Student):
     
    lib.update_one({"registration_no": id}, {"$set": student.dict()})
    return {"message": "Student data updated successfully!"}

    
def delete(id:int):
    lib.delete_one({'registration_no':id})
    return {"message": "Student record deleted successfully"}

   