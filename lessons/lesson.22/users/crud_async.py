"""
C - create
R - read
U - update
D - delete
"""
from typing import Optional

import aiohttp
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession as Session

from models import User
from .schemas import UserIn


async def list_users(session: Session) -> list[User]:
    stmt = select(User)
    stmt = stmt.order_by(User.id)
    result: Result = await session.execute(stmt)
    users: list[User] = result.scalars().all()
    return users


async def create_user(session: Session, user_in: UserIn) -> User:
    user = User(**user_in.dict())
    print("created user", user)

    session.add(user)
    await session.commit()

    return user


async def get_user_by_id(session: Session, user_id: int) -> Optional[User]:
    try:
        async with aiohttp.ClientSession() as client_session:
            async with client_session.get("https://httpbin.org/get") as resp:
                await resp.json()
    except:
        pass

    user = await session.get(User, user_id)
    return user


async def get_user_by_token(session: Session, token: str) -> Optional[User]:
    # stmt = select(User).where(
    stmt = select(User).filter(
        User.token == token,
    )
    result: Result = await session.execute(stmt)
    user: User | None = result.scalar_one_or_none()
    print("found user", user)
    return user
