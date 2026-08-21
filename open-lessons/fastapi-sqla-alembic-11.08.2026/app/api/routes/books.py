from collections.abc import Sequence

from fastapi import APIRouter
from fastapi import status

from app.api.params import Limit
from app.api.params import Offset
from app.api.params import PrimaryKey
from app.dependencies import CatalogServiceDependency
from app.models.book import Book
from app.schemas.books import BookCreate
from app.schemas.books import BookRead

router = APIRouter(tags=["books"])


@router.post(
    "/authors/{author_id}/books",
    response_model=BookRead,
    status_code=status.HTTP_201_CREATED,
)
def create_book(
    author_id: PrimaryKey,
    payload: BookCreate,
    service: CatalogServiceDependency,
) -> Book:
    return service.create_book(author_id, payload)


@router.get("/books", response_model=list[BookRead])
def list_books(
    service: CatalogServiceDependency,
    offset: Offset = 0,
    limit: Limit = 20,
) -> Sequence[Book]:
    return service.list_books(offset=offset, limit=limit)


@router.get("/books/{book_id}", response_model=BookRead)
def get_book(
    book_id: PrimaryKey,
    service: CatalogServiceDependency,
) -> Book:
    return service.get_book(book_id)
