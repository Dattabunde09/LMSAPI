from sqlalchemy import Column, String, Integer, Date
from utils.database import Base

class Books(Base):
    __tablename__ = 'books'
    
    book_name = Column(String(100), nullable=False, unique=True)
    book_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    auther_name = Column(String(100), nullable=False)
    category = Column(String(100), nullable=False)
    status = Column(String(100))
    issued_date = Column(Date)
    return_date = Column(Date)
    