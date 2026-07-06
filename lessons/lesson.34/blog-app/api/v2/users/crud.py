import logging

import aiohttp
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User

log = logging.getLogger(__name__)


class Crud:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_users(self) -> list[User]:
        stmt = select(User).order_by(User.id)
        users = await self.session.scalars(stmt)
        return list(users.all())

    async def get_user(self, user_id: int) -> User | None:
        async with aiohttp.ClientSession() as client:
            async with client.post(
                f"http://localhost:5050/api/{user_id}",
                json={"user_id": user_id},
            ) as response:
                response_data = await response.json()
        log.info("[v2] user response data: %s", response_data)
        return await self.session.get(User, user_id)
