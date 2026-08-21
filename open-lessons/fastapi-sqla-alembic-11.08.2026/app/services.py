from collections.abc import Sequence

from sqlalchemy.orm import Session

from app.models import Author
from app.models import Book
from app.repositories.authors import AuthorRepository
from app.repositories.books import BookRepository
from app.schemas.authors import AuthorCreate
from app.schemas.books import BookCreate


class CatalogService:
    def __init__(self, session: Session) -> None:
        self.session = session
        self.authors = AuthorRepository(session)
        self.books = BookRepository(session)

    def create_author(self, data: AuthorCreate) -> Author:
        author = Author(**data.model_dump())
        self.authors.add(author)
        self.session.commit()
        return author

    def list_authors(self, *, offset: int, limit: int) -> Sequence[Author]:
        return self.authors.list(offset=offset, limit=limit)

    def get_author(self, author_id: int) -> Author:
        return self.authors.get_with_books(author_id)

    def create_book(self, author_id: int, data: BookCreate) -> Book:
        book = Book(title=data.title, author_id=author_id)
        self.authors.get(author_id)
        self.books.add(book)
        self.session.commit()
        return book

    def list_books(self, *, offset: int, limit: int) -> Sequence[Book]:
        return self.books.list(offset=offset, limit=limit)

    def get_book(self, book_id: int) -> Book:
        return self.books.get(book_id)
