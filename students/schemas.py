from pydantic import BaseModel

class AddStudent(BaseModel):
    name: str
    email:str
    phone:str
    book_id: int
    admin_id: int
