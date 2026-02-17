from typing import Annotated
from uuid import UUID

from fastapi import Depends, Path, HTTPException, status

from dependencies.session import AsyncSessionDep
from models import Book
from schemas import BookCreate
from .crud import Crud

# TODO: refactor into modules


def crud_provider(
    session: AsyncSessionDep,
) -> Crud:
    return Crud(session)


CrudDep = Annotated[
    Crud,
    Depends(crud_provider),
]


async def get_books_list(
    crud: CrudDep,
) -> list[Book]:
    return await crud.list()


BooksListDep = Annotated[
    list[Book],
    Depends(get_books_list),
]


async def create_book(
    book_create: BookCreate,
    crud: CrudDep,
):
    return await crud.create(
        book_create=book_create,
    )


CreateBookDep = Annotated[
    Book,
    Depends(create_book),
]


async def get_book_by_id(
    book_id: Annotated[UUID, Path()],
    crud: CrudDep,
) -> Book:
    book = await crud.get_by_id(book_id=book_id)
    if book is not None:
        return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book '{book_id}' not found",
    )


GetBookDep = Annotated[
    Book,
    Depends(get_book_by_id),
]
