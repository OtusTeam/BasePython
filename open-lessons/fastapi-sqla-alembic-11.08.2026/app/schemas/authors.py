import re
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr
from pydantic import StringConstraints

from app.schemas.books import BookRead

AuthorName = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=1,
        max_length=120,
        pattern=re.compile(r"^[^\x00\ud800-\udfff]+$"),
    ),
]


class AuthorCreate(BaseModel):
    name: AuthorName
    email: EmailStr | None = None


class AuthorRead(AuthorCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime


class AuthorWithBooks(AuthorRead):
    books: list[BookRead]
