"""
Create
Read
Update
Delete
"""
import asyncio
import logging
from typing import Sequence

import aiohttp
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from schemas.user import (
    UserCreate,
    UserIdType,
)

log = logging.getLogger(__name__)


class UsersStorage:

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(
        self,
        user_in: UserCreate,
    ) -> User:
        user = User(
            **user_in.model_dump(),
        )
        self.session.add(user)
        await self.session.commit()
        return user

    async def create_many_users(
        self,
        n_users: int,
    ) -> Sequence[User]:
        users = [
            User(
                username=f"user_{idx:04d}_{n_users:04d}",
            )
            for idx in range(1, n_users + 1)
        ]
        self.session.add_all(users)
        await self.session.commit()
        return users

    async def get(self) -> Sequence[User]:
        stmt = (
            # users
            select(User)
            # order by!
            .order_by(User.id)
        )
        users = await self.session.scalars(stmt)
        return users.all()

    async def get_by_id(self, user_id: UserIdType) -> User | None:
        await asyncio.sleep(0.5)
        # async with aiohttp.ClientSession() as session:
        #     async with session.get("https://example.org/") as response:
        #         log.info("Result posts: %s", await response.text())
        return await self.session.get(User, user_id)

    async def get_by_token(self, token: str) -> User | None:
        stmt = select(User).where(User.token == token)
        res = await self.session.scalars(stmt)
        user: User | None = res.one_or_none()
        return user
