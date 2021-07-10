from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class UserIn(BaseModel):
    username: str


class UserBase(UserIn):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)
    status: str = "active"


def generate_token():
    token = str(uuid4())
    print("Create Token", token)
    return token


class User(UserBase):
    token: str = Field(default_factory=generate_token)


class UserOut(UserBase):
    pass


class AuthorBase(BaseModel):
    nickname: str
    user: User


class Author(AuthorBase):
    pass


class AuthorIn(BaseModel):
    nickname: str


class AuthorOut(AuthorBase):
    user: UserOut


class PostBase(BaseModel):
    title: str
    body: str


class Post(PostBase):
    id: int
    author: Author


class PostIn(PostBase):
    """"""


class PostOut(Post):
    author: AuthorOut
