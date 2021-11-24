from datetime import datetime

from pydantic import BaseModel, Field


class CalcInput(BaseModel):
    a: int
    b: int


class UserIn(BaseModel):
    username: str


class UserBase(UserIn):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)


class UserOut(UserBase):
    class Config:
        orm_mode = True
