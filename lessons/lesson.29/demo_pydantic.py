from datetime import datetime
from typing import Optional
from uuid import uuid4
from pydantic import BaseModel, Field


def create_user(username: Optional[str]  = None):
    """
    :param username:
    :return:
    """
    if username is None:
        username = 'asdqweqwe'  # a VERY random string
    return User(id=0, username=username)


def generate_token() -> str:
    token = str(uuid4())
    print("new token", token)
    return token


class UserBase(BaseModel):
    username: str
    is_staff: bool = False
    date_banned: Optional[datetime] = None

    class Config:
        extra = "forbid"
        # extra = Extra.ignore


class User(UserBase):
    id: int
    token: str = Field(default_factory=generate_token)

    # class Config:
    #     orm_mode = True


class UserOut(BaseModel):
    user: User


if __name__ == "__main__":

    u = User(id=1, username="john")
    admin = User(id=42, username="admin", is_staff=True)

    print("user", repr(u))
    print("admin", repr(admin))

    user_data = {
        "id": 2,
        "username": "user",
        # "is_admin": True,
    }

    u2 = User(**user_data)

    print(repr(u2))


    user_dict = u2.dict(exclude={'id'})
    # user_dict = u2.dict(exclude_unset=True)
    print(user_dict)
