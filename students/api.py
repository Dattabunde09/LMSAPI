from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from students.schemas import AddStudent
from students.services import StudentService
from utils.database import get_db

router = APIRouter()

class StudentsAPI:

    @router.get("/get_students")
    def get_students(db: Session = Depends(get_db)):
        return StudentService.get_students(db)


    @router.post("/create_student")
    def create_student(student: AddStudent, db: Session = Depends(get_db)):
        return StudentService.create_student(student, db)