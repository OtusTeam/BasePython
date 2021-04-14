from datetime import datetime
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field


def generate_token():
    return str(uuid4())


class Item(BaseModel):
    name: str


class UserBase(BaseModel):
    username: str
    is_staff: bool = False
    created_at: datetime = Field(default_factory=datetime.now)


class User(UserBase):
    id: int
    token: str = Field(default_factory=generate_token)

    def update_username(self, upd: "UpdateUsername"):
        return self.update_username_from_str(upd.username)

    def update_username_from_str(self, new_username: str):
        self.username = new_username
        self.save()

    def save(self):
        print("saved!", self)


class UserOut(BaseModel):
    user: User


class UpdateUsername(BaseModel):
    username: str
