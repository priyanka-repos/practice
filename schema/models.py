from pydantic import BaseModel


class Student(BaseModel):
    name: str
    registration_no: int
    course_id: int
    course_name: str
    price: int