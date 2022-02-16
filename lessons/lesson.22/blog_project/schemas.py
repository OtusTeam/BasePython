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


class UserSchemaBase(UserIn):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)


class UserSchemaOut(UserSchemaBase):

    class Config:
        orm_mode = True
