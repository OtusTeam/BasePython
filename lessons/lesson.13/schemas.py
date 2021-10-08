from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class CalcInput(BaseModel):
    a: int
    b: int


class UserIn(BaseModel):
    username: str


class UserBase(UserIn):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)
    status: str = "active"


class UserOut(UserBase):
    pass


def generate_token():
    token = str(uuid4())
    print("Created token", repr(token))
    return token


class User(UserBase):
    token: str = Field(default_factory=generate_token)
