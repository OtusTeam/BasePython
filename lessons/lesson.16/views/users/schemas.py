from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    """
    Create new user with username and email
    """


class UserOut(UserBase):
    id: int = Field(
        ...,
        description="User ID assigned in DB automatically",
        example=123,
    )


class User(UserBase):
    id: int
