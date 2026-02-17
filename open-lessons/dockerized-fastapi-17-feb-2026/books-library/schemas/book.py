from uuid import UUID
from datetime import date

from pydantic import BaseModel, constr

Title = constr(min_length=1, max_length=500)


class BookBase(BaseModel):
    title: str
    pub_date: date


class BookCreate(BookBase):
    """
    Create a new book
    """

    title: Title


class BookRead(BookBase):
    """
    Read a book
    """

    id: UUID


class BookUpdate(BookBase):
    """
    Update a book
    """

    title: Title
