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

from models import User
from schemas import UserCreate


log = logging.getLogger(__name__)


class Crud:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_users(self) -> list[User]:
        statement = select(User).order_by(User.id)
        users = await self.session.scalars(statement)
        return list(users.all())

    async def get_user(self, user_id: int) -> User | None:
        async with aiohttp.ClientSession() as session:
            async with session.post(f"http://localhost:5050/api/{user_id}") as response:
                data = await response.json()
        log.debug("data: %s", data)
        return await self.session.get(User, user_id)

    async def create_user(
        self,
        user_create: UserCreate,
    ) -> User:
        user = User(
            **user_create.model_dump(),
        )
        self.session.add(user)
        await self.session.commit()
        # await self.session.refresh(user)
        return user
