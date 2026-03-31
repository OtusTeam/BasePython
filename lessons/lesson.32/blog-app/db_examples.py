import asyncio
from collections.abc import Sequence
from itertools import cycle

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session, joinedload, selectinload

from models import Base, User, Post, Tag
from models.db_async import async_session, async_engine


async def insert_users() -> None:
    user_john = User(
        username="john",
        email="john@example.com",
        full_name="Johnathan",
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


async def insert_posts(
    session: AsyncSession,
    user: User,
    posts_titles: list[str],
) -> None:
    posts = [
        Post(
            title=title,
            content=f"content for user {user.id} - title {title}",
            # user_id=user.id,
            user=user,
        )
        for title in posts_titles
    ]
    session.add_all(posts)
    await session.commit()
    print(posts)


async def fetch_users(
    session: AsyncSession,
) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    users = await session.scalars(stmt)
    return users.all()


async def create_posts_for_all_users(
    session: AsyncSession,
) -> None:
    users = await fetch_users(session)
    for idx, user in enumerate(users, start=1):
        await insert_posts(
            session,
            user,
            [
                # просто какой-то заголовок
                f"title-user-{user.username}-{i}"
                for i in range(1, idx + 1)
            ],
        )


async def show_posts_with_authors(
    session: AsyncSession,
) -> None:
    stmt = (
        select(Post)
        .options(
            joinedload(Post.user),
            # subqueryload(Post.user),
        )
        .order_by(
            Post.title,
            Post.id.asc(),
        )
    )
    posts_result = await session.scalars(stmt)
    posts: Sequence[Post] = posts_result.all()

    for post in posts:
        print("-", post)
        print(" • author:", post.user)


async def show_users_and_their_posts(
    session: AsyncSession,
) -> None:
    stmt = (
        select(User)
        .where(
            User.email.is_not(None),
        )
        .options(
            selectinload(User.posts),
        )
        .order_by(
            User.username,
        )
    )
    users_result = await session.scalars(stmt)
    users: Sequence[User] = users_result.all()

    for user in users:
        print("+", user)
        if not user.posts:
            print(" [no posts]")
            continue
        for post in user.posts:
            print(" -", post)


async def show_filtered_users_and_their_posts(
    session: AsyncSession,
) -> None:
    stmt = (
        select(User)
        .join(
            User.posts,
        )
        .where(
            Post.title.like("%-2"),
        )
        .options(
            selectinload(User.posts),
        )
        .order_by(
            User.username,
        )
    )
    users_result = await session.scalars(stmt)
    users: Sequence[User] = users_result.all()

    for user in users:
        print("+", user)
        if not user.posts:
            print(" [no posts]")
            continue
        for post in user.posts:
            print(" -", post)


async def show_posts_with_tags(
    session: AsyncSession,
) -> None:
    stmt = (
        select(Post)
        .options(
            selectinload(Post.tags),
        )
        .order_by(Post.title)
    )
    posts_result = await session.scalars(stmt)
    posts: Sequence[Post] = posts_result.all()

    for post in posts:
        print("-", post)
        print(" • tags:", post.tags)


async def create_posts_with_names_for_all_users(
    session: AsyncSession,
    posts_titles: list[str],
) -> None:
    users: Sequence[User] = await fetch_users(session)

    posts = []
    for post_title, user in zip(posts_titles, cycle(users)):
        posts.append(
            Post(
                title=post_title,
                content=f"content for user {user.id} - title {post_title}",
                user=user,
            )
        )

    session.add_all(posts)
    await session.commit()
    print("posts:")
    print(posts)


async def get_tags(
    session: AsyncSession,
) -> list[Tag]:

    stmt = select(Tag).order_by(Tag.name)

    tags_result = await session.scalars(stmt)
    tags = tags_result.all()
    return list(tags)


async def create_tags(
    session: AsyncSession,
    tag_names: list[str],
) -> None:
    stmt_tag_name = select(Tag.name).order_by(Tag.name)
    tags_results = await session.scalars(stmt_tag_name)
    res_tags_names = tags_results.all()
    tags_names = {tag_name.lower() for tag_name in res_tags_names}

    seen = set()
    tags = []  #
    for name in tag_names:
        name_lower = name.lower()
        if name_lower not in tags_names and name_lower not in seen:
            tags.append(Tag(name=name))
            seen.add(name_lower)

    session.add_all(tags)
    await session.commit()

    stmt = (
        select(Tag)
        .where(
            Tag.name.in_(tag_names),
        )
        .order_by(Tag.name)
    )
    new_tags_result = await session.scalars(stmt)
    new_tags = new_tags_result.all()
    print("tags:", new_tags)


async def auto_bind_tags_to_posts(
    session: AsyncSession,
) -> None:
    stmt_tags = select(Tag)
    all_tags_result = await session.scalars(stmt_tags)
    all_tags = all_tags_result.all()
    tag_name_to_tag = {tag.name.lower(): tag for tag in all_tags}

    stmt = select(Post).options(
        selectinload(Post.tags),
    )
    all_posts_result = await session.scalars(stmt)
    all_posts: Sequence[Post] = all_posts_result.all()

    for post in all_posts:
        post_title = post.title.lower().strip()
        for part in post_title.split():
            tag = tag_name_to_tag.get(part.strip())
            if not tag:
                continue
            if tag not in post.tags:
                post.tags.append(tag)

    await session.commit()


posts_names = [
    "Python FastAPI Intro",
    "Python Django Intro",
    "Go Intro",
    "JS Intro",
    "Python lesson",
    "Go lesson",
    "Python news",
]

tags_names_create = [
    #
    tag_name.strip()
    for post_name in posts_names
    for tag_name in post_name.split()
]


async def main() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    await insert_users()

    async with async_session() as session:
        # await insert_posts(session)
        # users = await fetch_users(session)
        # print("users:", users)
        await create_posts_for_all_users(session)
        await show_posts_with_authors(session)
        await show_users_and_their_posts(session)
        await show_filtered_users_and_their_posts(session)
        await create_posts_with_names_for_all_users(
            session,
            posts_names,
        )
        await create_tags(session, tags_names_create)
        await auto_bind_tags_to_posts(session)
        await show_posts_with_tags(session)


if __name__ == "__main__":
    asyncio.run(main())
