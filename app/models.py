from sqlalchemy import Column, Integer, String, Enum
from .database import Base
import enum

class Role(str, enum.Enum):
    STUDENT = "student"
    INSTRUCTOR = "instructor"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String, default=Role.STUDENT)
