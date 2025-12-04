from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict


class UserBaseSchema(BaseModel):
    username: str
    email: EmailStr | None
    full_name: str = ""


class UserCreateSchema(UserBaseSchema):
    """
    Create new user
    """


class UserReadSchema(UserBaseSchema):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    created_at: datetime
