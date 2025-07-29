from datetime import datetime

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    name: str
    username: str
    email: str


class UserCreateSchema(UserBaseSchema):
    """
    Create new user
    """


class UserReadSchema(UserBaseSchema):
    id: int
    created_at: datetime
