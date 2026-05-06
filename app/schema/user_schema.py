from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    name: str
    password: str
    email: str

class LoginUserRequest(BaseModel):
    password: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
