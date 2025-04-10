"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import UserCreate
from models import User


class UsersCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self) -> list[User]:
        statement = select(User).order_by(User.id)
        result = await self.session.scalars(statement)
        return list(result.all())

    async def get_by_id(self, user_id: int) -> User | None:
        return await self.session.get(User, user_id)

    async def get_by_token(self, token: str) -> User | None:
        statement = select(User).where(User.token == token)
        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def create(self, user_in: UserCreate) -> User:
        user = User(
            **user_in.model_dump(),
        )
        self.session.add(user)
        await self.session.commit()
        return user
