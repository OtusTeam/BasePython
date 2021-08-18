from datetime import datetime

from pydantic import BaseModel, Field


class UserIn(BaseModel):
    username: str


class UserBase(UserIn):
    id: int
    created_at: datetime
    is_staff: bool = False


class User(UserBase):
    auth_token: str


class UserOut(UserBase):

    class Config:
        orm_mode = True
