from pydantic import BaseModel

class UserRequest(BaseModel):
    id: int
    name: str
    password: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
