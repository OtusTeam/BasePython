from typing import Annotated
from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import StringConstraints


class BookCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=100)]
    pages: Annotated[int, Field(strict=True, gt=0, le=10_000)]


class BookOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    pages: int
    is_read: bool
