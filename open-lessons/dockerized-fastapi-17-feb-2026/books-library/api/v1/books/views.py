from fastapi import APIRouter, status

from models import Book
from schemas import BookRead

from .dependencies import BooksListDep, CreateBookDep, GetBookDep

router = APIRouter(
    prefix="/books",
    tags=["books"],
)


@router.post(
    "/",
    response_model=BookRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_book(
    created_book: CreateBookDep,
) -> Book:
    return created_book


@router.get(
    "/",
    response_model=list[BookRead],
)
async def get_books(
    books: BooksListDep,
) -> list[Book]:
    return books


@router.get(
    "/{book_id}/",
    response_model=BookRead,
)
def get_book(
    book: GetBookDep,
) -> Book:
    return book
