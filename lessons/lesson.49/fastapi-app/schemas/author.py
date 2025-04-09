from typing import Annotated

from pydantic import BaseModel, EmailStr
from annotated_types import MaxLen


class AuthorBase(BaseModel):
    name: Annotated[str, MaxLen(200)]
    email: EmailStr | None = None
    bio: str = ""


class AuthorRead(AuthorBase):
    """
    Reads author
    """

    id: int
    ref_code: str


class AuthorCreate(AuthorBase):
    """
    Creates author
    """
