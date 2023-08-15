import asyncio

import config
from models import engine
from models import User, Post, Tag

from sqlalchemy import func, select, literal
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session, joinedload, selectinload, sessionmaker


async_engine = create_async_engine(
    url=config.ASYNC_DB_URL,
    echo=config.DB_ECHO,
)

async_session = sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def create_user(
    session: AsyncSession,
    username: str,
    email: str | None = None,
) -> User:
    user = User(username=username, email=email)

    session.add(user)
    await session.commit()

    print(user)
    return user


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    user = await session.get(User, user_id)
    print("user by id", user_id, "value:", user)
    return user


async def get_user_by_username(session: AsyncSession, username: str) -> User:
    result: Result = await session.execute(statement=select(User).where(User.username == username))
    user = result.scalar_one()
    # user = result.scalar_one_or_none()
    # result.scalars().first()
    # result.scalar_one_or_none()
    print("user by username", username, "value:", user)
    return user


async def create_post(session: AsyncSession, post_title: str, user: User) -> Post:
    post = Post(
        title=post_title,
        user_id=user.id,
        # user=user,
    )

    session.add(post)
    await session.commit()

    print("created post", post)

    return post


async def show_user_with_posts(session: AsyncSession, user_id: int) -> User | None:
    # session.expire_all()
    user: User | None = await (
        session
        .get(
            User,
            user_id,
            options=(selectinload(User.posts),),
        )
    )
    if user is None:
        print("user not found")
        return

    print()
    print("************* user", user.username)
    for post in user.posts:
        print("post", post.id, post.title)

    print()
    return user


async def show_users_with_posts(
    session: AsyncSession,
    only_with_posts: bool = False,
) -> list[User]:
    stmt = (
        select(User)
        .options(
            joinedload(User.posts, innerjoin=only_with_posts)
            # selectinload(User.posts)
        )
        .order_by(User.id)
    )
    result: Result = await session.execute(stmt)
    # print(result)
    users: list[User] = result.unique().scalars().all()

    # for user in users:
    #     print("u", user)

    for user in users:

        print()
        print("************* user", user.username)
        for post in user.posts:
            print("post", post.id, post.title)

        print()

    return users


async def show_posts_with_users(session: AsyncSession) -> list[Post]:
    stmt = (
        select(Post)
        # .options(joinedload(Post.user, innerjoin=True))
        .options(
            joinedload(Post.user)
        )
        .order_by(Post.id)
    )

    result: Result = await session.execute(stmt)
    posts: list[Post] = result.scalars().all()

    for post in posts:
        print()
        print("*" * 10, post.id, post.title, post.user)

    return posts


async def show_posts_with_title_len_no_more(
    session: AsyncSession,
    max_title_len: int,
) -> list[Post]:
    stmt = (
        select(Post)
        .where(
            func.length(Post.title) <= max_title_len,
        )
        .order_by(Post.id)
    )

    result: Result = await session.execute(stmt)
    posts: list[Post] = result.scalars().all()

    for post in posts:
        print("post", post.id, len(post.title), post.title)

    return posts


async def show_users_by_email_domain(session: AsyncSession, domain: str) -> list[User]:
    stmt = (
        select(User)
        .where(User.email.ilike(f"%{domain}"))
        .order_by(User.id)
    )
    result: Result = await session.execute(stmt)
    users: list[User] = result.scalars().all()
    print("users with email domain", domain, users)

    return users


async def show_posts_with_users_on_domain(session: AsyncSession, domain: str) -> list[Post]:
    stmt = (
        select(Post)
        .join(Post.user)
        # .join(
        #     User,
        #     Post.user_id == User.id,
        # )
        .where(
            User.email.ilike(f"%@{domain}")
        )
        .options(joinedload(Post.user))
        .order_by(Post.id)
    )

    result: Result = await session.execute(stmt)
    posts: list[Post] = result.scalars().all()

    print("posts for users on domain", domain)
    for post in posts:
        print()
        print("*" * 10, post.id, post.title, post.user)

    return posts


async def create_tags(session: AsyncSession, *tags_names: str) -> list[Tag]:
    tags = [
        Tag(name=tag_name)
        for tag_name in tags_names
    ]
    session.add_all(tags)
    await session.commit()

    print("tags:", tags)
    return tags


async def show_posts_with_tags(
    session: AsyncSession,
) -> None:
    stmt = (
        select(Post)
        .options(selectinload(Post.tags))
        # .options(noload(Post.tags))
        .order_by(Post.id)
    )
    result: Result = await session.execute(stmt)
    posts: list[Post] = result.scalars().all()
    for post in posts:
        print(" --- post", post.id, post.title)
        print("post tags:", post.tags)


async def auto_associate_tags_with_posts(
    session: AsyncSession,
) -> None:
    stmt_posts = (
        select(Post)
        .options(selectinload(Post.tags))
        # .options(noload(Post.tags))
        .order_by(Post.id)
    )
    result: Result = await session.execute(stmt_posts)
    posts: list[Post] = result.scalars().all()

    stmt_tags = (
        select(Tag)
        .order_by(Tag.id)
    )
    result: Result = await session.execute(stmt_tags)
    tags: list[Tag] = result.scalars().all()

    for post in posts:
        title = post.title.lower()
        for tag in tags:
            if tag.name.lower() in title and tag not in post.tags:
                post.tags.append(tag)

    await session.commit()


async def show_posts_with_any_of_tags(session: AsyncSession, *tags_names: str) -> list[Post]:
    stmt = (
        select(Post)
        .join(Post.tags)
        .where(
            func.lower(Tag.name).in_(tags_names),
        )
        .options(
            joinedload(Post.user),
            selectinload(Post.tags),
        )
        .order_by(Post.id)
    )

    result: Result = await session.execute(stmt)
    posts: list[Post] = result.scalars().all()

    for post in posts:
        print("----")
        print("post", post.id, post.title)
        print("author:", post.user)
        print("tags:", post.tags)

    return posts


async def show_users_using_tags(session: AsyncSession, *tags_names: str) -> list[User]:
    stmt = (
        select(User)
        .join(User.posts)
        .join(Post.tags)
        .where(
            func.lower(Tag.name).in_(tags_names),
        )
        .order_by(User.id)
    )
    result: Result = await session.execute(stmt)
    users: list[User] = result.unique().scalars().all()

    for user in users:
        print("----")
        print("author:", user)

    return users


async def show_users_using_tags_with_posts_and_tags(
    session: AsyncSession,
    *tags_names: str,
) -> list[User]:
    stmt = (
        select(User)
        .join(User.posts)
        .join(Post.tags)
        .where(
            func.lower(Tag.name).in_(tags_names),
        )
        .options(
            joinedload(
                User.posts
            ).selectinload(
                Post.tags
            )
        )
        .order_by(User.id)
    )

    result: Result = await session.execute(stmt)
    users: list[User] = result.unique().scalars().all()

    for user in users:
        print("----")
        print("author:", user)
        print("--posts--")
        for post in user.posts:
            print("post", post.id, post.title)
            print("tags:", post.tags)

    return users


async def run_queries():
    async with async_session() as session:  # type: AsyncSession
        # result: Result = await session.execute(select(literal("1")))
        # print(result.scalar_one())

        # user_john = await create_user(session, username="john", email="john@example.com")
        # user_sam = await create_user(session, username="sam", email="sam@yahoo.com")
        # user_nick = await create_user(session, username="nick", email="nick@example.com")
        # user_kate = await create_user(session, username="kate", email="kate@yahoo.com")

        # await get_user_by_id(session, 2)
        # await get_user_by_id(session, 1)
        # await get_user_by_id(session, 0)

        # user_sam = await get_user_by_username(session, "sam")
        # user_john = await get_user_by_username(session, "john")
        # user_kate = await get_user_by_username(session, "kate")

        # await create_post(session, "SQL Lesson", user=user_john)
        #
        # await create_post(session, "Python news", user=user_sam)
        # await create_post(session, "PyCharm news", user=user_sam)
        # await create_post(session, "VS Code news", user=user_sam)
        #
        # await create_post(session, "JS lesson", user=user_kate)

        # await show_user_with_posts(session, user_john.id)
        # await show_user_with_posts(session, user_sam.id)

        # await show_user_with_posts(session, 1)
        # await show_user_with_posts(session, 2)

        # await show_users_with_posts(session)
        # await show_users_with_posts(session, only_with_posts=True)

        # await show_posts_with_users(session)

        # await show_posts_with_title_len_no_more(session, 11)
        # await show_users_by_email_domain(session, "@yahoo.com")
        # await show_users_by_email_domain(session, "@example.com")
        # await show_posts_with_users_on_domain(session, "yahoo.com")
        # await show_posts_with_users_on_domain(session, "example.com")

        # await create_tags(session, "news", "python", "PyCharm", "VS Code", "JS")
        # await create_tags(session, "SQL")

        # await show_posts_with_tags(session)
        # await auto_associate_tags_with_posts(session)
        # await show_posts_with_tags(session)
        # await show_posts_with_any_of_tags(session, "python", "js")
        # await show_users_using_tags(session, "python", "js")
        await show_users_using_tags_with_posts_and_tags(session, "python", "js")


def main():
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    asyncio.run(run_queries())


if __name__ == '__main__':
    main()
