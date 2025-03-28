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