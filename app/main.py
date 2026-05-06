from fastapi import FastAPI
from app.routes import route
from app.db.database import engine, Base
from app.models import user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(route.router, prefix="/api/v1")

@app.get("/")
def HealthCheck():
    return {"Status": "OK"}