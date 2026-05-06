from fastapi import APIRouter, Depends
from app.db.database import get_db
from app.models.user import User
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()