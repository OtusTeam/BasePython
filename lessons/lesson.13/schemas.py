from uuid import uuid4
from datetime import datetime

from pydantic import BaseModel, Field, validator, constr


class UserIn(BaseModel):
    username: constr(min_length=3)

    @validator("username")
    def validate_username(cls, value: str):
        if value.isdigit():
            raise ValueError("username cannot be digits-only")

        return value


class UserBase(UserIn):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)


class UserOut(UserBase):
    pass


def generate_token():
    token = str(uuid4())
    print("token:", repr(token))
    return token


class User(UserBase):
    token: str = Field(default_factory=generate_token)


#

class CalcInput(BaseModel):
    a: int
    b: int
