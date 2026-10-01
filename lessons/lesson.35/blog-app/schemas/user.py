from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: str | None
    full_name: str


class UserRead(UserBase):
    id: int


class UserCreate(UserBase):
    """
    User create schema
    """

    email: EmailStr | None = None
    full_name: str = ""
