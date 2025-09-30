from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UserBaseSchema(BaseModel):
    username: str
    email: str
    full_name: str


class UserCreateSchema(UserBaseSchema):
    """
    Create new user schema
    """


class UserReadSchema(UserBaseSchema):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    created_at: datetime
