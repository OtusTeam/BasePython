"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from schemas.author import AuthorCreate
from models import Author


class AuthorsStorage:
    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    def create(self, author_in: AuthorCreate) -> Author:
        author = Author(
            **author_in.model_dump(),
        )
        self.session.add(author)
        self.session.commit()
        return author

    def get(self) -> list[Author]:
        statement = select(Author).order_by(Author.id)
        return list(self.session.scalars(statement))

    def get_by_id(self, author_id: int) -> Author | None:
        return self.session.get(Author, author_id)
