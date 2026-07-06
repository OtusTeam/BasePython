from pydantic import BaseModel


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

    email: str | None = None
    full_name: str = ""
