from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from utils.database import sessionLocal, get_db
from Admin.models import Admin
from Admin.schemas import UserSignup, Login, ResetPassword, UpdateAdmin
from Admin.services import AdminService

router = APIRouter()

class AdminAPI:
    @router.post("/signup")
    def signup(admin: UserSignup, db: Session = Depends(get_db)):
        return AdminService.signup(admin, db)
    
    @router.post("/login")
    def login(admin: Login, db: Session = Depends(get_db)):
        return AdminService.login(admin, db)
    
    @router.get("/get")
    def get_admin(db: Session = Depends(get_db)):
        return AdminService.get_admin(db)
    
    @router.put("/update_password")
    def reset_password(data: ResetPassword, db: Session = Depends(get_db)):
        return AdminService.reset_password(data, db)
    
    @router.put("/update_admin")
    def update_admin(data: UpdateAdmin, db: Session = Depends(get_db)):
        return AdminService.update_admin(data, db)