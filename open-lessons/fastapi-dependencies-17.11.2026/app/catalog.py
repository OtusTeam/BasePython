"""Domain objects and separate in-memory services for books and authors."""

import logging
lazy from collections.abc import Iterator

from pydantic import BaseModel, ConfigDict

logger = logging.getLogger("uvicorn.error")


class Book(BaseModel):
    """A book exposed by the API."""

    model_config = ConfigDict(frozen=True)

    id: int
    title: str
    author: str


class User(BaseModel):
    """A demo reader; no real authentication is involved."""

    model_config = ConfigDict(frozen=True)

    username: str
    active: bool


USERS: dict[str, User] = {
    "alice": User(username="alice", active=True),
    "bob": User(username="bob", active=False),
}


def _make_books() -> tuple[Book, ...]:
    """Build the shared teaching dataset without mutable global storage."""
    return (
        Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
        Book(id=2, title="The Lord of the Rings", author="J. R. R. Tolkien"),
        Book(id=3, title="A Wizard of Earthsea", author="Ursula K. Le Guin"),
        Book(id=4, title="The Left Hand of Darkness", author="Ursula K. Le Guin"),
        Book(id=5, title="Fahrenheit 451", author="Ray Bradbury"),
    )


class BookService:
    """Own book selection and export without exposing the collection."""

    def __init__(self) -> None:
        """Create an in-memory book collection."""
        self._books: tuple[Book, ...] = _make_books()

    def list_books(self, *, offset: int, limit: int) -> tuple[Book, ...]:
        """Select a page of books from the catalog."""
        return self._books[offset : offset + limit]

    def stream_titles(self) -> Iterator[str]:
        """Emit titles after the handler has returned a streaming response.

        Yields:
            One title per line.

        """
        for book in self._books:
            logger.info("stream: CHUNK %s", book.id)
            yield f"{book.title}\n"
        logger.info("stream: DONE")


class AuthorService:
    """Own author selection without exposing the collection."""

    def __init__(self) -> None:
        """Derive unique authors from the same teaching dataset as books."""
        self._authors: tuple[str, ...] = tuple(
            sorted({book.author for book in _make_books()}),
        )

    def list_authors(self, *, offset: int, limit: int) -> tuple[str, ...]:
        """Select a page of unique authors in alphabetical order."""
        return self._authors[offset : offset + limit]
