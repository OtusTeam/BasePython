"""
Create
Read
Update
Delete
"""

import logging
import secrets

import aiohttp
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from schemas.user import UserCreateSchema

log = logging.getLogger(__name__)


class UsersCRUD:

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_list(self) -> list[User]:
        statement = select(User).order_by(User.id)
        result = await self.session.scalars(statement)
        return list(result.all())

    async def get_by_id(self, user_id: int) -> User | None:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"http://0.0.0.0:5050/api/users/{user_id}/"
            ) as response:
                user_data = await response.json()
        log.debug("User data: %s", user_data)
        return await self.session.get(User, user_id)

    async def create(self, user_in: UserCreateSchema) -> User:
        user = User(**user_in.model_dump())
        self.session.add(user)
        await self.session.commit()
        # await self.session.refresh(user)
        return user

    async def create_many(self, n_users: int) -> list[User]:
        random_seed = secrets.token_urlsafe(6)
        random_domain = secrets.token_urlsafe(8)
        users = [
            User(
                username=f"user-{idx:03d}-{random_seed}",
                email=f"{random_seed}.{idx:03d}@{random_domain}.com",
                full_name=f"{secrets.token_urlsafe(8)} {secrets.token_urlsafe(8)}",
            )
            for idx in range(1, n_users + 1)
        ]

        self.session.add_all(users)
        await self.session.commit()
        return users
