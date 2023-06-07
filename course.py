"""This is a student record registring in course"""
from fastapi import APIRouter,HTTPException
from core.handler import st_handler
from core.handler.st_handler import Crud
from schema.models import Student,EmailClass
from scripts.constants.app_constants import APis



data_router = APIRouter()
obj = Crud()

@data_router.post(APis.create_api)
def post_data(student:Student):
    return obj.create(student)
@data_router.get(APis.view_all_data_api)
def get_data():
    return obj.get_all_data()

@data_router.put(APis.update_api)
def update_data(id:int,student:Student):
    return obj.update(id,student)

@data_router.delete(APis.delete_api)
def delete_data(id:int):
    return obj.delete(id)
@data_router.post(APis.send_email_api)
def email_testing(email:EmailClass):
    return obj.send_email(email)


