import logging
import random

import aiohttp
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from schemas.user import UserCreateSchema


log = logging.getLogger(__name__)


class UsersCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_list(self) -> list[User]:
        statement = select(User).order_by(User.id)
        result = await self.session.scalars(statement)
        return list(result.all())

    async def get_by_id(self, user_id: int) -> User | None:
        url = f"http://localhost:5050/users/{user_id}"
        async with (
            aiohttp.ClientSession() as session,
            session.get(url) as response,
        ):
            response_data = await response.json()

        log.info("response data: %s", response_data)

        return await self.session.get(User, user_id)

    async def create(self, user_create: UserCreateSchema) -> User:
        user = User(**user_create.model_dump())
        self.session.add(user)
        await self.session.commit()
        # self.session.refresh(user)
        return user

    async def create_many(self, n_users: int) -> list[User]:
        rnd_part = int(random.random() * 1000)
        users = [
            User(
                username=f"user-{idx:03d}-{rnd_part}",
                email=f"email-{idx:04d}-{rnd_part}@example.com",
            )
            for idx in range(1, n_users + 1)
        ]
        self.session.add_all(users)
        await self.session.commit()
        return users
