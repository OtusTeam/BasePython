"""
Async

Create
Read
Update
Delete
"""

import asyncio
import logging
import random

import aiohttp
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from models import Author

from schemas.author import (
    AuthorCreateSchema,
)


log = logging.getLogger(__name__)


class AuthorStorage:
    def __init__(
        self,
        session: AsyncSession,
    ) -> None:
        self.session = session

    async def create(self, author_in: AuthorCreateSchema) -> Author:
        author = Author(
            **author_in.model_dump(),
        )
        self.session.add(author)
        await self.session.commit()
        return author

    async def create_many(self, n_authors: int) -> list[Author]:
        rnd_val = random.randint(100, 999)
        authors = [
            Author(
                **AuthorCreateSchema(
                    name=f"Name-{rnd_val}-{idx}",
                    username=f"author-{rnd_val}-{idx:03d}",
                    email=f"author.{rnd_val}.{idx}@example.com",
                ).model_dump(),
            )
            for idx in range(1, n_authors + 1)
        ]
        self.session.add_all(authors)
        await self.session.commit()
        return authors

    async def get(self) -> list[Author]:
        stmt = select(Author).order_by(Author.id)
        results = await self.session.scalars(stmt)
        return list(results.all())

    async def get_by_id(self, author_id: int) -> Author | None:
        # async with aiohttp.ClientSession() as session:
        #     async with session.post(
        #         "https://dummyjson.com/test",
        #         json={"author_id": author_id},
        #     ) as response:
        #         data: dict = await response.json()
        # await asyncio.sleep(0.3)
        await asyncio.sleep(0.7)
        data = {}
        log.info("got async data response for author %s: %s", author_id, data)

        return await self.session.get(Author, author_id)

    async def get_by_email(self, email: str) -> Author | None:
        stmt = select(Author).where(Author.email == email)
        # result = await self.session.execute(stmt)
        # return result.scalar_one_or_none()
        return await self.session.scalar(stmt)
