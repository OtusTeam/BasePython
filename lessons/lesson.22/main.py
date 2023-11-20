import asyncio
from typing import Sequence

from sqlalchemy import select
from sqlalchemy import and_
from sqlalchemy import or_
from sqlalchemy import func
from sqlalchemy import update
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import joinedload, selectinload

import config
from models import Base
from models import Post
from models import User


async_engine = create_async_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
)
async_session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def create_user(
    session: AsyncSession,
    username: str,
    email: str | None = None,
) -> User:
    user = User(
        username=username,
        email=email,
    )
    print(user)
    session.add(user)
    await session.commit()
    print("saved user")
    # await session.refresh(user)
    print("user details:", user)
    return user


async def create_users(
    session: AsyncSession,
    *usernames: str,
) -> list[User]:
    users = [User(username=username) for username in usernames]
    session.add_all(users)
    await session.commit()
    print("saved users:", users)
    return users


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
    user = await session.get(User, user_id)
    print(user)
    # if user is None:
    #     raise ...
    return user


async def find_user_by_id(
    session: AsyncSession,
    user_id: int,
) -> User | None:
    stmt = select(User).where(User.id == user_id)
    # result: Result = session.execute(stmt)
    # user = result.scalar_one_or_none()
    user = await session.scalar(stmt)
    if user is None:
        print("no user by id", user_id)
    else:
        print("found user", user)

    return user


async def find_user_by_username(
    session: AsyncSession,
    username: str,
) -> User | None:
    # stmt = select(User).where(User.username == username)
    stmt = select(User).where(User.username.ilike(username))
    # stmt = select(User).where(func.lower(User.username) == func.lower(username))
    # result: Result = session.execute(stmt)
    # user = result.scalar_one_or_none()
    user = await session.scalar(stmt)
    # result: Result = await session.execute(stmt)
    # user = result.scalar_one()
    if user is None:
        print("no user by username", username)
    else:
        print("found user", user)

    return user


async def get_user_by_username(
    session: AsyncSession,
    username: str,
) -> User:
    stmt = select(User).where(User.username == username)
    result: Result = await session.execute(stmt)
    return result.scalar_one()


async def demo_update_users(session: AsyncSession):
    filter_has_j = User.username.ilike("j%")
    filters = (
        filter_has_j,
        User.email.is_(None),
        # User.email.isnot(None),
    )
    stmt_users_j = select(User).where(
        *filters,
    )
    users_w_o = (await session.scalars(stmt_users_j)).all()
    print(users_w_o)
    upd_stmt = (
        update(User)
        .where(*filters)
        .values(
            {
                User.email: func.concat(User.username, "@ya.ru"),
                # User.email: "abc",
            }
        )
    )
    await session.execute(upd_stmt)
    await session.commit()
    stmt_users_j_and_has_email = select(User).where(
        filter_has_j,
        User.email.isnot(None),
    )
    # await session.refresh()
    users_w_o = (await session.scalars(stmt_users_j_and_has_email)).all()
    print(users_w_o)


async def find_users(
    session: AsyncSession,
) -> Sequence[User]:
    stmt = (
        select(User)
        .where(
            # or_(
            and_(
                User.email.isnot(None),
                User.username.ilike("%n%"),
            ),
        )
        .order_by(User.id)
    )
    users = (await session.scalars(stmt)).all()
    print(users)
    return users


async def create_post(
    session: AsyncSession,
    user_id: int,
    title: str,
) -> Post:
    post = Post(
        title=title,
        user_id=user_id,
    )
    session.add(post)
    await session.commit()
    print(post)
    return post


async def show_posts_with_authors(session: AsyncSession):
    # stmt = select(Post).where(Post.id == 1).order_by(Post.id)
    # stmt = select(Post).order_by(Post.id)

    # stmt = select(Post.id, Post.title)
    # stmt = select(Post.id, )
    # result: Result = session.execute(stmt)
    # # items = result.scalars().all()
    # items = result.scalars().all()
    # post = result.one_or_none()
    # post = result.one()
    # post = result.scalar_one()
    # post = result.scalar_one_or_none()
    # print(post)
    # return
    # items = result.all()
    # print(items)
    # # for (item,) in items:
    # for item in items:
    #     print("item:", item)
    #     print("- item.id:", item.id)
    #     print("- item.title:", item.title)

    stmt = (
        select(Post)
        .join(Post.user)
        # .where(User.email.isnot(None))
        # .where(User.email.is_(None))
        # .options(joinedload(Post.user))
        .options(selectinload(Post.user))
        .order_by(Post.id)
    )

    result_scalars = await session.scalars(stmt)
    for post in result_scalars.all():  # type: Post
        print("-", post, "by", post.user.username, post.user.email)


async def show_users_with_posts(session: AsyncSession):
    stmt = (
        select(User)
        # .where(User.id <= 2)
        .options(selectinload(User.posts))
        .order_by(User.id)
    )
    result_scalars = await session.scalars(stmt)
    for user in result_scalars.all():  # type: User
        print(user)
        for post in user.posts:  # type: Post
            print("-", post)


async def show_filtered_users_with_posts(session: AsyncSession):
    stmt = (
        select(User)
        .join(User.posts)
        # .join(
        #     Post,
        #     Post.user_id == User.id,
        # )
        # .where(Post.title.ilike("Post by%"))
        # .where(Post.title.ilike("Another%"))
        # .where()
        .group_by(User.id)
        .having(func.count(Post.id) >= 2)
        .options(selectinload(User.posts))
        # .options(joinedload(User.posts))
        .order_by(User.id)
    )
    result_scalars = await session.scalars(stmt)
    for user in result_scalars.unique().all():  # type: User
        print(user)
        for post in user.posts:  # type: Post
            print("-", post)


async def show_count_posts(session: AsyncSession):
    stmt = select(func.count(Post.id))
    print("posts count:", await session.scalar(stmt))


async def main():
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    async with async_session() as session:
        john: User = await create_user(session, "john")
        sam: User = await create_user(session, "sam")
        bob: User = await create_user(session, "bob")
        kate: User = await create_user(session, "kate", "kate@ya.ru")
        nick: User = await create_user(session, "nick", "nick@example.com")

        await create_users(session, "jane", "kyle", "jim")

        john: User = await get_user_by_username(session, "john")
        sam: User = await get_user_by_username(session, "sam")
        # klark: User = await get_user_by_username(session, "klark")

        post1_by_john: Post = await create_post(session, user_id=john.id, title="Post by John")
        post2_by_john: Post = await create_post(session, user_id=john.id, title="Another post by John")
        post_by_sam: Post = await create_post(session, user_id=sam.id, title="Post by Sam")
        await show_posts_with_authors(session)
        await show_users_with_posts(session)
        await show_filtered_users_with_posts(session)
        await show_count_posts(session)

        await get_user_by_id(session, 1)
        await get_user_by_id(session, 2)
        await get_user_by_id(session, 1)
        await find_user_by_id(session, 1)
        await find_user_by_id(session, 2)
        await find_user_by_id(session, 5)
        await find_user_by_id(session, 0)
        await find_user_by_username(session, "qwerty")
        await find_user_by_username(session, "bob")
        await find_user_by_username(session, "Nick")
        await demo_update_users(session)
        await find_users(session)


if __name__ == "__main__":
    asyncio.run(main())
