from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from datetime import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

class Base(DeclarativeBase): 
    pass

class Person(Base):
    __tablename__ = "people" 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(String, default="female")
    created_at = Column(DateTime, default=datetime.utcnow)

SessionLocal = sessionmaker(autoflush=False, bind=engine)