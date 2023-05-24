from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from .schemas import UserIn


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User)
    result: Result = await session.execute(stmt)
    return result.scalars().all()


async def create_user(session: AsyncSession, user_in: UserIn) -> User:
    user = User(**user_in.dict())
    session.add(user)
    await session.commit()
    # await session.refresh(user)
    return user


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def get_user_by_token(session: AsyncSession, token: str) -> User | None:
    stmt = select(User).where(User.token == token)
    result: Result = await session.execute(stmt)
    return result.scalar_one_or_none()
