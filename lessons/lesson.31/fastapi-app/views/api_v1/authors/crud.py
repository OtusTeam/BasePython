"""
Create
Read
Update
Delete
"""

from sqlalchemy import select

from sqlalchemy.orm import Session

from models import Author

from .schemas import (
    AuthorCreateSchema,
)


class AuthorStorage:
    def __init__(
        self,
        session: Session,
    ) -> None:
        self.session = session

    def create(self, author_in: AuthorCreateSchema) -> Author:
        author = Author(
            **author_in.model_dump(),
        )
        self.session.add(author)
        self.session.commit()
        return author

    def get(self) -> list[Author]:
        stmt = select(Author).order_by(Author.id)
        return list(self.session.scalars(stmt).all())

    def get_by_id(self, author_id: int) -> Author | None:
        return self.session.get(Author, author_id)

    def get_by_email(self, email: str) -> Author | None:
        stmt = select(Author).where(Author.email == email)
        # result = self.session.execute(stmt)
        # return result.scalar_one_or_none()
        return self.session.scalar(stmt)
