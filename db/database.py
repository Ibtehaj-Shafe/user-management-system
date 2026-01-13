from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import DATABASE_URL

Engine = create_engine(DATABASE_URL)    #Engine to connect to the database
SessionLocal=sessionmaker(bind=Engine) #Handle to create sessions / db operations
Base = declarative_base()#Registry of ORM models

#Dependency of FASTAPI

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


