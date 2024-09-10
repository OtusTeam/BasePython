"""
Create
Read
Update
Delete
"""
from random import randint
from typing import Sequence
import logging

import aiohttp
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from schemas.user import (
    UserCreate,
    UserIdType,
)
log = logging.getLogger(__name__)


class UsersAsyncStorage:

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

    async def create_many(
        self,
        n_users: int,
    ) -> list[User]:
        rnd_val = randint(100, 999)
        users = [
            User(username=f"user-{rnd_val}-{idx:03d}")
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
        return (await self.session.scalars(stmt)).all()

    async def get_by_id(self, user_id: UserIdType) -> User | None:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://httpbin.org/get") as response:
                # data = await response.json()
                data = await response.text()
        log.debug("Data: %s", data)
        return await self.session.get(User, user_id)

    async def get_by_token(self, token: str) -> User | None:
        stmt = select(User).where(User.token == token)
        res = await self.session.scalars(stmt)
        user: User | None = res.one_or_none()
        return user
