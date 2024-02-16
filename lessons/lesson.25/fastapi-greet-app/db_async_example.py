import asyncio
from typing import Sequence

from sqlalchemy import select, update
from sqlalchemy import and_
from sqlalchemy import func
from sqlalchemy import or_
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session, defer
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import selectinload

from models import User, Post, Tag

from config import DB_URL_ASYNC, DB_ECHO

async_engine = create_async_engine(
    DB_URL_ASYNC,
    echo=DB_ECHO,
)
async_session = async_sessionmaker(
    bind=async_engine,
    autocommit=False,
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
    session.add(user)
    await session.commit()

    print("saved user")
    print("user info:", user)
    # session.refresh(user)

    return user


async def create_users(
    session: AsyncSession,
    *usernames: str,
) -> list[User]:
    users = [
        # create new user
        User(username=username)
        # for each username
        for username in usernames
    ]
    session.add_all(users)
    await session.commit()
    print("saved users:", users)
    return users


async def get_user_by_primary_key(
    session: AsyncSession,
    pk: int,
) -> User | None:
    # user = session.get(User, pk)
    user = await session.get(User, pk)
    # session.refresh(user)
    print("user for pk", pk, "result:", user)
    return user


async def find_user_by_pk(
    session: AsyncSession,
    pk: int,
) -> User:
    stmt = select(User).where(
        User.id == pk,
        # User.id > 10,
    )
    # result = session.execute(stmt)
    # user = result.scalar()
    # user = session.scalar(stmt)
    result: Result = await session.execute(stmt)
    # user: User | None = result.scalar_one_or_none()
    # user: User = result.scalar_one()
    # user: User = result.scalars().first()
    user: User = result.scalar_one()
    print(user)
    return user


async def find_user_by_username(
    session: AsyncSession,
    username: str,
) -> User | None:
    stmt = select(User).where(User.username == username)
    # user: User | None = session.scalar(stmt)
    user: User | None = (await session.scalars(stmt)).one_or_none()
    print("user username", username, user)
    return user


async def search_users(
    session: AsyncSession,
) -> Sequence[User]:
    no_email_and_a_in_username_condition = and_(
        User.email.isnot(None),
        User.username.ilike("%a%"),
    )
    stmt = (
        select(User)
        .where(
            or_(
                User.username.ilike("%e"),
                no_email_and_a_in_username_condition,
            )
        )
        .order_by(User.id)
    )
    users = (await session.scalars(stmt)).all()

    for user in users:
        print(user)

    # print(list(users))
    return users


#


async def create_posts(
    session: AsyncSession,
    user: User,
    *posts_titles: str,
) -> list[Post]:
    posts = [
        # create a new post for this user
        Post(title=title, user_id=user.id)
        # for each title in titles
        for title in posts_titles
    ]
    session.add_all(posts)
    await session.commit()

    for post in posts:
        print(post)

    print(posts)

    return posts


async def show_posts_with_authors(
    session: AsyncSession,
):
    # N + 1
    # 1 - запрос на все посты
    # N - количество постов, количество подгрузок пользователей
    # stmt = select(Post).order_by(Post.id)

    # это не тот `.join` !!
    stmt = (
        # fetch all posts
        select(Post)
        # extra params for ORM
        .options(
            # join all authors to posts in SQL, for use in ORM. one query
            # joinedload(Post.author),
            # extra SQL request, for use in ORM. second query
            selectinload(Post.author)
        )
        # sort
        .order_by(Post.id)
    )

    posts = (await session.scalars(stmt)).all()
    for post in posts:  # type: Post
        print(post)
        print("+ author:", post.author)


async def show_users_with_posts(session: AsyncSession):
    stmt = (
        # all users
        select(User)
        # extra ORM options
        .options(
            # 'to many' - only selectinload
            selectinload(User.posts)
        )
        # sort
        .order_by(User.id)
    )

    users = (await session.scalars(stmt)).all()

    for user in users:  # type: User
        print(user)
        for post in user.posts:
            print("-", post)


async def show_all_posts_count(session: AsyncSession):
    stmt = select(func.count(Post.id))
    count: int = await session.scalar(stmt)
    print("posts count:", count)


async def show_users_posts_counts(session: AsyncSession):
    stmt = (
        # query
        select(
            # full user
            User,
            # count
            func.count(Post.id).label("posts_count"),
        )
        .join(
            User.posts,
            isouter=True,
        )
        .group_by(User.id)
        # sort
        .order_by(User.id)
    )
    result: Result = await session.execute(stmt)
    for user, posts_count in result.all():
        print(posts_count, "posts by user", user)


async def find_users_by_post_filter(session: AsyncSession):
    stmt = (
        select(User)
        .join(User.posts)
        # .where(
        #     Post.title.ilike("%intro%"),
        # )
        .group_by(User.id)
        .having(func.count(Post.id) > 1)
        .order_by(User.id)
    )
    users = (await session.scalars(stmt)).all()
    for user in users:
        print(user)


async def create_tags(
    session: AsyncSession,
    *tag_names: str,
) -> list[Tag]:
    tags = [
        # create a new post for this user
        Tag(name=name)
        # for each title in titles
        for name in tag_names
    ]
    session.add_all(tags)
    await session.commit()

    print(tags)

    return tags


async def auto_associate_posts_and_tags(
    session: AsyncSession,
):
    posts: Sequence[Post] = (
        #
        (
            await session.scalars(
                #
                select(Post)
                .options(
                    selectinload(Post.tags),
                )
                .order_by(Post.id)
            )
        ).all()
    )
    tags: Sequence[Tag] = (
        #
        (
            await session.scalars(
                #
                select(Tag).order_by(Tag.id)
            )
        ).all()
    )
    for post in posts:
        title = post.title.lower()
        for tag in tags:
            if (
                # check if post title matches tag
                tag.name.lower() in title
                # and if tag is not already associated
                and tag not in post.tags
            ):
                post.tags.append(tag)

    await session.commit()


async def semi_manual_associate_posts_and_tags(
    session: AsyncSession,
):
    # tag_lesson = session.execute(
    #     select(Tag).where(Tag.name == "lesson"),
    # ).scalar_one()
    tag_code_editors = (
        await session.execute(
            select(Tag).where(Tag.name == "code-editors"),
        )
    ).scalar_one()
    # tag_news = session.execute(
    #     select(Tag).where(Tag.name == "news"),
    # ).scalar_one()

    posts_editors = (
        await session.scalars(
            select(Post)
            .where(
                or_(
                    Post.title.icontains("vs code"),
                    Post.title.icontains("pycharm"),
                )
            )
            .options(selectinload(Post.tags))
        )
    ).all()
    for post in posts_editors:
        post.tags.append(tag_code_editors)

    await session.commit()


async def show_posts_with_tags(session: AsyncSession):
    posts = (
        await session.scalars(
            select(Post)
            .options(
                selectinload(Post.tags),
                defer(Post.created_at),
                # defer(...  # from tag)
            )
            .order_by(Post.id)
        )
    ).all()

    for post in posts:
        print("+ Post:")
        print(post.id, post.title)
        print("Tags:")
        for tag in post.tags:
            print("-", tag)


async def show_tags_with_posts(session: AsyncSession):
    tags = (
        await session.scalars(
            select(Tag)
            .options(
                selectinload(Tag.posts),
            )
            .order_by(Tag.id)
        )
    ).all()

    for tag in tags:
        print("+ Tag:", tag)
        for post in tag.posts:
            print("-", post.id, post.title)


async def show_posts_which_have_tag(
    session: AsyncSession,
    tag_name: str,
):
    stmt = (
        select(Post)
        .join(Post.tags)
        .where(
            Tag.name == tag_name,
        )
    )
    posts = (await session.scalars(stmt)).all()
    print("Next posts for tag", repr(tag_name))
    for post in posts:
        print("+ Post:", post.id, post.title)


async def show_users_with_posts_with_this_tag(
    session: AsyncSession,
    tag_name: str,
):
    stmt = (
        select(User)
        .join(User.posts)
        .join(Post.tags)
        .where(
            Tag.name == tag_name,
        )
        .group_by(User)
    )
    print("users with posts by tag", repr(tag_name))
    # users = session.scalars(stmt).unique().all()
    users: Sequence[User] = (await session.scalars(stmt)).all()
    for user in users:
        print(user)


async def main():
    async with async_session() as session:
        user: User = await create_user(
            session,
            "john",
        )
        user: User = await create_user(
            session,
            "sam",
            "sam@example.com",
        )

        users: list[User] = await create_users(
            session,
            "bob",
            "alice",
            "kate",
            "jack",
        )

        await get_user_by_primary_key(session, 0)
        await get_user_by_primary_key(session, 1)
        await get_user_by_primary_key(session, 3)
        await get_user_by_primary_key(session, 10)
        await find_user_by_pk(session, 1)
        await find_user_by_pk(session, 0)
        await find_user_by_username(session, "bob")
        await find_user_by_username(session, "sam")
        await find_user_by_username(session, "qwerty")
        bob, sam = await asyncio.gather(
            find_user_by_username(session, "bob"),
            find_user_by_username(session, "sam"),
        )
        print("bob:", bob)
        print("sam:", sam)
        await search_users(session)

        user_john: User = await find_user_by_username(session, "john")
        user_sam: User = await find_user_by_username(session, "sam")
        john_posts: list[Post] = await create_posts(
            session,
            user_john,
            "MySQL Lesson",
            "MS SQL Intro",
            "Postgres update review",
        )
        sam_posts: list[Post] = await create_posts(
            session,
            user_sam,
            "PyCharm recent release details",
            "VS Code tips and tricks",
        )
        await show_posts_with_authors(session)
        await show_users_with_posts(session)
        await show_all_posts_count(session)
        await show_users_posts_counts(session)
        await find_users_by_post_filter(session)

        await create_tags(
            session,
            "MySQL",
            "MS SQL",
            "Postgres",
            "lesson",
            "code-editors",
            "news",
        )
        await auto_associate_posts_and_tags(session)
        await semi_manual_associate_posts_and_tags(session)
        await show_posts_with_tags(session)
        await show_tags_with_posts(session)
        await show_posts_which_have_tag(session, "news")
        await show_users_with_posts_with_this_tag(session, "news")


if __name__ == "__main__":
    asyncio.run(main())
