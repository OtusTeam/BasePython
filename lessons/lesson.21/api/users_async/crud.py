"""
Create
Read
Update
Delete
"""
from time import time

import aiohttp
from sqlalchemy import select, delete
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from api.schemas.user import UserIn


# Get
async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User)
    stmt = stmt.order_by(User.id)
    result_users: Result = await session.execute(stmt)
    users = result_users.scalars().all()

    return users


# Get (details)
async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    async with aiohttp.ClientSession() as req_session:
        async with req_session.get("https://httpbin.org/get") as response:
            data = await response.json()

    user: User | None = await session.get(User, user_id)
    return user


async def get_user_by_token(session: AsyncSession, token: str) -> User | None:
    stmt = select(User).where(User.token == token)
    result: Result = await session.execute(stmt)
    user: User | None = result.scalar_one_or_none()

    return user


# CREATE
async def create_user(session: AsyncSession, user_in: UserIn) -> User:
    user = User(**user_in.dict())
    session.add(user)
    await session.commit()

    # await session.refresh(user)
    return user


async def create_many_users(session: AsyncSession, count: int) -> list[User]:
    current_time = int(time()) % 1000
    users = [
        User(username=f"user_{current_time}_{i:03d}")
        for i in range(1, count + 1)
    ]
    session.add_all(users)
    await session.commit()
    return users


# Delete
async def delete_user(session: AsyncSession, user_id: int) -> None:
    stmt = delete(User).where(User.id == user_id)
    await session.execute(stmt)
    await session.commit()
