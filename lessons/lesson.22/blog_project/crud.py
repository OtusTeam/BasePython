# Create
# Read
# Update
# Delete
import asyncio
from time import sleep
from typing import Optional
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session as SessionType
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine.result import Result

from blog_project.models import User
from .schemas import UserIn


def create_user(session: SessionType, user_in: UserIn) -> User:
    user = User(**user_in.dict())
    session.add(user)
    session.commit()
    return user


def list_users(session: SessionType) -> list[User]:
    # response = requests.get("https://httpbin.org")
    # response.json()
    sleep(1.5)
    return session.query(User).order_by(User.id).all()
    # return session.query(User).order_by(User.id).limit(10).all()


async def list_users_async(async_session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await async_session.execute(stmt)
    users: list[User] = list(result.scalars())

    # async with ClientSession() as session:
    #     async with session.get("https://httpbin.org") as response:
    #         await response.json()

    await asyncio.sleep(1.5)

    return users


async def create_many_users(async_session: AsyncSession, users_count: int) -> list[User]:

    rnd_elem = datetime.now().microsecond
    users = [
        User(username=f"user_{rnd_elem}_{i:03}")
        for i in range(1, users_count + 1)
    ]
    async with async_session.begin():
        async_session.add_all(users)

    return users


async def get_user_by_id(async_session: AsyncSession, user_id: int) -> Optional[User]:
    return await async_session.get(User, user_id)
