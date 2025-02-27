from typing import Annotated

from annotated_types import Len, Ge, Le
from pydantic import BaseModel, Field



class MovieBase(BaseModel):
    title: str
    year: int


class MovieCreate(MovieBase):
    title: Annotated[
        str,
        Len(min_length=1, max_length=200),
    ]
    year: Annotated[
        int,
        Ge(1878),
        Le(2222),
    ]


class MovieRead(MovieBase):
    id: int = Field(example=42)


class Movie(MovieBase):
    """
    The Movie model
    """
    id: int
