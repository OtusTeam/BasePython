from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, selectinload

from app.exceptions import AuthorAlreadyExistsError, AuthorNotFoundError
from app.models.author import Author


class AuthorRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def add(self, author: Author) -> None:
        self.session.add(author)
        try:
            self.session.flush()
        except IntegrityError as exc:
            raise AuthorAlreadyExistsError(author.name) from exc

    def list(self, *, offset: int, limit: int) -> Sequence[Author]:
        statement = (
            select(Author)
            .options(
                selectinload(Author.books),
            )
            .order_by(Author.id)
            .limit(limit)
            .offset(offset)
        )
        return self.session.scalars(statement).all()

    def get(self, author_id: int) -> Author:
        author = self.session.get(Author, author_id)
        if author is not None:
            return author
        raise AuthorNotFoundError(author_id)

    def get_with_books(self, author_id: int) -> Author:
        statement = (
            select(Author)
            .options(
                selectinload(Author.books),
            )
            .where(
                Author.id == author_id,
            )
        )
        author = self.session.scalar(statement)
        if author is not None:
            return author
        raise AuthorNotFoundError(author_id)
