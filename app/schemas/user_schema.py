from pydantic import BaseModel
from typing import Optional


class UserRegister(BaseModel):
    username: str
    email: str
    password: str
    profile_image_url: Optional[str] = None


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    profile_image_url: Optional[str] = None