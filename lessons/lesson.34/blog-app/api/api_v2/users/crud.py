"""
Async Users CRUD

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
from schemas.user import UserCreateSchema

API_URL = "http://0.0.0.0:8888/reverse-id"

log = logging.getLogger(__name__)


class UsersCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self) -> list[User]:
        stmt = select(User).order_by(User.id)
        return list((await self.session.scalars(stmt)).all())

    @classmethod
    async def fetch_user_info(cls, user_id: int) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.post(API_URL, json={"user_id": user_id}) as response:
                result = await response.json()
        log.debug("Response: %s", result)

    async def get_by_id(self, user_id: int) -> User | None:
        await self.fetch_user_info(user_id)
        return await self.session.get(User, user_id)

    async def create(self, user_create: UserCreateSchema) -> User:
        user = User(**user_create.model_dump())
        self.session.add(user)
        await self.session.commit()
        # await self.session.refresh(user)
        return user
