import asyncio
from itertools import cycle
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from models import Base, User, Post, Tag
from models.db_async import async_engine, async_session
import re
import unicodedata


def slugify(s, sep="-", max_len=None):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", sep, s).strip(sep)
    if max_len and len(s) > max_len:
        s = s[:max_len].rstrip(sep)
    return s


async def create_users():
    user_john = User(
        username="john",
        email="john@example.com",
    )
    async with async_session() as session:
        session.add(user_john)
        print("user before commit:", user_john)
        await session.commit()
        print("user after commit:", user_john)

    users = [
        User(
            username="bob",
            email="bob@example.com",
            full_name="Bob White",
        ),
        User(
            username="alice",
        ),
    ]
    async with async_session() as session, session.begin():
        session.add_all(users)


async def create_users_and_posts(
    session: AsyncSession,
):
    user_john = User(
        username="john",
        email="john@example.com",
    )
    user_bob = User(
        username="bob",
        email="bob@example.com",
        full_name="Bob White",
    )
    user_alice = User(
        username="alice",
    )
    users = [
        user_john,
        user_bob,
        user_alice,
    ]
    session.add_all(users)
    # это не часто используется
    # тут мы получаем айдишники, но ещё не сохраняем всё
    # await session.flush()
    await session.commit()

    for count, user in enumerate(users):
        if not count:
            continue

        posts = []
        for num in range(1, count + 1):
            post_title = f"post-{num:02d} by {user.username} ({user.id})"
            post = Post(
                title=post_title,
                slug=slugify(post_title),
                # user=user,
                user_id=user.id,
            )
            posts.append(post)
        session.add_all(posts)

    await session.commit()


async def create_tags(
    session: AsyncSession,
    *tags_names: str,
) -> list[Tag]:
    tags = [Tag(name=name) for name in tags_names]
    session.add_all(tags)
    await session.commit()
    return tags


async def initial_creation():
    # print(Base.metadata.tables)
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    # insert_values()
    # await create_users()

    tags = [
        "SQLAlchemy",
        "tutorial",
        "Python",
        "async",
        "REST",
        "backend",
        "containers",
        "observability",
        "typing",
        "web",
        "API",
        "database",
        "best practices",
        "deep dive",
        "migrations",
        "metrics",
    ]

    async with async_session() as session:
        await create_users_and_posts(session)
        await create_tags(session, "PyCharm", "VS Code", "Django", "FastAPI")
        await create_tags(session, *tags)


async def show_posts_with_authors(
    session: AsyncSession,
):
    # statement = select(Post).order_by(Post.id)
    statement = (
        select(Post)
        .options(
            joinedload(Post.user),
        )
        .order_by(Post.id)
    )
    posts = (await session.scalars(statement)).all()
    for post in posts:
        print("-", post, "by", post.user)


async def show_users_with_posts(session: AsyncSession):
    statement = (
        select(User)
        # .where(func.length(User.username) > 3)
        .options(
            selectinload(User.posts),
        ).order_by(User.id)
    )
    users = (await session.scalars(statement)).all()
    for user in users:
        print(user, "and posts:")
        if not user.posts:
            print("=== no posts yet === ")
            continue
        for post in user.posts:
            print("  •", post)


async def create_posts_with_tags_for_users(
    session: AsyncSession,
    users: Sequence[User],
):
    users_cycle = cycle(users)

    titles = [
        "How to get started with SQLAlchemy. Tutorial 1",
        "Deep dive into Python typing",
        "Async patterns in web apps",
        "Designing RESTful APIs",
        "Designing Async RESTful APIs",
        "Optimizing database queries",
        "Testing strategies for backend services. Tutorial.",
        "Deploying with containers",
        "Deploying best practices",
        "Security best practices",
        "Working with migrations",
        "Observability and metrics",
        "Scaling background jobs",
        "Data modeling patterns",
    ]
    tags = (await session.scalars(select(Tag))).all()

    for title in titles:
        post = Post(
            title=title,
            slug=slugify(title),
            user=next(users_cycle),
        )
        session.add(post)

        title_lower = title.lower()
        for tag in tags:
            if tag.name.lower() in title_lower:
                post.tags.append(tag)

    await session.commit()


async def show_posts_with_tags(session: AsyncSession):
    posts = (
        await session.scalars(
            select(Post)
            .order_by(Post.id)
            .options(
                selectinload(Post.tags),
            )
        )
    ).all()

    for post in posts:
        print("+", post)
        if not post.tags:
            print("  -- no tags yet")
            continue
        print("  tags:")
        for tag in post.tags:
            print("  •", tag.name)


async def main() -> None:
    """"""
    # print(Base.metadata.tables)
    await initial_creation()
    async with async_session() as session:  # type: AsyncSession
        result = await session.scalars(select(User))
        users: list[User] = list(result.all())
        await create_posts_with_tags_for_users(session, users)

    async with async_session() as session:  # type: AsyncSession
        await show_posts_with_authors(session)
        await show_users_with_posts(session)
        await show_posts_with_tags(session)


if __name__ == "__main__":
    asyncio.run(main())
