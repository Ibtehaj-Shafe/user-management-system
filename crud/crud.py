from schema.user import UserCreate, UserUpdate, UserResponse
from models.user import User
from sqlalchemy.orm import Session
from fastapi import HTTPException
from dependencies.password import hash_password

def CreateUser(user: UserCreate, db: Session):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = hash_password(user.password)
    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def Get_all_user(db:Session):
    users=db.query(User).all()
    return users


def Get_user_by_id(user_name:str, db:Session):
    user=db.query(User).filter(User.name==user_name).first()
    if not user:
            raise HTTPException(status_code=404, detail="User not found")
    return user
    
def Update_user(user_name:str, user:UserUpdate, db:Session):
    db_user=db.query(User).filter(User.name==user_name).first()
    if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
    db_user.name = user.name
    db_user.email = user.email
    db_user.role = user.role
    db.commit()
    db.refresh(db_user)
    return db_user

def Delete_user(user_email:str, db:Session):
    db_user=db.query(User).filter(User.email==user_email).first()
    if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"detail": "User deleted successfully"}