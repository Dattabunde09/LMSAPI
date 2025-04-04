from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from utils.config import DATABASE_URL
import os

load_dotenv()

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set, Check your environment variable or config files.")

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

def init_db():
    from Admin.models import Admin
    from Books.models import Books
    Base.metadata.create_all(bind=engine)
    
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()