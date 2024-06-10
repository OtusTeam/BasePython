
from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from fastapi_jsonapi.schema_base import BaseModel, Field, RelationshipInfo

if TYPE_CHECKING:
#     from .post import PostSchema
    from .user_bio import UserBioSchema


class UserBaseSchema(BaseModel):
    """User base schema."""

    class Config:
        """Pydantic schema config."""

        orm_mode = True

    first_name: str
    last_name: str
    age: int | None = None
    email: str | None = None

    bio: Optional["UserBioSchema"] = Field(
        relationship=RelationshipInfo(
            resource_type="user_bio",
        ),
    )


class UserUpdateSchema(UserBaseSchema):
    """User PATCH schema."""

    first_name: str | None = None
    last_name: str | None = None


# class UserCreateSchema(UserBaseSchema):
#     """User input schema."""


class UserSchema(UserBaseSchema):
    """User item schema."""

    id: int
