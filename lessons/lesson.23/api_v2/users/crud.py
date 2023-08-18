"""
Create
Read
Update
Delete
"""
from sqlalchemy import select
from sqlalchemy.engine import Result

from models import User
from models.db_async import AsyncScopedSession
from .schemas import UserIn


async def get_users() -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await AsyncScopedSession.execute(stmt)
    return result.scalars().all()


async def create_user(user_in: UserIn) -> User:
    user = User(**user_in.model_dump())
    AsyncScopedSession.add(user)
    await AsyncScopedSession.commit()
    return user


async def get_user_by_id(user_id: int) -> User | None:
    return await AsyncScopedSession.get(User, user_id)


async def get_user_by_token(token: str) -> User | None:
    stmt = select(User).where(User.token == token)
    result: Result = await AsyncScopedSession.execute(stmt)
    return result.scalar_one_or_none()
