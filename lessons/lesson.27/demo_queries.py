import asyncio
from collections.abc import Sequence

from sqlalchemy import desc
from sqlalchemy import distinct
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.orm import aliased
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from models import (
    async_engine,
    async_session,
    Base,
    User,
    Post,
    Tag,
)


async def create_tables():
    # Base.metadata.drop_all(bind=engine)
    # print("Creating tables...", Base.metadata.tables)
    # Base.metadata.create_all(bind=engine)
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def create_user(
    session: AsyncSession,
    username: str,
    email: str | None = None,
) -> User:
    user = User(username=username, email=email)
    session.add(user)

    await session.commit()
    # await session.refresh(user)

    print("user created:", user)
    return user


async def create_post(
    session: AsyncSession,
    title: str,
    user_id: int,
) -> Post:
    post = Post(title=title, user_id=user_id)
    # post.author = user
    session.add(post)
    await session.commit()
    print("post created:", post)
    return post


async def create_users(
    session: AsyncSession,
    *usernames: str,
) -> Sequence[User]:
    users = [User(username=username) for username in usernames]
    session.add_all(users)
    print("prepared users:", users)

    await session.commit()

    print("saved users:", users)
    return users


async def create_posts(
    session: AsyncSession,
    *titles: str,
    user_id: int,
) -> Sequence[Post]:
    posts = [Post(title=title, user_id=user_id) for title in titles]
    session.add_all(posts)
    print("prepared posts:", posts)
    await session.commit()
    print("saved posts:", posts)
    return posts


async def create_tags(
    session: AsyncSession,
    *names: str,
) -> Sequence[Tag]:
    tags = [Tag(name=name) for name in names]
    session.add_all(tags)
    print("prepared tags:", tags)
    await session.commit()
    print("saved tags:", tags)
    return tags


async def fetch_all_users(session: AsyncSession) -> Sequence[User]:
    # stmt = select(User).order_by(User.id)
    stmt = select(User).order_by(desc(User.username))
    # result = session.execute(stmt)
    # users = result.scalars().all()
    result = await session.scalars(stmt)
    users = result.all()
    print("users:", users)
    return users


async def fetch_users_with_posts(
    session: AsyncSession,
) -> Sequence[User]:
    stmt = (
        select(User)
        .options(
            # joinedload(User.posts),
            selectinload(User.posts),
        )
        .order_by(User.id)
    )

    print("load users w/ posts:")
    # users = session.scalars(stmt).unique().all()
    result = await session.scalars(stmt)
    users = result.all()
    for user in users:
        print("+", user)
        for post in user.posts:
            print("  -", post)

    return users


async def fetch_all_posts(session: AsyncSession) -> Sequence[Post]:
    stmt = select(Post).order_by(Post.id)
    # result = session.execute(stmt)
    # posts = result.scalars().all()
    result = await session.scalars(stmt)
    posts = result.all()
    print("posts:", posts)
    return posts


async def fetch_all_tags(session: AsyncSession) -> Sequence[Tag]:
    stmt = select(Tag).order_by(Tag.id)
    result = await session.scalars(stmt)
    tags = result.all()
    print("tags:", tags)
    return tags


async def fetch_all_tags_with_posts(session: AsyncSession) -> Sequence[Tag]:
    stmt = (
        select(Tag)
        .options(
            selectinload(Tag.posts),
        )
        .order_by(Tag.id)
    )
    result = await session.scalars(stmt)
    tags = result.all()
    return tags


async def fetch_all_posts_with_authors(
    session: AsyncSession,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .options(
            joinedload(Post.author),
        )
        .order_by(Post.id)
    )
    result = await session.scalars(stmt)
    posts = result.all()
    print("posts:", posts)

    for post in posts:
        print("+", post)
        print("= author:", post.author)

    return posts


async def fetch_all_posts_with_tags(
    session: AsyncSession,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .options(
            selectinload(Post.tags),
        )
        .order_by(Post.id)
    )
    result = await session.scalars(stmt)
    posts = result.all()
    return posts


async def fetch_all_posts_with_tags_where_tag_is_present(
    session: AsyncSession,
    tag_name: str,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .join(Post.tags)
        .where(func.lower(Tag.name) == tag_name.lower())
        .options(
            selectinload(Post.tags),
        )
        .order_by(Post.id)
    )
    result = await session.scalars(stmt)
    posts = result.all()
    return posts


async def fetch_user_by_username(
    session: AsyncSession,
    username: str,
) -> User | None:
    stmt = select(User).where(User.username == username)
    # result = session.execute(stmt)
    # user = result.scalars().one_or_none()
    result = await session.scalars(stmt)
    user: User | None = result.one_or_none()
    print("user for username", repr(username), "result:", user)
    return user


SQL = """
UPDATE users 
SET email=concat(
    lower(users.username), 
    '@ya.ru'::VARCHAR
)
WHERE users.email IS NULL 
    AND length(users.username) < 5::INTEGER;
"""


async def set_emails_for_null_email_users_with_username_limit(
    session: AsyncSession,
    username_size_limit: int,
    domain: str,
):
    """

    :param session:
    :param username_size_limit:
    :param domain: example: '@ya.ru'
    :return:
    """

    new_email = func.concat(
        func.lower(User.username),
        domain.lower(),
    )
    stmt = (
        update(User)
        .where(
            # empty email
            User.email.is_(None),
            # username len limit
            func.length(User.username) < username_size_limit,
        )
        .values(
            {
                User.email: new_email,
            }
        )
    )

    await session.execute(stmt)
    await session.commit()


"""
SQL:
SELECT ('a', 'b');

python:
result all: [('a', 'b'),]
result first: ('a', 'b')

SQL:
SELECT (42);

python 
result all: [(42, ),]
result first: (42, )

result all: [(42, ), (7, ), ]

python scalars
result scalars all: [42, 7,]
result scalar first: 42


SELECT ( {tag.id, tag.name} )

python
result all: [ (Tag(id=1, name='...'), ), (Tag(id=2, name='...'), ), ]
result scalars all: [ Tag(id=1, name='...'), Tag(id=2, name='...'), ]
result first: ( Tag(id=1, name='...'), )
result scalar first: Tag(id=1, name='...')


SELECT ( {user.id, user.username}, count )
group by ...

python
result all [ (User(...), count, ), (User(...), count, ) ]
result first (User(...), count, )
"""


async def select_top_users_with_posts_sorted(
    session: AsyncSession,
) -> None:
    users_w_posts_count_stmt = (
        select(User, func.count(Post.id).label("posts_count"))
        .join(User.posts, isouter=True)
        .group_by(User.id)
        .order_by(func.count(Post.id).desc(), User.username)
    )
    result = await session.execute(users_w_posts_count_stmt)
    result = result.all()
    for user, posts_count in result:
        print("+ user", user.id, user.username, "w/", posts_count, "posts")


async def create_tags_based_on_posts_titles(
    session: AsyncSession,
) -> Sequence[Tag]:
    posts = await fetch_all_posts(session)
    known_tags = await fetch_all_tags(session)
    known_tags_names: set[str] = {tag.name.lower() for tag in known_tags}

    new_tags_names: set[str] = set()
    for post in posts:
        parts = post.title.lower().strip().split()
        new_tags_names.update(parts)

    new_tags_names.difference_update(known_tags_names)
    tags = await create_tags(session, *new_tags_names)
    return tags


async def auto_associate_tags_with_posts(session: AsyncSession) -> None:
    posts = await fetch_all_posts_with_tags(session)
    tags = await fetch_all_tags(session)

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
        .where(func.lower(Tag.name) == tag_name.lower())
        .order_by(User.id)
    )
    result = await session.scalars(stmt)
    users = result.unique().all()
    print("users who used tag", repr(tag_name), "in posts:")
    for user in users:
        print("+", user)

    return users


async def get_users_with_posts_with_tag_using_subquery(
    session: AsyncSession,
    tag_name: str,
) -> Sequence[User]:

    stmt_users_ids_for_posts_with_tag = (
        select(distinct(Post.user_id))
        .join(Post.tags)
        .where(func.lower(Tag.name) == tag_name.lower())
    )
    # print(session.execute(stmt_users_ids_for_posts_with_tag).all())
    stmt = (
        select(User)
        .where(
            User.id.in_(
                select(stmt_users_ids_for_posts_with_tag.subquery()),
            )
        )
        .order_by(User.id)
    )
    result = await session.scalars(stmt)
    users = result.all()
    print("users who used tag", repr(tag_name), "in posts:")
    for user in users:
        print("+", user)

    return users


async def show_posts_with_one_of_tags(
    session: AsyncSession,
    *tags_names: str,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .join(Post.tags)
        .where(func.lower(Tag.name).in_([name.lower() for name in tags_names]))
        .options(selectinload(Post.tags))
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
            func.lower(table_tags1.name) == t1_name.lower(),
            func.lower(table_tags2.name) == t2_name.lower(),
        )
        .options(selectinload(Post.tags))
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
        filters.append(func.lower(table_tags.name) == tag_name)

    stmt = (
        stmt.where(
            *filters,
        )
        .options(selectinload(Post.tags))
        .order_by(Post.id)
    )
    posts = await session.scalars(stmt)
    return posts.unique().all()


async def main():
    # await create_tables()
    async with async_session() as session:
        # await create_user(session, username="admin", email="admin@admin.com")
        # bob: User = await create_user(session, username="bob", email=None)
        # john: User = await create_user(session, username="john", email=None)
        # greg: User = await create_user(session, username="greg", email=None)
        # post_pg: Post = await create_post(
        #     session=session,
        #     title="PostgreSQL news",
        #     user_id=greg.id,
        # )
        # print("post pg:", post_pg)
        # await create_users(session, "nick", "alice")
        # sam: User = await create_user(session, username="sam", email=None)
        # josh: User = await create_user(session, username="josh", email=None)
        # await create_posts(
        #     session,
        #     "MySQL Intro",
        #     "MariaDB SQL Lesson",
        #     user_id=sam.id,
        # )
        # await create_posts(
        #     session,
        #     "Python Intro",
        #     "Python Lesson",
        #     "Python decorators",
        #     user_id=josh.id,
        # )

        # await create_users(session, "pete", "jenn", "marco")
        # await create_users(session, "kyle", "james", "kate")
        #
        # await fetch_all_users(session)
        # await fetch_users_with_posts(session)

        # posts = await fetch_all_posts(session)
        #
        # for post in posts:
        #     print("+", post)

        await fetch_all_posts_with_authors(session)
        # posts: Sequence[Post] = await fetch_all_posts_with_authors(session)

        # for post in posts:
        #     print("+", post)
        #     print("= author:", post.author)

        # await create_tags(session, "news", "postgres", "python", "sql", "lesson")

        await create_tags_based_on_posts_titles(session)
        await auto_associate_tags_with_posts(session)
        posts: Sequence[Post] = await fetch_all_posts_with_tags(session)
        for post in posts:
            print("+", post)
            for t in post.tags:
                print(" *", t.name)

        posts: Sequence[Post] = await fetch_all_posts_with_tags_where_tag_is_present(
            session, tag_name="sql"
        )

        for post in posts:
            print("+", post)
            for t in post.tags:
                print(" *", t.name)

        tags_with_posts: Sequence[Tag] = await fetch_all_tags_with_posts(session)
        for tag in tags_with_posts:
            print("+", tag)
            for post in tag.posts:
                print(" | ", post.id, post.title)

        await get_users_with_posts_with_tag(session, "sql")
        await get_users_with_posts_with_tag_using_subquery(session, "sql")
        posts = await show_posts_with_one_of_tags(session, "sql", "Python")
        posts = await show_posts_with_two_tags(session, "lesson", "Python")
        posts = await show_posts_with_all_tags(session, "postgres", "sql", "news")
        for post in posts:
            print("+", post)
            for t in post.tags:
                print(" *", t.name)

        posts = await fetch_all_posts(session)
        await fetch_all_posts_with_authors(session)

        for post in posts:
            print("+", post)
            print("= author:", post.author)


if __name__ == "__main__":
    asyncio.run(main())
