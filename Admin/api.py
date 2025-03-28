from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from utils.database import sessionLocal, get_db
from Admin.models import Admin
from Admin.schemas import UserSignup, Login
from Admin.services import AdminService

router = APIRouter()

class AdminAPI:
    @router.post("/signup")
    def signup(admin: UserSignup, db: Session = Depends(get_db)):
        return AdminService.signup(admin, db)
    
    @router.post("/login")
    def login(admin: Login, db: Session = Depends(get_db)):
        return AdminService.login(admin, db)