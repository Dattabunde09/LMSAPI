from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from students.model import Student
from students.schemas import AddStudent
from utils.database import get_db

class StudentService:

    def create_student(student: AddStudent, db: Session = Depends(get_db)):
        try:
            # No need to check by ID anymore unless you're checking by other fields
            new_student = Student(
                name=student.name,
                email=student.email,
                phone=student.phone,
                
                book_id=student.book_id,
                admin_id=student.admin_id
            )
            db.add(new_student)
            db.commit()
            db.refresh(new_student)
            return {"message": "Student created successfully", "student_id": new_student.id}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


    def get_students(db: Session = Depends(get_db)):
        try:
            students = db.query(Student).all()
            student_data = [{
                "id": s.id,
                "name": s.name,
                "email":s.email,
                "phone":s.phone,
                "book_id": s.book_id,
                "admin_id": s.admin_id
            } for s in students]
            return {"total_students": len(student_data), "students": student_data}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
