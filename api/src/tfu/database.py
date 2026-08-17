from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


URL_BANCO = "sqlite:///ecommerce.db"
engine = create_engine(URL_BANCO, 
                       connect_args={"check_same_thread": False})
SessionLocal = sessionmaker

class Base(DeclarativeBase):
    pass