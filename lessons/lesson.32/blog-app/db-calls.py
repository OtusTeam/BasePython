import asyncio
from datetime import datetime
from itertools import cycle
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload, noload

from models.db_async import async_session
from models import User, Post, UserStatus, Tag


async def create_users(
    session: AsyncSession,
) -> None:
    bob = User(
        username="bob",
        email="bob@example.com",
        created_at=datetime.utcnow(),
    )
    alice = User(
        username="alice",
        email="alice@example.com",
    )
    john = User(
        username="john",
        full_name="John Smith",
    )
    session.add(bob)
    print("bob", bob.id, "'created at' before commit", bob.created_at)
    await session.commit()
    print("bob", bob.id, "'created at' after commit", bob.created_at)

    session.add(alice)
    session.add(john)
    await session.commit()


async def get_user_by_username(
    session: AsyncSession,
    username: str,
) -> User:
    statement = select(User).where(User.username == username)
    result = await session.execute(statement)
    return result.scalar_one()


async def create_post(
    session: AsyncSession,
    title: str,
    body: str,
    user_id: int,
) -> Post:
    post = Post(
        title=title,
        body=body,
        user_id=user_id,
    )
    session.add(post)
    await session.commit()
    # await session.refresh(post)
    return post


async def create_posts(
    session: AsyncSession,
    *titles: str,
    user: User,
) -> list[Post]:
    posts = [
        Post(
            title=title,
            user=user,
        )
        for title in titles
    ]
    session.add_all(posts)
    await session.commit()
    return posts


async def get_users(
    session: AsyncSession,
) -> Sequence[User]:
    statement = select(User).order_by(User.id)
    result = await session.scalars(statement)
    return result.all()


async def get_users_with_posts(
    session: AsyncSession,
) -> Sequence[User]:
    statement = (
        select(User)
        # .join(Post)
        # .join(User.posts)
        .join(
            User.posts,
            isouter=False,
        )
        # .join(
        #     Post,
        #     Post.user_id == User.id,
        # )
        .options(
            # joinedload(User.posts),
            selectinload(User.posts),
        ).order_by(User.id)
    )
    # result = session.execute(statement)
    # return result.scalars().all()
    # return session.scalars(statement).all()
    return (await session.scalars(statement)).unique().all()


async def get_posts_with_author(
    session: AsyncSession,
) -> Sequence[Post]:
    statement = (
        select(Post)
        .options(
            joinedload(Post.user),
            # selectinload(Post.user),
        )
        .order_by(Post.id)
    )
    return (await session.scalars(statement)).all()


async def create_statuses(
    session: AsyncSession,
) -> None:
    status_active = UserStatus(
        name="active",
        description="User is active",
    )
    status_prospect = UserStatus(
        name="prospect",
        description="User is prospect",
    )

    session.add(status_active)
    session.add(status_prospect)
    await session.commit()


async def create_some_posts(
    session: AsyncSession,
) -> list[Post]:
    # Sample Post objects for SQLAlchemy model 'Post'
    users = cycle(await get_users(session))
    posts = [
        Post(
            title="Tech The Future of AI Trends",
            body="AI continues to evolve rapidly, impacting many industries. Businesses are adapting to this changing landscape.",
            user=next(users),
        ),
        Post(
            title="Nature: Exploring the Quiet Beauty of Mountain Lakes",
            body="Mountain lakes offer a tranquil escape from city life. Their pristine waters reflect majestic peaks.",
            user=next(users),
        ),
        Post(
            title="Health Simple Morning Routines for Healthy Living",
            body="A consistent morning routine can boost productivity and wellness. Small habits make a big difference.",
            user=next(users),
        ),
        Post(
            title="Tech Advances in Quantum Computing Hardware Design",
            body="Quantum computing hardware is pushing the limits of processing power. Researchers are making significant breakthroughs.",
            user=next(users),
        ),
        Post(
            title="Nature: Wildflower Meadows Thriving in Springtime",
            body="Vibrant wildflower meadows bloom each spring, attracting pollinators. Their colors brighten natural landscapes.",
            user=next(users),
        ),
        Post(
            title="Lifestyle: Embracing Less for More Joy",
            body="Minimalist lifestyle encourages decluttering and mindfulness. It helps people focus on what truly matters.",
            user=next(users),
        ),
        Post(
            title="Top Tech Gadgets You Should Know About",
            body="New gadgets make life easier and more fun. Stay updated to leverage the latest innovations.",
            user=next(users),
        ),
        # Post(
        #     title="1000Top Tech Gadgets You Should Know About",
        #     body="1000New gadgets make life easier and more fun. Stay updated to leverage the latest innovations.",
        #     user_id=1000,
        # ),
    ]
    session.add_all(posts)
    await session.commit()
    return posts


async def create_some_tags(
    session: AsyncSession,
) -> list[Tag]:
    tags_names = {
        "AI",
        "Nature",
        "Health",
        "Tech",
        "Nature",
        "Lifestyle",
        "Tech",
    }
    tags = [Tag(name=name) for name in tags_names]
    session.add_all(tags)
    await session.commit()
    return tags


async def auto_match_tags_posts(
    session: AsyncSession,
) -> None:
    posts = (
        await session.scalars(
            select(Post).options(
                noload(Post.tags),
            )
        )
    ).all()
    tags = (await session.scalars(select(Tag))).all()
    for post in posts:
        for tag in tags:
            if tag.name.lower() in post.title.lower():
                if tag not in post.tags:
                    post.tags.append(tag)

    await session.commit()


async def get_posts_with_tags(
    session: AsyncSession,
) -> list[Post]:
    statement = (
        select(Post)
        .options(
            selectinload(Post.tags),
        )
        .order_by(
            Post.id,
        )
    )
    return list((await session.scalars(statement)).all())


async def main() -> None:
    async with async_session() as session:
        await create_users(session)
        await create_some_posts(session)
        await create_some_tags(session)
        await auto_match_tags_posts(session)

        for post in await get_posts_with_tags(session):
            print("post", post)
            for tag in post.tags:
                print("+", tag)
        await create_statuses(session)
        bob = await get_user_by_username(session, "bob")
        some_post = await create_post(
            session=session,
            title="Post Title",
            body="Post Body",
            user_id=bob.id,
        )
        print(some_post.id, some_post.title, some_post.created_at)

        john = await get_user_by_username(session, "john")
        await create_posts(
            session,
            "Green Post",
            "Red Post",
            "Black Post",
            user=john,
        )
        users_w_posts = await get_users_with_posts(session)
        for user in users_w_posts:
            print("@", user)
            if not user.posts:
                print("- no posts for user", user.username)
                continue
            for post in user.posts:
                print("+", post)

        print()
        print()
        print()

        posts_w_author = await get_posts_with_author(session)
        for post in posts_w_author:
            print("+", post)
            print("@", post.user)


if __name__ == "__main__":
    asyncio.run(main())
