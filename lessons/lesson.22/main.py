import asyncio

from datetime import datetime
from typing import Iterable

from sqlalchemy import (
    select,
    update,
    create_engine,
    func,
    or_,
)
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy.orm import (
    aliased,
    Session,
    joinedload,
    selectinload,
    sessionmaker,
)

from models import User, Author, Post, Tag

import config

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
)

async_engine = create_async_engine(
    url=config.DB_ASYNC_URL,
    echo=config.DB_ECHO,
)

async_session = sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    print("user", user)
    session.add(user)
    await session.commit()
    # await session.refresh(user)
    print("saved user", user)
    return user


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def get_user_by_username(session: AsyncSession, username: str) -> User:
    stmt = select(User).where(User.username == username)
    result: Result = await session.execute(stmt)
    user: User = result.scalar_one()
    # user: User = result.scalar_one_or_none()
    print("user for username", username, "is", user)

    return user


async def create_author(session: AsyncSession, name: str, user: User) -> Author:
    author = Author(
        name=name,
        user_id=user.id,
        # user=user,
    )
    session.add(author)
    await session.commit()
    print("created author", author)

    return author


async def show_users_with_authors(session: AsyncSession):
    # N+1 Problem (solved)
    users_stmt = (
        # get all users
        select(User)
        # extra options
        .options(
            # join all "to-one" relations (User -> Author)
            joinedload(User.author)
        ).order_by(User.id)
    )
    result: Result = await session.execute(users_stmt)
    users = result.scalars().all()
    # [U1, U2, U3] - with scalars call
    # [(U1, ), (U2, ), (U3, )] - w/o scalars call

    for user in users:
        print(user, user.author)


async def show_users_only_with_authors(session: AsyncSession):
    # N+1 Problem
    users_stmt = (
        # get all users
        select(User)
        # for filtering
        # .join(User.author)
        # extra options
        .options(
            # join all "to-one" relations (User -> Author)
            joinedload(User.author, innerjoin=True)
        )
        # add "where" to SQL
        # .filter(
        #     Author.user_id.isnot(None),
        # )
        # get all
        .order_by(User.id)
    )

    result: Result = await session.execute(users_stmt)
    users = result.scalars().all()
    for user in users:
        print(user, user.author)


async def show_authors_with_users(session: AsyncSession):
    authors_stmt = (
        # get all authors
        select(Author)
        # extra
        .options(
            # join "to-one" users
            joinedload(Author.user)
        )
        # get all objects
        .order_by(Author.id)
    )
    result: Result = await session.execute(authors_stmt)
    authors: Iterable[Author] = result.scalars().all()

    for author in authors:
        print(author, author.user)


async def update_users_emails_by_username(session: AsyncSession, domain: str, *filters):
    async with session.begin():
        stmt = (
            update(
                User,
            )
            .where(*filters)
            .values(
                {
                    User.email: User.username + domain,
                },
            )
            .execution_options(synchronize_session=False)
        )

        await session.execute(stmt)

    # commit happens on __aexit__ for this session in context manager
    # await session.commit()


async def find_authors_by_user_email_domain(session: AsyncSession, email_domain: str):
    authors_stmt = (
        # get author objects
        select(Author)
        # join users
        .join(Author.user)
        .filter(User.email.endswith(email_domain))
        # .join(
        #     User,
        #     Author.user_id == User.id,
        # )
        .options(joinedload(Author.user))
        .order_by(Author.id)
    )

    result: Result = await session.execute(authors_stmt)
    authors: Iterable[Author] = result.scalars().all()

    for author in authors:
        print(author, author.user)


async def find_author_by_user_username(session: AsyncSession, username: str) -> Author:
    stmt = (
        select(Author)
        # явное присоединение
        # explicit join
        .join(Author.user)
        # find by username
        .filter(User.username == username)
    )
    result: Result = await session.execute(stmt)
    author = result.scalar_one()
    print("found author for username", username, author)
    return author


async def create_posts(
    session: AsyncSession,
    author: Author,
    *titles: str,
) -> list[Post]:
    posts = [
        Post(
            title=title,
            author_id=author.id,
        )
        for title in titles
    ]
    session.add_all(posts)
    await session.commit()
    print("posts:", posts)
    return posts


async def show_users_with_author_and_posts(session: AsyncSession):
    users_stmt = (
        # get users
        select(User).options(
            # users' authors
            joinedload(User.author)
            # authors' posts
            .selectinload(Author.posts),
        )
        # sort
        .order_by(User.id)
        # get all of them
    )

    result: Result = await session.execute(users_stmt)
    users: Iterable[User] = result.scalars().all()
    # users: Iterable[User] = result.scalars()

    for user in users:
        print("- user", user)
        if not user.author:
            continue
        print("++ author", user.author)
        print("=== posts:")
        for post in user.author.posts:
            print("=", post)


async def show_authors_with_users_and_posts(session: AsyncSession):
    authors_stmt = (
        # all authors
        select(Author)
        # join related objects
        .options(
            # "to one"
            joinedload(Author.user),
            # "to many"
            selectinload(Author.posts),
        )
        # sort
        .order_by(Author.id)
    )

    result: Result = await session.execute(authors_stmt)
    authors: Iterable[Author] = result.scalars().all()

    for author in authors:
        print("+", author)
        print("++", author.user)

        print("=== posts:")
        for post in author.posts:
            print("=", post)


async def create_tags(session: AsyncSession, *names: str) -> list[Tag]:
    tags = [Tag(name=name) for name in names]
    session.add_all(tags)
    await session.commit()
    print(tags)

    return tags


async def find_tags(session: AsyncSession, *names: str) -> list[Tag]:
    tags_stmt = (
        # tags
        select(Tag)
        # within these names
        .filter(func.lower(Tag.name).in_(names))
    )
    result: Result = await session.execute(tags_stmt)
    tags: list[Tag] = result.scalars().all()
    print("found tags", tags)

    return tags


async def create_post_with_tags(
    session: AsyncSession,
    author: Author,
    title: str,
    tags: Iterable[Tag],
) -> Post:
    post = Post(
        title=title,
        # author=author
        author_id=author.id,
        tags=tags,
    )
    session.add(post)
    await session.commit()

    print(post)
    print(post.tags)

    return post


async def auto_associate_tags_with_posts(session: AsyncSession):
    tags: Iterable[Tag] = (await session.execute(select(Tag))).scalars().all()

    posts_stmt = (
        select(Post)
        # joins
        .options(selectinload(Post.tags))
    )
    result_posts: Result = await session.execute(posts_stmt)
    posts: list[Post] = result_posts.scalars().all()

    for post in posts:
        title = post.title.lower()
        for tag in tags:
            if tag.name.lower() in title and tag not in post.tags:
                post.tags.append(tag)

    await session.commit()


async def find_posts_for_any_of_tags(
    session: AsyncSession, *tags_names: str
) -> Iterable[Post]:
    posts_stmt = (
        select(Post)
        .join(Post.tags)
        .filter(
            func.lower(Tag.name).in_(tags_names),
        )
        .options(
            joinedload(Post.author),
            selectinload(Post.tags),
        )
        .order_by(Post.title)
        .distinct()
    )
    result: Result = await session.execute(posts_stmt)
    posts: Iterable[Post] = result.scalars().all()

    for post in posts:
        print("---")
        print("post", post)
        print("author:", post.author)
        print("tags:", post.tags)

    return posts


async def find_posts_for_two_tags(
    session: AsyncSession, tag1: str, tag2: str
) -> list[Post]:
    table_tags1 = aliased(Tag, name="table_tags1")
    table_tags2 = aliased(Tag, name="table_tags2")
    # table_tags3 = aliased(Tag, name="table_tags2")
    posts_stmt = (
        select(Post)
        .join(table_tags1, Post.tags)
        .join(table_tags2, Post.tags)
        # .join(table_tags3, Post.tags)
        .filter(
            func.lower(table_tags1.name) == tag1,
            func.lower(table_tags2.name) == tag2,
            # func.lower(table_tags3.name) == tag3,
        )
        .options(selectinload(Post.tags))
        .order_by(Post.id)
    )

    result: Result = await session.execute(posts_stmt)
    posts: list[Post] = result.scalars().all()

    print("posts for both tags", tag1, tag2)

    for post in posts:
        print("---")
        print("post", post)
        print("tags:", post.tags)

    return posts


async def find_posts_for_all_of_tags(
    session: AsyncSession, *tags: str
) -> Iterable[Post]:
    posts_stmt = select(Post)

    tags_names = list(set(map(str.lower, tags)))
    filters = []

    for tag_name in tags_names:
        table = aliased(Tag, name=f"table_tags_{tag_name}")
        posts_stmt = posts_stmt.join(table, Post.tags)
        filters.append(
            func.lower(table.name) == tag_name,
        )

    posts_stmt = (
        # apply filters
        posts_stmt.filter(*filters)
        # add join options to select related
        .options(selectinload(Post.tags))
        # order
        .order_by(Post.id)
    )

    result: Result = await session.execute(posts_stmt)
    posts: list[Post] = result.scalars().all()

    print()
    print("posts for tags", tags)

    for post in posts:
        print("post", post)
        print("tags:", post.tags)
        print("---")

    return posts


async def find_posts_between_dates(
    session: AsyncSession,
    after_dt: datetime,
    before_dt: datetime,
) -> Iterable[Post]:
    posts_stmt = (
        select(Post)
        .filter(
            Post.created_at >= after_dt,
            Post.created_at <= before_dt,
        )
        .order_by(Post.created_at)
    )

    result: Result = await session.execute(posts_stmt)
    posts: list[Post] = result.scalars().all()

    for post in posts:
        print(post.title, post.created_at)

    return posts


async def find_posts_by_title(session: AsyncSession, *texts: str) -> Iterable[Post]:
    posts_stmt = (
        select(Post)
        .filter(or_(*(func.lower(Post.title).contains(text.lower()) for text in texts)))
        .order_by(Post.id)
    )

    result: Result = await session.execute(posts_stmt)
    posts = result.scalars().all()

    for post in posts:
        print("p", post)

    return posts


async def find_posts_with_tags_by_title(
    session: AsyncSession, *texts: str
) -> Iterable[Post]:
    posts_stmt = (
        select(Post)
        .filter(or_(*(func.lower(Post.title).contains(text.lower()) for text in texts)))
        .options(selectinload(Post.tags))
        .order_by(Post.id)
    )

    result: Result = await session.execute(posts_stmt)
    posts = result.scalars().all()

    for post in posts:
        print("p", post)

    return posts


# def find_tags(session: Session, *tag_names: str) -> Iterable[Tag]:
#     return session.query(Tag).filter(func.lower(Tag.name).in_(tag_names))


async def add_tags_to_posts(
    session: AsyncSession,
    posts: Iterable[Post],
    tags: Iterable[Tag],
):
    for post in posts:
        print("post", post, "tags", post.tags)
        for tag in tags:
            if tag not in post.tags:
                post.tags.append(tag)
                print("added tag", tag, "to post", post)

    await session.commit()


async def main():
    # async with async_session() as session:
    #         async with session.begin():
    async with async_session() as session:
        john: User = await create_user(session, username="john")
        sam: User = await create_user(session, username="sam")
        kate: User = await create_user(session, username="kate")
        alice: User = await create_user(session, username="alice")
        user_3: User | None = await get_user_by_id(session, 3)
        print("user 3", user_3)

        user_john: User = await get_user_by_username(session, "john")
        user_sam: User = await get_user_by_username(session, "sam")
        author_john: Author = await create_author(session, "John Smith", user=user_john)
        author_sam: Author = await create_author(session, "Sam White", user=user_sam)

        await show_users_with_authors(session)
        await show_authors_with_users(session)
        await show_users_only_with_authors(session)
        await update_users_emails_by_username(
            session,
            "@google.com",
            User.username == "kate",
        )

        await update_users_emails_by_username(
            session,
            "@yahoo.com",
            (func.length(User.username) == 4),
        )

        await find_authors_by_user_email_domain(session, "@yahoo.com")
        author_john: Author = await find_author_by_user_username(session, "john")
        await create_posts(session, author_john, "PyCharm News", "Python Tutorial")
        author_sam: Author = await find_author_by_user_username(session, "sam")
        await create_posts(session, author_sam, "Postgres news", "MySQL Tutorial")
        await show_users_with_author_and_posts(session)
        await show_authors_with_users_and_posts(session)

        await create_tags(session, "Python", "news", "lesson", "PyCharm")
        await create_tags(session, "MySQL", "tutorial")
        await create_tags(session, "database")

        posts: Iterable[Post] = await find_posts_by_title(session, "mysql", "postgres")
        posts: Iterable[Post] = await find_posts_with_tags_by_title(
            session,
            "mysql",
            "postgres",
        )
        tags = await find_tags(session, "database")
        await add_tags_to_posts(session, posts, tags)

        tags = await find_tags(session, "python", "news")
        await create_post_with_tags(session, author_john, "New Python Update", tags)
        await auto_associate_tags_with_posts(session)

        await find_posts_for_any_of_tags(session, "tutorial", "mysql", "database")
        await find_posts_for_any_of_tags(session, "qwerty")
        await find_posts_for_any_of_tags(session, "pycharm", "news")
        await find_posts_for_two_tags(session, "pycharm", "news")

        await find_posts_for_all_of_tags(session, "tutorial", "mysql", "database")
        await find_posts_for_all_of_tags(session, "tutorial")
        await find_posts_for_all_of_tags(session, "database")
        await find_posts_between_dates(
            session,
            after_dt=datetime(2023, 5, 22, 17, 58),
            before_dt=datetime(2023, 5, 22, 18),
        )


if __name__ == "__main__":
    asyncio.run(main())
