from uuid import uuid4

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str = Field(
        ...,
        example="john",
        min_length=3,
        max_length=40,
    )


class UserIn(UserBase):
    ...


class UserOut(UserBase):
    id: int = Field(..., example=123)

    class Config:
        orm_mode = True
