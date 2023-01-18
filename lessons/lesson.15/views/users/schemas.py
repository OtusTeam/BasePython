from uuid import uuid4

from pydantic import BaseModel, constr, Field


class UserBase(BaseModel):
    username: constr(min_length=3, max_length=32)


class UserIn(UserBase):
    pass


def generate_token():
    return str(uuid4())


class UserOut(UserBase):
    id: int


class User(UserBase):
    id: int
    token: str = Field(default_factory=generate_token)

