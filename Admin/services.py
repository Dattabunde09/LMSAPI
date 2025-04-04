from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from utils.database import sessionLocal, get_db
from Admin.models import Admin
from Admin.schemas import UserSignup, Login, ResetPassword, UpdateAdmin
from auth_utils import hash_password, verify_password

router = APIRouter() 
class AdminService:
    def signup(admin: UserSignup, db: Session = Depends(get_db)):
        try:
            existing_admin = db.query(Admin).filter(Admin.email_id == admin.email_id).first()
            if existing_admin:
                raise HTTPException(status_code=400, detail="Email already registered")
            
            if admin.password != admin.confirm_password:
                raise HTTPException(status_code=400, detail="Password does not match")
            
            hashed_password = hash_password(admin.password)
            
            new_admin = Admin(
                admin_name=admin.admin_name,
                admin_num=admin.admin_num,
                email_id=admin.email_id,
                password=hashed_password)
            db.add(new_admin)
            db.commit()
            db.refresh(new_admin)
            return {"message": "Admin registered successfully", "admin_id": new_admin.admin_id}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
        
    def login(admin: Login, db: Session = Depends(get_db)):
        try: 
            existing_admin = db.query(Admin).filter(Admin.email_id == admin.email_id).first()
            if not existing_admin:
                raise HTTPException(status_code=400, detail='Invalid email')
            
            if not verify_password(admin.password, existing_admin.password):
                raise HTTPException(status_code=400, detail="Invalid Password")
            
            return{"message": "Login Sucessfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error:{str(e)}")
        
    def get_admin(db: Session = Depends(get_db)):
        try:
            admin_list = db.query(Admin).all()  # Fetch all admins
            admin_data = [{"name": ad.admin_name, "number": ad.admin_num, "email": ad.email_id, "admin_id": ad.admin_id} for ad in admin_list]
            return {"total_admin": len(admin_list), "admin": admin_data}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
        
    def reset_password(data: ResetPassword, db: Session = Depends(get_db)):
        try:
            admin = db.query(Admin).filter(Admin.email_id == data.email_id).first()
            if not admin:
                raise HTTPException(status_code=400, detail="Admin not found")
            if data.new_password != data.confirm_password:
                raise HTTPException(status_code=400, detail="Password do not match")
            
            hashed_password = hash_password(data.new_password)
            admin.password= hashed_password
            db.commit()
            db.refresh(admin)
            return {"message": "Password update sucessfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Seriver Error: {str(e)}")
        
    def update_admin(data: UpdateAdmin, db: Session = Depends(get_db)):
        try:
            admin = db.query(Admin).filter(Admin.email_id == data.email_id).first()
            if not admin:
                raise HTTPException(status_code=400, detail="Admin not found")
            
            admin.admin_name = data.admin_name
            admin.admin_num = data.admin_num
            
            db.commit()
            db.refresh(admin)
            return {"message": "Update admin information"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Seriver Error: {str(e)}")
        