"""
Create
Read
Update
Delete
"""
from time import time

from sqlalchemy import select, delete

from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from schemas.user import UserIn


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    return result.scalars().all()


async def create_user(session: AsyncSession, user_in: UserIn) -> User:
    user = User(**user_in.dict())
    session.add(user)
    await session.commit()
    print("new user", user)
    return user


async def get_user(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def get_user_by_token(session: AsyncSession, token: str) -> User | None:
    stmt = select(User).where(User.token == token)
    result: Result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def delete_user(session: AsyncSession, user_id: int) -> None:
    await session.execute(delete(User).where(User.id == user_id))
    await session.commit()


async def create_many_users(session: AsyncSession, count: int) -> list[User]:
    # 123456789 -> 789
    current_time = int(time()) % 1000
    users = [User(username=f"user_{current_time}_{i:03d}") for i in range(count)]
    session.add_all(users)
    await session.commit()
    return users
