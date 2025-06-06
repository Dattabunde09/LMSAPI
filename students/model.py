from sqlalchemy import Column, String, Integer
from utils.database import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email=Column(String(100),nullable=False)
    phone=Column(String(100),nullable=False)
    email=Column(String(100),nullable=False)
    book_id = Column(Integer)
    admin_id = Column(String(100),nullable=False)
