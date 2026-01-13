from models.user import User
from crud.crud import CreateUser, Get_all_user, Get_user_by_id, Update_user, Delete_user
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schema.user import UserCreate, UserUpdate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/",response_model=UserResponse)
def create_user(user:UserCreate, db:Session=Depends(get_db)):
    return CreateUser(user, db)

@router.get("/",response_model=list[UserResponse])
def get_all_users(db:Session=Depends(get_db)):
    return Get_all_user(db)

@router.get("/{user_name}", response_model=UserResponse)
def get_user_by_name(user_name:str , db:Session=Depends(get_db)):
    return Get_user_by_id(user_name, db)

@router.put("/{user_name}", response_model=UserResponse)
def update_user(user_name:str, user:UserUpdate, db:Session=Depends(get_db)):
    return Update_user(user_name, user, db)

@router.delete("/{user_email}")
def delete_user(user_email:str, db:Session=Depends(get_db)):
    return Delete_user(user_email, db)