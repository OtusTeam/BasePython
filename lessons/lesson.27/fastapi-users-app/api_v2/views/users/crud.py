"""
CRUD functions for users

Create
Read
Update
Delete
"""
import logging

import aiohttp
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from schemas.user import UserCreate, UserUpdate


log = logging.getLogger(__name__)


class UsersStorage:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_user(self, user_in: UserCreate) -> User:
        user = User(**user_in.model_dump())
        self.session.add(user)
        await self.session.commit()
        return user

    async def create_many_users(self, n_users: int) -> list[User]:
        users = [
            User(username=f"user_{i:04d}_{n_users:04d}")
            for i in range(1, n_users + 1)
        ]
        self.session.add_all(users)
        await self.session.commit()
        return users

    async def get_users(self) -> list[User]:
        result = await self.session.scalars(select(User))
        return list(result.all())

    async def get_user(self, user_id: int) -> User | None:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://pie.dev/get") as resp:
                log.info("response (async): %s", await resp.json())
        return await self.session.get(User, user_id)

    async def get_user_by_token(self, token: str) -> User | None:
        stmt = select(User).where(User.token == token)
        return await self.session.scalar(stmt)

    async def delete_user(self, user: User) -> None:
        await self.session.delete(user)
        await self.session.commit()

    async def update_user(self, user: User, user_in: UserUpdate):
        for name, value in user_in.model_dump(exclude_unset=True).items():
            setattr(user, name, value)
        await self.session.commit()
        return user
