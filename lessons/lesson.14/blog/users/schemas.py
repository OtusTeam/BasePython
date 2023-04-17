from uuid import uuid4

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str = Field(
        ...,
        example="john",
        min_length=3,
        max_length=20,
    )


class UserIn(UserBase):
    ...


class UserOut(UserBase):
    id: int = Field(..., example=123)


def generate_token():
    token = str(uuid4())
    print("New token:", token)
    return token


class User(UserBase):
    id: int
    token: str = Field(default_factory=generate_token)
