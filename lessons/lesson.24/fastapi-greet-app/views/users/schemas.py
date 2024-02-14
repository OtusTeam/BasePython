from pydantic import BaseModel, EmailStr, Field, ConfigDict

from views.common.schemas import MetadataSchema, LimitOffsetPaginationSchema


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    """
    Create User Schema
    """


class UserOut(UserBase):
    """
    User Out Schema (API representation)
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int = Field(example=123)


class UsersDataOut(BaseModel):
    data: list[UserOut]
    meta: MetadataSchema
