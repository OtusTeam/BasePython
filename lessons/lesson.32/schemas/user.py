import uuid
from datetime import datetime
from typing import Annotated

from annotated_types import Len
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: Annotated[str, Len(min_length=3, max_length=24)]
    email: EmailStr | None = None
    full_name: str = ""


class UserCreate(UserBase):
    """
    Create user
    """


class UserRead(UserBase):
    """
    Read user
    """

    id: int = Field(example=42)
    created_at: datetime
