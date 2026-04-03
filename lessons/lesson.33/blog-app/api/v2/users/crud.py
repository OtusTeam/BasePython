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
from schemas.user import UserCreate


log = logging.getLogger(__name__)


class Crud:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_users(self) -> list[User]:
        stmt = select(User).order_by(User.id)
        users = await self.session.scalars(stmt)
        return list(users.all())

    async def get_user(self, user_id: int) -> User | None:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=f"http://127.0.0.1:5050/api/{user_id}",
                json={"foo": "bar", "user_id": user_id},
            ) as response:
                result = await response.json()
        log.debug("response: %s", result)
        return await self.session.get(User, user_id)

    async def create_user(self, user_create: UserCreate) -> User:
        user = User(**user_create.model_dump())
        self.session.add(user)
        await self.session.commit()
        # await self.session.refresh(user)
        return user
