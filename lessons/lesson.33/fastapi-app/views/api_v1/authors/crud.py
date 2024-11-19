"""
Create
Read
Update
Delete
"""

import logging
import time

import requests
from sqlalchemy import select

from sqlalchemy.orm import Session

from models import Author

from schemas.author import (
    AuthorCreateSchema,
)

log = logging.getLogger(__name__)


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
        # response = requests.post(
        #     "https://dummyjson.com/test",
        #     json={"author_id": author_id},
        # )
        # data = response.json()
        # time.sleep(0.3)
        time.sleep(0.7)
        data = {}
        log.info("got sync data response for author %s: %s", author_id, data)
        return self.session.get(Author, author_id)

    def get_by_email(self, email: str) -> Author | None:
        stmt = select(Author).where(Author.email == email)
        # result = self.session.execute(stmt)
        # return result.scalar_one_or_none()
        return self.session.scalar(stmt)
