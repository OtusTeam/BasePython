from datetime import datetime
from typing import Annotated

from annotated_types import Len
from pydantic import BaseModel, EmailStr, Field
import random
import string


def new_friend_code():
    return "".join(random.choices(string.ascii_letters, k=8))


class UserBaseSchema(BaseModel):

    username: Annotated[str, Len(max_length=32)]
    email: Annotated[EmailStr | None, Len(max_length=150)]
    full_name: str = ""
    friend_code: Annotated[
        str,
        Len(max_length=20),
        Field(
            default_factory=new_friend_code,
        ),
    ]


class UserCreateSchema(UserBaseSchema):
    """
    Create new user
    """


class UserReadSchema(UserBaseSchema):
    id: int
    created_at: datetime
    status: str | None = None
