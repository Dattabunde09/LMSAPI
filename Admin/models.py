from sqlalchemy import Column, String,UUID
from sqlalchemy.orm import relationship
from utils.database import Base
from uuid import uuid4

class Admin(Base):
    __tablename__ = 'admin'
    
    admin_name = Column(String(100), nullable=False)
    admin_num = Column(String(10), nullable=False)
    email_id = Column(String, unique=True, nullable=False)
    admin_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False)
    password = Column(String, nullable=False)