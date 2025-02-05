"""
Create
Read
Update
Delete
"""

import logging

import aiohttp
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.author import AuthorCreate
from models import Author

log = logging.getLogger(__name__)


class AuthorsStorage:
    def __init__(
        self,
        session: AsyncSession,
    ):
        self.session = session

    async def create(self, author_in: AuthorCreate) -> Author:
        author = Author(
            **author_in.model_dump(),
        )
        self.session.add(author)
        await self.session.commit()
        return author

    async def create_many(
        self,
        n_authors: int,
    ) -> list[Author]:
        authors = [
            Author(
                name=f"Author {idx:03d} of {n_authors}",
                email=f"author.{idx:03d}.{n_authors}.mail@example.com",
            )
            for idx in range(1, n_authors + 1)
        ]
        self.session.add_all(authors)
        await self.session.commit()
        return authors

    async def get(self) -> list[Author]:
        statement = select(Author).order_by(Author.id)
        return list(await self.session.scalars(statement))

    async def get_by_id(self, author_id: int) -> Author | None:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://localhost:3000/get-data") as response:
                json_data = await response.json()
        log.info("Data: %s", json_data)
        return await self.session.get(Author, author_id)
