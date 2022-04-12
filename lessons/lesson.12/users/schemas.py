from uuid import uuid4

from pydantic import BaseModel, constr, Field


class UserBase(BaseModel):
    username: constr(min_length=8)


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    id: int = Field(..., example=123)


def generate_token():
    token = str(uuid4())
    print("new token", token)
    return token


class User(UserOut):
    token: str = Field(default_factory=generate_token)
