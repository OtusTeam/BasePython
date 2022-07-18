from uuid import uuid4

from pydantic import BaseModel, constr, Field


class UserBase(BaseModel):
    username: constr(min_length=3) = Field(..., example="john")


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    id: int = Field(..., example=123)


def generate_token():
    return str(uuid4())


class User(UserOut):
    token: str = Field(default_factory=generate_token)


# class Author(BaseModel):
#     name: str
#     bd: datetime
