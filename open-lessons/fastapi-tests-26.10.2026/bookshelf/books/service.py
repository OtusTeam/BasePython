from typing import TYPE_CHECKING

from sqlalchemy import select
from starlette import status

from bookshelf.books.models import Book
from bookshelf.core.errors import DomainError


if TYPE_CHECKING:
    from uuid import UUID

    from sqlalchemy.orm import Session

    from bookshelf.books.schemas import BookCreate
    from bookshelf.config.books import BookConfig


def list_books(session: Session) -> list[Book]:
    return list(session.scalars(select(Book).order_by(Book.created_at, Book.id)))


def create_book(session: Session, data: BookCreate, config: BookConfig) -> Book:
    if not config.allow_create:
        raise DomainError(status.HTTP_503_SERVICE_UNAVAILABLE, "Adding books is disabled")
    book = Book(title=data.title, pages=data.pages)
    session.add(book)
    session.flush()
    return book


def mark_read(session: Session, book_id: UUID) -> Book:
    book = session.get(Book, book_id)
    if book is None:
        raise DomainError(status.HTTP_404_NOT_FOUND, "Book not found")
    book.is_read = True
    session.flush()
    return book
