import re
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import StringConstraints

BookTitle = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=1,
        max_length=200,
        pattern=re.compile(r"^[^\x00\ud800-\udfff]+$"),
    ),
]


class BookCreate(BaseModel):
    title: BookTitle


class BookRead(BookCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    author_id: int
    created_at: datetime
