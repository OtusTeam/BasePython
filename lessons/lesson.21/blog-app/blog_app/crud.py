import asyncio
from datetime import datetime
from time import sleep
from typing import Optional, Dict, Sequence, List

import requests
from aiohttp import ClientSession
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from blog_app.schemas import UserIn
from core.models import User


USERS_BY_ID: Dict[int, User] = {}
USERS_BY_TOKEN: Dict[str, User] = {}


async def create_user(user_in: UserIn, db_session: AsyncSession) -> User:
    user = User(username=user_in.username)
    async with db_session.begin():
        db_session.add(user)
    return user


async def create_many_users(users_to_create: int, db_session: AsyncSession) -> List[User]:
    rnd_elem = datetime.now().microsecond
    users = [
        User(username=f"user_{rnd_elem}_{i:03}")
        for i in range(1, users_to_create + 1)
    ]
    async with db_session.begin():
        db_session.add_all(users)
    return users


async def get_users(db_session: AsyncSession) -> Sequence[User]:
    # async with ClientSession() as session:
    #     async with session.get("https://httpbin.org/get") as response:
    #         json_result = await response.json()

    # sleep(0.1)
    await asyncio.sleep(1)

    stmt = select(User)
    result = await db_session.execute(stmt)
    return result.scalars()


def get_users_sync(session) -> List[User]:
    # response = requests.get("https://httpbin.org/get")
    # json_result = response.json()
    sleep(1)

    users = session.query(User).all()
    return users


async def get_user(user_id: int, db_session: AsyncSession) -> Optional[User]:
    stmt = select(User).where(User.id == user_id)
    result = await db_session.execute(stmt)
    return result.scalar_one_or_none()


async def get_user_by_token(token: str, db_session: AsyncSession) -> Optional[User]:
    stmt = select(User).where(User.auth_token == token)
    result = await db_session.execute(stmt)
    return result.scalar_one_or_none()
