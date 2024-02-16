"""
Async CRUD

Create
Read
Update
Delete
"""
from sqlalchemy import select, func, text

from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from schemas.user import UserCreate


async def create_user(
    session: AsyncSession,
    user_in: UserCreate,
) -> User:
    user: User = User(
        **user_in.model_dump(),
    )
    session.add(user)
    await session.commit()
    return user


async def create_many_users(
    session: AsyncSession,
    n_users: int,
) -> list[User]:
    users = [
        # create new user
        User(username=f"user_{n_users:04}_{i:04}")
        # for each username
        for i in range(1, n_users + 1)
    ]
    session.add_all(users)
    await session.commit()
    return users


async def get_users(
    session: AsyncSession,
    limit: int | None = None,
    offset: int | None = None,
) -> list[User]:
    stmt = select(User).order_by(User.id)
    if limit is not None:
        stmt = stmt.limit(limit)
    if offset is not None:
        stmt = stmt.offset(offset)
    return list((await session.scalars(stmt)).all())


async def get_users_count(
    session: AsyncSession,
    stmt=None,
) -> int:
    if stmt is None:
        stmt = select(User.id)

    stmt = select(
        func.count(
            text("*"),
        ),
    ).select_from(
        stmt.subquery(),
    )
    return await session.scalar(stmt)


async def get_user(
    session: AsyncSession,
    user_id: int,
) -> User | None:
    return await session.get(User, user_id)


async def get_user_by_token(
    session: AsyncSession,
    token: str,
) -> User | None:
    stmt = select(User).where(User.token == token)
    return await session.scalar(stmt)
