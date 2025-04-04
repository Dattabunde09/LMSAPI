from pydantic import BaseModel, EmailStr, constr

class UserSignup(BaseModel):
    admin_name: str
    admin_num: str
    email_id: EmailStr
    password: constr(min_length=6) # type: ignore
    confirm_password: constr(min_length=6) # type: ignore
    
class Login(BaseModel):
    email_id:EmailStr
    password: str
    
class ResetPassword(BaseModel):
    email_id: EmailStr
    new_password: constr(min_length=6) # type: ignore
    confirm_password: constr(min_length=6) # type: ignore
    
class UpdateAdmin(BaseModel):
    email_id: EmailStr
    admin_name: str
    admin_num: str