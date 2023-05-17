from pydantic import BaseModel


class Student(BaseModel):
    name: str
    registration_no: int
    course_id: int
    course_name: str
    price: int

class EmailClass(BaseModel):
        rec_email: str
        subject: str
        # body: str    