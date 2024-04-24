from pydantic import (
    BaseModel,
    EmailStr,
    Field,
)


class UserBase(BaseModel):
    username: str
    email: EmailStr | None = None
    bio: str | None = None


class UserCreate(UserBase):
    """
    Create new user
    """


class UserUpdate(UserBase):
    """
    Update user
    """
    username: str | None = None
    email: EmailStr | None = None
    bio: str | None = None


class UserOut(UserBase):
    id: int = Field(
        ...,
        description="User ID assigned in DB automatically",
        example=123,
    )
