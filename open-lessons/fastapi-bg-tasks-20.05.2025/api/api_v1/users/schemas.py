from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, EmailStr
from annotated_types import Len


class UserBase(BaseModel):
    # noinspection PyTypeHints
    username: Annotated[
        str,
        Len(min_length=3, max_length=20),
    ]
    email: EmailStr
    full_name: str = ""


class UserCreate(UserBase):
    """
    Create user
    """

    # noinspection PyTypeHints
    password: Annotated[
        str,
        Len(min_length=8, max_length=1000),
    ]


class UserRead(UserBase):
    id: UUID
