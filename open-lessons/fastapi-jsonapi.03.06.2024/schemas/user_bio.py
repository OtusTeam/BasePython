from typing import TYPE_CHECKING

from fastapi_jsonapi.schema_base import BaseModel, Field, RelationshipInfo

if TYPE_CHECKING:
    from .user import UserSchema


class UserBioBaseSchema(BaseModel):
    """UserBio base schema."""

    class Config:
        """Pydantic schema config."""

        orm_mode = True

    birth_city: str
    favourite_movies: str

    user: "UserSchema" = Field(
        relationship=RelationshipInfo(
            resource_type="user",
        ),
    )


class UserBioUpdateSchema(UserBioBaseSchema):
    """UserBio PATCH schema."""

    birth_city: str | None = None
    favourite_movies: str | None = None

# class UserBioInSchema(UserBioBaseSchema):
#     """UserBio input schema."""


class UserBioSchema(UserBioBaseSchema):
    """UserBio item schema."""

    class Config:
        """Pydantic model config."""

        orm_mode = True

    id: int
