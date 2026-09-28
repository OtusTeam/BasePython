import asyncio
from collections.abc import Sequence
from itertools import cycle

from sqlalchemy import select, or_, func
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import Session, selectinload, joinedload, subqueryload

from models import (
    Base,
    User,
    engine,
    session_factory,
    async_engine,
    async_session_factory,
    Post,
    Tag,
)


async def create_clear_tables() -> None:
    async with async_engine.connect() as conn, conn.begin():
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    await async_engine.dispose()


async def insert_values(async_session: AsyncSession):
    bob = User(
        username="bob",
        email="bob@example.com",
    )
    kyle = User(
        username="kyle",
    )
    alice = User(
        username="alice",
        full_name="Alice White",
    )
    async_session.add(bob)
    async_session.add(kyle)
    async_session.add(alice)
    await async_session.commit()

    post_1 = Post(
        title="foo",
        body="bar",
        # user_id=bob.id,
        user=bob,
    )
    post_2 = Post(
        title="fizz",
        body="buzz",
        # user_id=bob.id,
        user=bob,
    )
    post_3 = Post(
        title="lala",
        body="bubub",
        # user_id=alice.id,
        user=alice,
    )
    async_session.add(post_1)
    async_session.add(post_2)
    async_session.add(post_3)
    await async_session.commit()


async def fetch_users(async_session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result = await async_session.scalars(stmt)
    users = result.all()
    return list(users)


async def show_users_with_posts(async_session: AsyncSession):
    stmt = (
        select(User)
        .options(
            selectinload(User.posts),
        )
        .order_by(User.id)
    )
    result = await async_session.scalars(stmt)
    users = result.all()
    for user in users:
        print(user.id, user.username)
        print("with posts:")
        for post in user.posts:
            print(" -", post.title, post.body)


async def show_posts_with_users(async_session: AsyncSession):
    stmt = (
        select(Post)
        .options(
            joinedload(Post.user, innerjoin=True),
        )
        .order_by(Post.id)
    )
    result = await async_session.scalars(stmt)
    posts = result.all()
    for post in posts:
        print("Post:", post.id, post.title, post.body)
        print(" by", post.user.id, post.user.username)


async def show_posts_from_registered_users(async_session: AsyncSession):
    stmt = (
        select(Post)
        .join(Post.user)
        # .join(
        #     User,
        #     Post.user_id == User.id,
        # )
        .options(
            joinedload(
                Post.user,
                innerjoin=True,
            ),
        )
        .where(
            User.email.isnot(None),
        )
        .order_by(Post.id)
    )
    print(stmt)
    result = await async_session.scalars(stmt)
    posts = result.all()
    for post in posts:
        print("Post:", post.id, post.title, post.body)
        print(" by", post.user.id, post.user.username)


posts_titles = [
    "Python FastAPI Intro",
    "Python Django Intro",
    "Go Intro",
    "JS Intro",
    "Python lesson",
    "Go lesson",
    "Python news",
]

tags_slugs_create: set[tuple[str, str]] = {
    (tag_slug.strip().lower(), tag_slug.strip())
    for post_title in posts_titles
    for tag_slug in post_title.split()
}


async def create_tags(async_session: AsyncSession) -> None:
    tags = [
        Tag(
            name=name,
            display_name=display_name,
        )
        for name, display_name in tags_slugs_create
    ]
    print("prepared tags:", tags)
    async_session.add_all(tags)
    await async_session.commit()
    print("saved tags:", tags)


async def create_posts_for_users(async_session: AsyncSession) -> None:
    users: list[User] = await fetch_users(async_session)
    posts = [
        Post(
            title=post_title,
            user=user,
        )
        for post_title, user in zip(posts_titles, cycle(users))
    ]
    async_session.add_all(posts)
    await async_session.commit()
    print("saved posts:", posts)


async def auto_assign_new_tags_to_posts(async_session: AsyncSession) -> None:
    all_tags: Sequence[Tag] = (await async_session.scalars(select(Tag))).all()
    all_posts: Sequence[Post] = (
        await async_session.scalars(
            select(Post).options(
                selectinload(Post.tags),
            )
        )
    ).all()

    tag_name_to_tag = {tag.name: tag for tag in all_tags}

    for post in all_posts:
        post_title = post.title.lower()
        for title_word in post_title.split():
            tag = tag_name_to_tag.get(title_word.strip())
            if not tag:
                continue
            if tag not in post.tags:
                post.tags.append(tag)

    await async_session.commit()


async def show_posts_with_tags(async_session: AsyncSession) -> None:
    stmt = (
        select(Post)
        .where(
            or_(
                Post.title.ilike("%lesson%"),
                Post.title.ilike("%intro%"),
            )
        )
        .options(
            selectinload(Post.tags),
        )
    )
    result = await async_session.scalars(stmt)
    posts = result.all()
    for post in posts:
        print(post)
        print(" *", *[tag.name for tag in post.tags])


async def show_posts_with_tags_and_authors(async_session: AsyncSession) -> None:
    stmt = (
        select(Post)
        .where(
            or_(
                Post.title.ilike("%lesson%"),
                Post.title.ilike("%intro%"),
            )
        )
        .options(
            selectinload(Post.tags),
            joinedload(Post.user, innerjoin=True),
        )
    )
    result = await async_session.scalars(stmt)
    posts = result.all()
    for post in posts:
        print(post, "by", post.user.username)
        print(" *", *[tag.name for tag in post.tags])


async def show_users_with_posts_with_tags(async_session: AsyncSession) -> None:
    stmt = (
        select(User)
        .where(func.length(User.username) > 3)
        .options(
            # selectinload(User.posts).selectinload(Post.tags),
            subqueryload(User.posts).subqueryload(Post.tags),
        )
    )
    result = await async_session.scalars(stmt)
    users = result.all()
    for user in users:
        print(user.username, user.full_name)
        for post in user.posts:
            print(" Post:", post)
            tags_names = [tag.name for tag in post.tags]
            if tags_names:
                print("  *", *tags_names)


async def main():
    # await create_clear_tables()
    async with async_session_factory() as async_session:
        await insert_values(async_session)
        await show_users_with_posts(async_session)
        await show_posts_with_users(async_session)
        await show_posts_from_registered_users(async_session)
        await create_tags(async_session)
        await create_posts_for_users(async_session)
        await auto_assign_new_tags_to_posts(async_session)
        await show_posts_with_tags(async_session)
        await show_posts_with_tags_and_authors(async_session)
        await show_users_with_posts_with_tags(async_session)


if __name__ == "__main__":
    asyncio.run(main())
