import asyncio
from datetime import datetime
from time import sleep
from typing import Optional, Sequence

import requests
from aiohttp import ClientSession
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from blog_app.models import User
from blog_app.schemas import UserIn


async def create_user(session: AsyncSession, user_in: UserIn) -> User:
    user = User(**user_in.dict())
    async with session.begin():
        session.add(user)

    await session.refresh(user)
    return user


async def create_users(session: AsyncSession, count: int) -> list[User]:
    rnd_elem = datetime.now().microsecond

    users = [
        User(username=f"user_{rnd_elem}_{i:03}")
        for i in range(1, count + 1)
    ]
    async with session.begin():
        session.add_all(users)

    # await session.refresh(user)
    return users


def list_users_sync(session: Session) -> list[User]:
    response = requests.get("http://httpbin.org/get")
    response.json()
    sleep(2)
    users = session.query(User).order_by(User.id).all()
    return users


async def list_users(session: AsyncSession) -> Sequence[User]:
    async with ClientSession() as client_session:
        response = await client_session.get("http://httpbin.org/get")
        await response.json()
    await asyncio.sleep(2)
    stmt = select(User).order_by(User.id)
    result = await session.execute(stmt)
    return result.scalars()


async def get_user_by_token(session: AsyncSession, token: str) -> Optional[User]:
    stmt = select(User).where(User.access_token == token)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()
