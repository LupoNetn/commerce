from app.db.database import get_db
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.service.user_service import create_user
from app.schema.user_schema import CreateUserRequest, UserResponse

router = APIRouter()

@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def signup_user(request: CreateUserRequest, db: Session = Depends(get_db)):
    new_user = create_user(request, db)
    return new_user