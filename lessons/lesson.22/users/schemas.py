from uuid import uuid4

from pydantic import BaseModel, constr, Field


class UserBase(BaseModel):
    username: constr(min_length=3) = Field(..., example="john")


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    id: int = Field(..., example=123)

    class Config:
        orm_mode = True


def generate_token():
    return str(uuid4())
