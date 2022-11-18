import asyncio
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

from models import User, Author, Post
from models.base import Base

import config

async_engine: AsyncEngine = create_async_engine(
    url=config.DB_ASYNC_URL,
    echo=config.DB_ECHO,
)

async_session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    # expire_on_commit=True,
)


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    session.add(user)
    print("user create", user)

    await session.commit()
    print("user saved", user)

    # not required!!!!
    await session.refresh(user)
    print("user refreshed", user)

    return user


async def get_all_users(session: AsyncSession) -> list[User]:
    stmt = select(User)
    # stmt = stmt.order_by(User.id)
    result_users: Result = await session.execute(stmt)
    users = result_users.scalars().all()
    # users = result_users.all()

    print("users", users)
    return users


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    user: User | None = await session.get(User, user_id)

    print("user", user)
    return user


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    # stmt = select(User).filter(User.username == username)
    stmt = select(User).where(User.username == username)
    # result = await session.execute(stmt)
    result: Result = await session.execute(stmt)
    user: User | None = result.scalar_one_or_none()

    print("user", user)
    return user


async def get_users_by_username_match(session: AsyncSession, username_part: str) -> list[User]:
    # stmt = select(User).filter(User.username == username)
    stmt = select(User).where(User.username.ilike(f"%{username_part}%"))
    # result = await session.execute(stmt)
    result: Result = await session.execute(stmt)
    users: list[User] = result.scalars().all()

    print("users", users)
    return users


async def create_author(
    session: AsyncSession,
    user: User,
    name: str
) -> Author:
    author = Author(name=name, user=user)
    session.add(author)
    print("author create", author)

    await session.commit()
    # Сработает если обращение только к тем полям,
    # где есть значение по умолчанию.
    # Иначе выполнится неудачное обращение к БД.
    print("author saved", author)

    # ... !!!!
    await session.refresh(author)
    print("author refreshed", author)

    return author


async def get_author_by_user_username(
    session: AsyncSession,
    username: str,
) -> Author | None:
    stmt_authors = select(Author)
    stmt_authors_w_users = stmt_authors.join(Author.user)
    stmt_author = stmt_authors_w_users.where(User.username == username)
    result: Result = await session.execute(stmt_author)
    author: Author | None = result.scalar_one_or_none()

    print("author", author)
    return author


async def create_posts_for_author(
    session: AsyncSession,
    author: Author,
    *posts_titles: str,
) -> list[Post]:
    # posts = []
    # for post_title in posts_titles:
    #     post = Post(title=post_title, author=author)
    #     posts.append(post)
    #     session.add(post)
    posts = [
        Post(title=post_title, author=author)
        for post_title in posts_titles
    ]
    session.add_all(posts)
    # for post in posts:
    #     session.add(post)
    print("posts to create:", posts)

    await session.commit()
    print("created posts", posts)

    return posts


async def main():
    # await asyncio.gather(asyncio.sleep(1), create_tables())
    # await create_tables()

    async with async_session() as session:
        await create_user(session, "john")
        await create_user(session, "sam")
        await create_user(session, "nick")
        kate = await create_user(session, "kate")
        await create_author(session, user=kate, name="Kate W.")
        jane = await create_user(session, "jane")
        await create_author(session, user=jane, name="Jane Q.")
        bob = await create_user(session, "bob")
        await create_author(session, user=bob, name="Bob A.")
        await get_all_users(session)
        await get_user_by_id(session, 1)
        await get_user_by_id(session, 2)
        await get_user_by_id(session, 100)
        await get_user_by_username(session, "john")
        await get_user_by_username(session, "samuel")
        bob = await get_author_by_user_username(session, "bob")
        await get_author_by_user_username(session, "john")
        await create_posts_for_author(session, bob, "Python", "SQLAlchemy", "Postgres")
        await get_users_by_username_match(session, "j")
        await get_users_by_username_match(session, "o")


if __name__ == '__main__':
    asyncio.run(main())
