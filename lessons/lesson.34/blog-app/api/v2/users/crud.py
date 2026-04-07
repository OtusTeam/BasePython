"""
Create
Read
Update
Delete
"""

import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from schemas.user import UserCreate


class Crud:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_users(self) -> list[User]:
        stmt = select(User).order_by(User.id)
        users = await self.session.scalars(stmt)
        return list(users.all())

    async def get_user(self, user_id: int) -> User | None:
        return await self.session.get(User, user_id)

    async def create_user(self, user_create: UserCreate) -> User:
        user = User(**user_create.model_dump())
        self.session.add(user)
        await self.session.commit()
        return user
