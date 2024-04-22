import asyncio
from typing import Sequence

from sqlalchemy import (
    select,
    update,
    func,
    distinct,
)
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import (
    Session,
    joinedload,
    selectinload,
    aliased,
)

from models import (
    User,
    Post,
    Tag,
    Base,
)
from models.db import (
    async_engine,
    async_session,
)


def example_calc(session: Session):
    result = session.execute(select(1))

    # print(result.all())
    # print(result.one())
    print(result.scalar())

    # SELECT 1 + 2;
    result = session.execute(select(text("1 + 2")))
    print(result.scalar())


async def create_user(
    session: AsyncSession,
    username: str,
    email: str | None = None,
    refresh_after_commit: bool = False,
) -> User:
    user = User(username=username, email=email)
    session.add(user)
    await session.commit()
    if refresh_after_commit:
        await session.refresh(user)
    print("created user:", user)
    return user


async def create_post(
    session: AsyncSession,
    title: str,
    user_id: int,
) -> Post:
    post = Post(title=title, user_id=user_id)
    session.add(post)
    await session.commit()
    print("created post:", post)
    return post


async def create_posts(
    session: AsyncSession,
    *titles: str,
    user_id: int,
) -> list[Post]:
    posts = [
        Post(title=title, user_id=user_id)
        for title in titles
    ]
    session.add_all(posts)
    await session.commit()
    print("created posts:", posts)
    return posts


async def fetch_all_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    res = await session.scalars(stmt)
    users = res.all()
    # result = session.execute(stmt)
    # users = result.scalars().all()
    users_list = list(users)
    for user in users_list:
        print(user)
    return users_list


async def fetch_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    # stmt = select(User).where(User.id == user_id)
    # user = session.scalar(stmt)
    user: User | None = await session.get(User, user_id)
    # await session.refresh(user)
    print("user:", user)
    return user


def fetch_user_by_username(session: Session, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    user = session.scalar(stmt)
    print("user:", user)
    return user


def update_users_emails(
    session: Session,
    username_len: int,
    email_domain: str,
):
    stmt = update(User).where(
        User.email.is_(None),
        func.length(User.username) > username_len,
    ).values(
        {
            User.email: func.concat(func.lower(User.username), email_domain.lower()),
            # User.username: "aqwe"
        }
    )
    session.execute(stmt)
    # print(result.all())
    session.commit()


def fetch_users_for_domain(session: Session, domain: str) -> list[User]:
    stmt = select(User).where(
        User.email.ilike(f"%{domain.lower()}")
    )
    users = session.scalars(stmt).all()
    print(f"users for domain {domain}:", users)
    return users


async def fetch_all_posts(
    session: AsyncSession,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .order_by(Post.id)
    )
    result = await session.scalars(stmt)
    return result.all()


async def fetch_posts_for_user_id(
    session: AsyncSession,
    user_id: int,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .where(Post.user_id == user_id)
        .order_by(Post.id)
    )
    posts = await session.scalars(stmt)
    return posts.all()


async def fetch_users_with_posts(
    session: AsyncSession,
) -> Sequence[User]:
    stmt = (
        select(User)
        # .where(func.length(User.username) > 3)
        .options(
            # joinedload(User.posts),
            selectinload(User.posts),
        )
        .order_by(User.id)
    )
    users = await session.scalars(stmt)
    # return users.unique().all()
    return users.all()


async def fetch_authors_with_posts(
    session: AsyncSession,
) -> Sequence[User]:
    """
    Left join to get only users with posts
    """
    stmt = (
        select(User)
        .join(
            User.posts,
        )
        # .join(
        #     Post,
        #     # Post.user_id == User.id,
        # )
        # .join(
        #     Post,
        #     Post.user_id == User.id,
        # )
        .options(
            joinedload(User.posts)
        )
        .order_by(User.id)
    )
    users = await session.scalars(stmt)
    return users.unique().all()


async def fetch_posts_with_authors(
    session: AsyncSession,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .options(
            # joinedload(Post.author),
            selectinload(Post.author),
        )
        .order_by(Post.id)
    )
    posts = await session.scalars(stmt)
    return posts.all()


async def create_tags(
    session: AsyncSession,
    *tags_names: str,
) -> list[Tag]:
    tags = [
        Tag(name=tag_name)
        for tag_name in tags_names
    ]
    session.add_all(tags)
    await session.commit()
    print(tags)
    return tags


async def create_tags_for_posts_names(
    session: AsyncSession,
) -> Sequence[Tag]:
    posts = await fetch_all_posts(session)
    tags_names = []
    for post in posts:
        parts = post.title.lower().strip().split()
        tags_names.extend(parts)

    tags = [
        Tag(name=name)
        for name in set(tags_names)
        if name
    ]
    session.add_all(tags)
    await session.commit()
    print(tags)
    return tags


async def fetch_all_tags_with_posts(
    session: AsyncSession,
) -> Sequence[Tag]:
    stmt = (
        select(Tag)
        .options(selectinload(Tag.posts))
        .order_by(Tag.id)
    )
    result = await session.scalars(stmt)
    return result.all()


async def fetch_all_posts_with_tags(
    session: AsyncSession,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .options(selectinload(Post.tags))
        .order_by(Post.id)
    )
    posts = await session.scalars(stmt)
    return posts.all()


async def auto_associate_tags_with_posts(session: AsyncSession):
    tags = await fetch_all_tags_with_posts(session)
    posts = await fetch_all_posts_with_tags(session)
    for post in posts:
        post_title = post.title.lower()
        for tag in tags:
            if tag in post.tags:
                continue
            if tag.name.lower() in post_title:
                post.tags.append(tag)

    await session.commit()


async def get_users_with_posts_with_tag(
    session: AsyncSession,
    tag_name: str,
) -> Sequence[User]:
    stmt = (
        select(User)
        .join(User.posts)
        .join(Post.tags)
        .where(
            func.lower(Tag.name) == tag_name.lower(),
        )
        .order_by(User.id)
    )
    result = await session.scalars(stmt)
    users = result.unique().all()
    print("users who used tag", repr(tag_name), "in posts:")
    for user in users:
        print(user)

    return users


async def get_users_with_posts_with_tag_using_subquery(
    session: AsyncSession,
    tag_name: str,
) -> Sequence[User]:
    stmt_user_id_from_posts_with_tag = (
        # select(Post.user_id)
        select(distinct(Post.user_id))
        .join(Post.tags)
        .where(
            func.lower(Tag.name) == tag_name.lower(),
        )
    )

    stmt = (
        select(User)
        .where(
            User.id.in_(
                stmt_user_id_from_posts_with_tag.subquery(),
            ),
        )
        .order_by(User.id)
    )
    result = await session.scalars(stmt)
    users = result.all()
    print("users who used tag", repr(tag_name), "in posts:")
    for user in users:
        print(user)

    return users


async def show_posts_with_one_of_tags(
    session: AsyncSession,
    *tags_names: str,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .join(Post.tags)
        .where(
            func.lower(Tag.name).in_([name.lower() for name in tags_names])
        )
        .options(
            selectinload(Post.tags)
        )
        .order_by(Post.id)
    )
    posts = await session.scalars(stmt)
    return posts.unique().all()


async def show_posts_with_two_tags(
    session: AsyncSession,
    t1_name: str,
    t2_name: str,
) -> Sequence[Post]:
    table_tags1 = aliased(Tag, name="table_tags1")
    table_tags2 = aliased(Tag, name="table_tags2")
    stmt = (
        select(Post)
        .join(
            table_tags1,
            Post.tags,
        )
        .join(
            table_tags2,
            Post.tags,
        )
        .where(
            func.lower(table_tags1.name) == t1_name,
            func.lower(table_tags2.name) == t2_name,
        )
        .options(
            selectinload(Post.tags)
        )
        .order_by(Post.id)
    )
    posts = await session.scalars(stmt)
    return posts.unique().all()


async def show_posts_with_all_tags(
    session: AsyncSession,
    *tags_names: str,
) -> Sequence[Post]:
    stmt = select(Post)
    tags_names = list(set(map(str.lower, tags_names)))
    filters = []
    for tag_name in tags_names:
        table_tags = aliased(Tag, name=f"table_tags_for_{tag_name}")
        stmt = stmt.join(
            table_tags,
            Post.tags,
        )
        filters.append(
            func.lower(table_tags.name) == tag_name
        )

    stmt = (
        stmt
        .where(
            *filters,
        )
        .options(
            selectinload(Post.tags)
        )
        .order_by(Post.id)
    )
    posts = await session.scalars(stmt)
    return posts.unique().all()


async def demo(session: AsyncSession) -> None:
    user_john: User = await create_user(session, "john", refresh_after_commit=True)
    user_sam: User = await create_user(session, "sam")
    user_nick: User = await create_user(session, "nick")
    # await fetch_all_users(session)

    await create_post(session, "Intro Lesson", user_id=user_john.id)
    await create_posts(
        session,
        "SQL Introduction",
        "MySQL Lesson",
        "Postgresql Lesson",
        user_id=user_sam.id,
    )

    user_1: User | None = await fetch_user_by_id(session, 1)
    user_2: User | None = await fetch_user_by_id(session, 2)
    user_10: User | None = await fetch_user_by_id(session, 10)

    user_bob: User = await create_user(session, "bob")
    user_alice: User = await create_user(session, "alice")

    await create_posts(
        session,
        "SQL Transactions",
        "Transactions in MySQL",
        user_id=user_bob.id,
    )

    await create_tags(
        session,
        "news",
        "python",
    )

    await create_tags_for_posts_names(session)
    await auto_associate_tags_with_posts(session)

    # 1
    for user_id in (0, 1, 2, 10):
        posts = await fetch_posts_for_user_id(session, user_id)
        if not posts:
            print("no posts for user id", user_id)
            continue
        print("++user id posts", user_id)
        for post in posts:
            print("-", post)
    # 2
    users_with_posts = await fetch_users_with_posts(session)
    for user in users_with_posts:
        print("++ posts for user", user)
        for post in user.posts:
            print("-", post)

    # 3
    authors_with_posts = await fetch_authors_with_posts(session)
    for user in authors_with_posts:
        print("++ posts for author", user)
        for post in user.posts:
            print("-", post)

    # 4
    posts_with_authors = await fetch_posts_with_authors(session)
    for post in posts_with_authors:
        print("post", (post.id, post.title), "author:", post.author)

    posts_w_tags = await fetch_all_posts_with_tags(session)
    for post in posts_w_tags:
        print("P:", post)
        for tag in post.tags:
            print("-t", tag)

    tags_w_posts = await fetch_all_tags_with_posts(session)
    for tag in tags_w_posts:
        print("T:", tag)
        for post in tag.posts:
            print("-", post.id, post.title)

    await get_users_with_posts_with_tag(session, "sql")
    await get_users_with_posts_with_tag(session, "news")
    await get_users_with_posts_with_tag(session, "mysql")

    await get_users_with_posts_with_tag_using_subquery(session, "sql")
    await get_users_with_posts_with_tag_using_subquery(session, "news")
    await get_users_with_posts_with_tag_using_subquery(session, "mysql")

    posts = await show_posts_with_one_of_tags(
        session,
        "mysql",
        "sql",
        "news",
    )
    posts = await show_posts_with_all_tags(
        session,
        "mysql",
        "sql",
    )
    print("ready to show")
    for post in posts:
        print("P:", post)
        for tag in post.tags:
            print("-t", tag)

    posts = await show_posts_with_all_tags(
        session,
        "mysql",
        "sql",
        "transactions",
    )
    print("ready to show")
    for post in posts:
        print("P:", post)
        for tag in post.tags:
            print("-t", tag)


async def async_main():
    # async with async_engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)
    #     await conn.run_sync(Base.metadata.create_all)
    async with async_session() as session:
        await demo(session)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
