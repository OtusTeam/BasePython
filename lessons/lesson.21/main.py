import asyncio
from typing import Iterable

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import sessionmaker, joinedload, selectinload, noload
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine

import config
from models import Base, User, Author, Post, Tag

async_engine: AsyncEngine = create_async_engine(
    config.DB_ASYNC_URL,
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
        print("todo: drop all")
        await conn.run_sync(Base.metadata.drop_all)
        print("todo: create all")
        await conn.run_sync(Base.metadata.create_all)


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    session.add(user)
    print("user create", user)

    await session.commit()
    print("user saved", user)

    # not necessary!! if expire_on_commit=False
    await session.refresh(user)
    print("user refreshed", user)

    return user


async def get_all_users(session: AsyncSession) -> list[User]:
    stmt = select(User)
    stmt = stmt.order_by(User.id)
    result: Result = await session.execute(stmt)
    users: list[User] = result.scalars().all()

    print("users:", users)

    return users


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    user = await session.get(User, user_id)
    print("user", user)
    return user


async def get_user_by_username_match(session: AsyncSession, username_part: str) -> list[User]:
    stmt = select(User).where(
        User.username.ilike(f"%{username_part}%")
    )

    result: Result = await session.execute(stmt)
    users: list[User] = result.scalars().all()

    print("users:", users)

    return users


async def get_user_by_username_exact(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(
        User.username == username,
    )
    result: Result = await session.execute(stmt)
    user: User | None = result.scalar_one_or_none()
    print("found user", user)
    return user


async def create_author_for_user(
    session: AsyncSession,
    user: User,
    author_name: str,
) -> Author:
    author = Author(
        name=author_name,
        user=user,
    )
    session.add(author)
    await session.commit()
    print("author:", author)
    return author


async def get_author_by_username(
    session: AsyncSession,
    username: str,
) -> Author | None:
    stmt = select(Author).join(Author.user).where(User.username == username)

    result: Result = await session.execute(stmt)
    author: Author | None = result.scalar_one_or_none()

    print("found author by username", username, author)

    return author


async def create_posts_for_author(
    session: AsyncSession,
    author: Author,
    posts_titles: list[str],
) -> list[Post]:
    posts = [
        Post(
            title=title,
            author=author,
        )
        for title in posts_titles
    ]
    print("posts to create:", posts)

    session.add_all(posts)

    await session.commit()
    print("created posts", posts)

    return posts


async def get_authors_with_users_and_posts_and_tags(session: AsyncSession):
    stmt = (
        select(Author)
        # .join(Author.user)
        # .where(User.username == "sam")
        .options(
            joinedload(Author.user),
            selectinload(Author.posts).selectinload(Post.tags),
        )
    )

    result: Result = await session.execute(stmt)
    authors: Iterable[Author] = result.scalars()
    for author in authors:
        print("author", author)
        print(" - with user", author.user)
        print("  :posts:", author.posts)
        for post in author.posts:
            print(" -- post", post.title, post.tags)


async def create_tags(session: AsyncSession, *tag_names: str) -> list[Tag]:
    tags = [
        Tag(name=name)
        for name in tag_names
    ]
    session.add_all(tags)
    await session.commit()
    print("created tags", tags)

    return tags


async def create_posts_tags_associations(session: AsyncSession):
    stmt_tags = select(Tag)
    result: Result = await session.execute(stmt_tags)
    tags: list[Tag] = result.scalars().all()

    # stmt_posts = select(Post)
    stmt_posts = select(Post).options(noload(Post.tags))
    # stmt_posts = select(Post).options(selectinload(Post.tags))
    result: Result = await session.execute(stmt_posts)
    posts: list[Post] = result.scalars().all()

    # tag_python: Tag | None = next(filter(lambda t: t.name == "python", tags), None)
    tag_python = None
    for tag in tags[:]:
        if tag.name == "python":
            tag_python = tag
            tags.remove(tag)
            break

    for post in posts:
        print("* process post", post, "with tags", post.tags)
        for tag in tags:
            if tag.name.lower() in post.title.lower():
                post.tags.append(tag)
        post.tags.append(tag_python)
        print("added tags", post.tags)

    await session.commit()


async def main():
    # await create_tables()
    async with async_session() as session:
        await create_user(session, "john")
        await create_user(session, "sam")
        await create_user(session, "nick")
        await get_all_users(session)
        await get_user_by_id(session, 1)
        await get_user_by_id(session, 3)
        await get_user_by_id(session, 0)
        await get_user_by_username_match(session, "n")
        sam = await get_user_by_username_exact(session, "sam")
        author = await create_author_for_user(session, sam, "Samuel L.")
        nick = await get_user_by_username_exact(session, "nick")
        author_nick = await create_author_for_user(session, nick, "Nick M.")
        author_sam = await get_author_by_username(session, "sam")
        author_nick = await get_author_by_username(session, "nick")
        await create_posts_for_author(
            session,
            author_sam,
            ["ORM Lesson", "SQLAlchemy Tutorial"],
        )

        await create_posts_for_author(
            session,
            author_nick,
            ["PyCharm Update", "Postgres News"],
        )
        # await get_authors_with_users_and_posts(session)
        await create_tags(
            session,
            "orm",
            "sqlalchemy",
            "pycharm",
            "postgres",
            "python",
        )
        await create_posts_tags_associations(session)
        await get_authors_with_users_and_posts_and_tags(session)


if __name__ == '__main__':
    asyncio.run(main())
