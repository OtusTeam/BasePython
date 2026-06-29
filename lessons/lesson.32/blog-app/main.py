import asyncio
from collections.abc import Sequence
from itertools import cycle

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session, selectinload, joinedload

from models import (
    Base,
    engine,
    User,
    Post,
    session_factory,
    Tag,
    async_engine,
    async_session,
)


async def insert_users(
    session: AsyncSession,
):
    john = User(
        username="john",
        email="john@example.com",
    )
    john.hello()
    print(john)

    session.add(john)
    await session.commit()
    print("committed, refreshing")
    await session.refresh(john)
    print("new john:", john)

    bob = User(
        username="bob",
        email="bob@example.com",
        full_name="Bob Black",
    )
    alice = User(
        username="alice",
        full_name="Alice",
    )
    new_users = [bob, alice]
    session.add_all(new_users)
    await session.commit()
    print("committed")
    print("new users:", new_users)


async def get_user(
    session: AsyncSession,
    username: str,
) -> User:
    stmt = select(User).where(User.username == username)
    result = await session.execute(stmt)
    return result.scalar_one()


async def insert_posts(
    session: AsyncSession,
    user: User,
    *posts_titles: str,
):
    posts = [
        Post(
            title=title,
            user=user,
        )
        for title in posts_titles
    ]
    session.add_all(posts)
    await session.commit()


async def create_posts(session: AsyncSession):
    await insert_posts(
        session,
        await get_user(session, "bob"),
        "Hello World (by Bob)",
    )
    await insert_posts(
        session,
        await get_user(session, "alice"),
        "Python lessons",
        "SQlite lessons",
    )


async def fetch_users(session: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    return (await session.scalars(stmt)).all()


async def fetch_users_with_posts(session: AsyncSession) -> Sequence[User]:
    stmt = (
        select(User)
        # .where(User.email.isnot(None))
        # .where(func.length(User.username) > 3)
        .options(
            selectinload(User.posts),
        ).order_by(User.id)
    )
    users = await session.scalars(stmt)
    return users.all()


async def show_users(session: AsyncSession):
    # users = fetch_users(session)
    users = await fetch_users_with_posts(session)
    for user in users:
        print("-", user)
        for post in user.posts:
            print(" ·", post)


async def fetch_posts(session: AsyncSession) -> Sequence[Post]:
    stmt = select(Post).order_by(Post.id)
    return (await session.scalars(stmt)).all()


async def fetch_posts_with_user(session: AsyncSession) -> Sequence[Post]:
    stmt = (
        select(Post)
        .options(
            joinedload(Post.user),
        )
        .order_by(Post.id)
    )
    posts = await session.scalars(stmt)
    return posts.all()


async def show_posts(session: AsyncSession):
    # posts = fetch_posts(session)
    posts = await fetch_posts_with_user(session)
    for post in posts:
        print("-", post)
        print("   by", post.user)


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


async def create_tags(session: AsyncSession) -> None:
    tags = [
        Tag(
            slug=tag_slug,
            display_name=tag_title,
        )
        for tag_slug, tag_title in tags_slugs_create
    ]
    session.add_all(tags)
    print("new tags:", tags)
    await session.commit()
    print("saved tags:", tags)


async def create_posts_for_users(session: AsyncSession) -> None:
    users = await fetch_users(session)
    posts = [
        Post(
            title=post_title,
            user=user,
        )
        for post_title, user in zip(posts_titles, cycle(users))
    ]
    session.add_all(posts)
    await session.commit()
    print("saved posts:", posts)


async def auto_assign_new_tags_to_posts(
    session: AsyncSession,
) -> None:
    all_tags: Sequence[Tag] = (await session.scalars(select(Tag))).all()
    all_posts: Sequence[Post] = (
        await session.scalars(
            select(Post).options(
                selectinload(Post.tags),
            )
        )
    ).all()

    tag_slug_to_tag = {tag.slug: tag for tag in all_tags}

    for post in all_posts:
        post_title = post.title.lower()
        for title_word in post_title.split():
            tag = tag_slug_to_tag.get(title_word.strip())
            if not tag:
                continue
            if tag not in post.tags:
                post.tags.append(tag)
                # print("adding tag", tag, "to post", post)

    await session.commit()


async def fetch_posts_with_tags(
    session: AsyncSession,
) -> Sequence[Post]:
    return (
        await session.scalars(
            select(Post).options(
                selectinload(Post.tags),
            )
        )
    ).all()


async def fetch_posts_with_tags_and_authors(
    session: AsyncSession,
) -> Sequence[Post]:
    return (
        await session.scalars(
            select(Post).options(
                selectinload(Post.tags),
                joinedload(Post.user),
            )
        )
    ).all()


async def fetch_users_with_posts_with_tags(
    session: AsyncSession,
) -> Sequence[User]:
    stmt = (
        select(User)
        .options(
            selectinload(
                User.posts,
            ).selectinload(
                Post.tags,
            ),
        )
        .where(
            func.length(User.username) > 3,
        )
        .order_by(
            User.username,
        )
    )
    return (await session.scalars(stmt)).all()


async def show_posts_with_tags(session: AsyncSession) -> None:
    posts = await fetch_posts_with_tags(session)
    for post in posts:
        print("-", post)
        for tag in post.tags:
            print("  ª", tag)


async def show_posts_with_tags_and_authors(session: AsyncSession) -> None:
    posts = await fetch_posts_with_tags_and_authors(session)
    for post in posts:
        print("-", post, "by", post.user)
        for tag in post.tags:
            print("  ª", tag)


async def show_users_with_posts_with_tags(session: AsyncSession) -> None:
    users = await fetch_users_with_posts_with_tags(session)
    for user in users:
        print("-", user)
        for post in user.posts:
            print(" ·", post)
            for tag in post.tags:
                print("  ª", tag)


async def fetch_users_with_posts_with_tags_by_post_title(
    session: AsyncSession,
    text_match: str,
) -> Sequence[User]:
    stmt = (
        select(User)
        .join(User.posts)
        .options(
            selectinload(
                User.posts,
            ).selectinload(
                Post.tags,
            ),
        )
        .where(
            func.length(User.username) > 3,
            Post.title.ilike(text_match),
        )
        .order_by(
            User.username,
        )
    )
    return (await session.scalars(stmt)).unique().all()


async def show_users_with_posts_with_tags_by_post_title(
    session: AsyncSession,
    text_part: str,
) -> None:
    users = await fetch_users_with_posts_with_tags_by_post_title(
        session,
        f"%{text_part.replace('%', '%%')}%",
    )
    for user in users:
        print("-", user)
        for post in user.posts:
            print(" ·", post)
            for tag in post.tags:
                print("  ª", tag)


async def main():
    async with async_session() as session:
        # await insert_users(session)
        # await create_posts(session)
        # await show_users(session)
        # await show_posts(session)
        # await create_tags(session)
        # await create_posts_for_users(session)
        # await auto_assign_new_tags_to_posts(session)
        # await show_posts_with_tags(session)
        await show_posts_with_tags_and_authors(session)
        await show_users_with_posts_with_tags(session)
        await show_users_with_posts_with_tags_by_post_title(session, "Go")
        await show_users_with_posts_with_tags_by_post_title(session, "Python")
        await show_users_with_posts_with_tags_by_post_title(session, "news")


if __name__ == "__main__":
    asyncio.run(main())
