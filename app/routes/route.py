from fastapi import APIRouter
from app.routes import user_router,products_router

router = APIRouter()

router.include_router(user_router.router, prefix="/users",tags=["users"])
router.include_router(products_router.router, prefix="/products",tags=["products"])