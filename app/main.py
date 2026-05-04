from fastapi import FastAPI
from app.routes import route
app = FastAPI()

app.include_router(route.router, prefix="/api/v1")

@app.get("/")
def HealthCheck():
    return {"Status": "OK"}