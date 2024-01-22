from uuid import uuid4

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    """
    Create User Schema
    """


class UserOut(UserBase):
    """
    User Out Schema (API representation)
    """
    id: int = Field(example=123)


def generate_token() -> str:
    token = str(uuid4())
    print("New user token:", token)
    return token


class User(UserBase):
    id: int
    token: str = Field(default_factory=generate_token)
