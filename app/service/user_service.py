from app.schema.user_schema import CreateUserRequest
from app.models.user import User
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_user(request: CreateUserRequest, db: Session):
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    new_user = User(
        name = request.name,
        email = request.email,
        hashed_password = get_password_hash(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_id(id: int, db: Session):
    return db.query(User).filter(User.id == id).first()