import aiohttp
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import User
from views.api.schemas import UserCreateSchema


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result_scalars = await session.scalars(stmt)
    return list(result_scalars.all())


async def get_user_by_id(
    session: AsyncSession,
    user_id: int,
) -> User | None:
    """
    From cache

    :param session:
    :param user_id:
    :return:
    """
    async with aiohttp.ClientSession() as client_session:
        async with client_session.get(f"https://example.com/users/{user_id}") as response:
            await response.text()

    user = await session.get(User, user_id)
    return user


async def create_user(
    session: AsyncSession,
    user_create: UserCreateSchema,
) -> User:
    user = User(**user_create.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh()
    return user


async def create_many_users(
    session: AsyncSession,
    n_users: int,
) -> list[User]:
    users = [
        User(username=f"user_{n_users}_{i:04}")
        for i in range(1, n_users + 1)
    ]
    session.add_all(users)
    await session.commit()
    return users
