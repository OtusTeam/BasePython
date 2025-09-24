import asyncio
from itertools import cycle
from random import randint

from sqlalchemy import select, Sequence, not_
from sqlalchemy.orm import (
    joinedload,
    selectinload,
)
from sqlalchemy.ext.asyncio import AsyncSession

from models import (
    async_session,
    Base,
    User,
    Post,
    Tag,
    async_engine,
)


async def insert_one(
    session: AsyncSession,
):
    user = User(
        username="bob",
        email="bob@example.com",
        full_name="Bob White",
    )
    session.add(user)
    print("user before commit:", user)
    await session.commit()
    print("user after commit:", user)


async def insert_many(
    session: AsyncSession,
) -> None:
    alice = User(
        username="alice",
        full_name="Alice White",
        email="alice@example.com",
    )
    john = User(
        full_name="",
        username="john",
        email="john@abc.qwe",
    )
    kate = User(
        username="kate",
        full_name="Kate Brown",
        email="kate@ya.ru",
    )
    kyle = User(
        username="kyle",
        full_name="",
        email="kyle@hello.org",
    )

    users = [
        alice,
        john,
        kate,
        kyle,
    ]
    session.add_all(users)
    await session.commit()


async def create_users() -> None:
    async with async_session() as session:
        await insert_one(session)
        await insert_many(session)


async def select_users(
    session: AsyncSession,
) -> Sequence[User]:
    statement = select(User).order_by(User.id)
    result = await session.scalars(statement)
    return result.all()


async def select_tags(
    session: AsyncSession,
) -> list[Tag]:
    statement = select(Tag)
    result = await session.scalars(statement)
    return list(result.all())


async def select_users_with_emails(
    session: AsyncSession,
) -> list[User]:
    statement = (
        select(User)
        .where(
            User.email.is_not(None),
        )
        .order_by(User.id)
    )
    result = await session.scalars(statement)
    return list(result.all())


async def select_users_with_emails_not_end_with(
    session: AsyncSession,
    ends_with: str = "@invalid.mail",
) -> list[int]:
    statement = (
        select(User.id)
        .where(
            not_(
                User.email.endswith(ends_with),
            ),
        )
        .order_by(User.id)
    )
    result = await session.scalars(statement)
    return list(result.all())


async def create_posts_for_user(
    session: AsyncSession,
    user: User,
) -> list[Post]:
    posts = [
        Post(
            title=f"Post #{idx} by {user.username}",
            user=user,
        )
        for idx in range(1, randint(3, 5))
    ]
    session.add_all(posts)
    await session.commit()
    for post in posts:
        print("post:", post)
    return posts


async def create_posts_for_users_with_emails():
    async with async_session() as session:
        users = await select_users_with_emails(session)
        for user in users:
            print("user", user)
            await create_posts_for_user(
                session,
                user=user,
            )


def select_posts(
    session: AsyncSession,
) -> list[Post]:
    statement = select(Post).order_by(Post.id)
    return list(session.scalars(statement).all())


def select_posts_with_users(
    session: AsyncSession,
) -> list[Post]:
    statement = (
        select(Post)
        .options(
            joinedload(Post.user),
        )
        .order_by(Post.id)
    )
    return list(session.scalars(statement).all())


def select_users_with_posts(
    session: AsyncSession,
) -> list[User]:

    statement = (
        select(User)
        .options(
            selectinload(User.posts),
        )
        .order_by(User.id)
    )
    return list(session.scalars(statement).all())


def select_users_by_post_title_match(
    session: AsyncSession,
    match_text: str,
) -> list[User]:
    post_filter = Post.title.ilike(f"%{match_text}%")
    statement = (
        select(User)
        .join(User.posts)
        .where(
            post_filter,
        )
        .options(
            # вот так плюс не иметь в кэше все подтянутые объекты
            # потому что если в сессии будут все релейшншипы, алхимия их покажет
            selectinload(User.posts.and_(post_filter)),
        )
        .order_by(User.id)
    )
    return list(session.scalars(statement).all())


async def create_tags(
    session: AsyncSession,
) -> list[Tag]:
    tag_names = [
        ("python", "Posts about Python"),
        ("sqlalchemy", "ORM-related posts"),
        ("web", "Web development"),
        ("tutorial", "How-to and tutorials"),
        ("ops", "DevOps and deployment"),
        ("data", "Data-related topics"),
    ]

    tags = [Tag(name=name, description=description) for name, description in tag_names]
    session.add_all(tags)

    await session.commit()
    print("created tags:", tags)
    return tags


async def create_posts_with_tags(
    session: AsyncSession,
) -> list[Post]:
    tag_sets = [
        ["python", "sqlalchemy", "tutorial"],
        ["python", "web", "tutorial"],
        ["web", "ops", "data", "python"],
        ["sqlalchemy", "data", "python"],
        ["ops", "web", "tutorial"],
        ["data", "python", "sqlalchemy"],
        ["web", "tutorial", "ops"],
    ]

    # all_tags: list[Tag] = await select_tags(session)
    #
    # # users' ids
    # some_users: list[int] = await select_users_with_emails_not_end_with(session)

    all_tags, some_users = await asyncio.gather(  # type: list[Tag], list[int]
        select_tags(session),
        select_users_with_emails_not_end_with(session),
    )
    tag_name_to_tag = {tag.name: tag for tag in all_tags}
    user_ids = cycle(some_users)
    posts = []
    for tag_set in tag_sets:
        tags_text = " | ".join(tag_set)
        user_id = next(user_ids)
        post = Post(
            title=f"Post by user #{user_id} ({tags_text})",
            user_id=user_id,
        )
        for tag_name in tag_set:
            post.tags.append(tag_name_to_tag[tag_name])

        posts.append(post)

    session.add_all(posts)
    await session.commit()

    print("created posts:", posts)
    return posts


async def get_posts_with_tags(
    session: AsyncSession,
) -> list[Post]:
    statement = (
        select(Post)
        .options(
            selectinload(Post.tags),
            # subqueryload(Post.tags),
        )
        .order_by(Post.id)
    )
    result = await session.scalars(statement)
    return list(result.all())


async def get_users_with_posts_matching_tag(
    session: AsyncSession,
    tag_name: str,
) -> list[User]:
    tag_filter = Tag.name == tag_name
    statement = (
        select(User)
        .join(User.posts)
        .join(Post.tags)
        .where(tag_filter)
        .options(
            selectinload(
                User.posts.and_(
                    Post.tags.and_(tag_filter),
                ),
            ).selectinload(Post.tags),
        )
        .order_by(User.id)
    )
    result = await session.scalars(statement)
    return list(result.unique().all())


async def create_clear_tables():
    """
    Только для примера. Так-то у нас есть миграции.
    """
    async with async_engine.connect() as conn:
        async with conn.begin():
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)


async def main() -> None:
    # await create_clear_tables()

    await create_users()
    await create_posts_for_users_with_emails()

    async with async_session() as session:
        await create_tags(session)
        await create_posts_with_tags(session)

        posts = await get_posts_with_tags(session)
        for post in posts:
            print("-", post)
            if not post.tags:
                print(" ***no tags")
                continue
            for tag in post.tags:
                print(" *", tag)

        users = await get_users_with_posts_matching_tag(session, "python")
        for user in users:
            print("•", user)
            for post in user.posts:
                print(" -", post)
                for tag in post.tags:
                    print("  **", tag)


if __name__ == "__main__":
    asyncio.run(main())
