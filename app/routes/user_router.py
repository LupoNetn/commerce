from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schema.user_schema import UserResponse
from app.service.user_service import get_user_by_id, get_all_users

router = APIRouter()

@router.get("/", response_model=List[UserResponse], status_code=status.HTTP_200_OK)
def read_all_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    return users

@router.get("/{id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def read_user(id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(id, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user