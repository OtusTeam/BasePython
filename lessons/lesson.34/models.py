from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str


class ItemUpdate(ItemBase):
    """Update Item"""


class Item(ItemBase):
    id: int


def generate_token():
    token = str(uuid4())
    print("Token:", token)
    return token


class UserBase(BaseModel):
    username: str
    created_at: datetime = Field(default_factory=datetime.now)


class User(UserBase):
    id: int
    token: str = Field(default_factory=generate_token)

    def update_username(self, upd: "UserUpdateUsername"):
        self.username = upd.username
        self.save()

    def save(self):
        print("saved user", self)


class UserOut(UserBase):
    id: int


class UserUpdateUsername(BaseModel):
    username: str
