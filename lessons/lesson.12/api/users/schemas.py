from uuid import uuid4
from pydantic import BaseModel, constr, Field


def generate_token() -> str:
    token = str(uuid4())
    print(token)
    return token


class UserBase(BaseModel):
    username: constr(min_length=3, max_length=32) = Field(..., example="john")


class UserOut(UserBase):
    id: int = Field(..., example=123)


class UserIn(UserBase):
    """
    Create user
    """


class User(UserOut):
    token: str = Field(default_factory=generate_token)
