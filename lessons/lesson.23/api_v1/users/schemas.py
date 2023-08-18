import uuid

from pydantic import BaseModel, Field, ConfigDict


class UserBase(BaseModel):
    username: str = Field(
        example="john",
        min_length=3,
        max_length=20,
    )


class UserIn(UserBase):
    """
    Create user
    """


class UserOut(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., example=123)
