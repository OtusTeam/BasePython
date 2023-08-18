"""
Create
Read
Update
Delete
"""
import asyncio

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from .schemas import UserIn


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    return result.scalars().all()


async def create_user(session: AsyncSession, user_in: UserIn) -> User:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user


async def create_many_users(
    session: AsyncSession,
    n_users: int,
) -> list[User]:
    users = [
        User(username=f"user_{n_users}_{i:03}")
        for i in range(1, n_users + 1)
    ]
    session.add_all(users)
    await session.commit()
    return users


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


create_user_lock = asyncio.Lock()


async def get_or_create_user_by_username(
    session: AsyncSession,
    username: str,
) -> User:
    async with create_user_lock:
        stmt = select(User).where(User.username == username)
        result: Result = await session.execute(stmt)
        user = result.scalar_one_or_none()
        if user:
            return user

        user = User(username=username)
        session.add(user)
        await session.commit()
        return user


async def get_user_by_token(session: AsyncSession, token: str) -> User | None:
    stmt = select(User).where(User.token == token)
    result: Result = await session.execute(stmt)
    return result.scalar_one_or_none()
