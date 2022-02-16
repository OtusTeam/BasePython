import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import noload, sessionmaker, joinedload, selectinload
from sqlalchemy.engine.result import Result

from blog_project import config
from blog_project.models import User, Author, Post, Tag
from blog_project.models.database import Base

engine = create_async_engine(
    config.SQLA_ASYNC_CONN_URI,
    echo=config.SQLA_ECHO,
)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def create_schemas():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(session: AsyncSession, username: str):
    user = User(username=username)
    print("create user", user)
    session.add(user)
    await session.commit()

    # async with session.begin():
    #     session.add(user)

    # only for demo!!
    print("saved user:", user)
    await session.refresh(user)
    print("refreshed user:", user)


async def get_user_by_id(session: AsyncSession, user_id: int):
    user = await session.get(User, user_id)
    print("found user", user, "by id", user_id)
    return user


async def create_author_for_user(
    session: AsyncSession,
    username: str,
    author_name: str,
):
    stmt = select(User).where(User.username == username)
    result: Result = await session.execute(stmt)
    # print("is Result type?", isinstance(result, Result))
    user = result.scalar_one()

    author = Author(
        name=author_name,
        user=user,
    )
    print("create author", author, "for user", user)
    session.add(user)
    await session.commit()


async def create_posts_for_user(
    session: AsyncSession,
    username: str,
    *posts_titles: str,
):
    stmt = select(Author).join(User).where(User.username == username)
    result: Result = await session.execute(stmt)
    author: Author = result.scalar_one()

    for posts_title in posts_titles:
        post = Post(
            title=posts_title,
            author=author,
        )
        print("create post", post, "for author", author, "and user with username", username)
        session.add(post)

    await session.commit()


async def create_tags(session: AsyncSession, *tags_names: str):
    tags = [
        Tag(name=name)
        for name in tags_names
    ]
    print("create tags", tags)

    session.add_all(tags)
    await session.commit()


async def create_posts_tags_associations(session: AsyncSession):
    stmt_tags = select(Tag)
    result: Result = await session.execute(stmt_tags)
    tags: list[Tag] = list(result.scalars())
    print("fetched tags", tags)

    stmt_posts = select(Post).options(noload(Post.tags))
    result: Result = await session.execute(stmt_posts)
    posts: list[Post] = result.scalars()

    # async with session.begin():
    for post in posts:
        print("* Process post", post, "with tags", post.tags)
        for tag in tags:
            if tag.name in post.title.lower():
                # # only if tags exist!!
                # for existing_tag in post.tags:
                #     if tag.id == existing_tag.id:
                #         break
                # else:
                #     post.tags.append(tag)
                post.tags.append(tag)
                print("Added tag", tag, "to post", post)

    await session.commit()


async def fetch_posts_with_tags(session: AsyncSession):
    # stmt_posts = select(Post).options(noload(Post.tags))
    stmt_posts = select(Post).options(selectinload(Post.tags))
    result: Result = await session.execute(stmt_posts)
    posts: list[Post] = result.scalars()

    for post in posts:
        print("* Post", post)
        print("post tags", post.tags)


async def fetch_posts_with_tags_and_authors(session: AsyncSession):
    stmt = (
        select(Post)
        .options(
            selectinload(Post.tags),
            joinedload(Post.author).joinedload(Author.user),
        )
    )
    result: Result = await session.execute(stmt)
    posts: list[Post] = result.scalars()

    for post in posts:
        print("* Post", post)
        print("- author", post.author)
        print("-- with user", post.author.user)
        print("post tags", post.tags)


async def main_async():
    """
    :return:
    """
    # await create_schemas()
    # session = async_session()
    async with async_session() as session:  # type: AsyncSession
        await create_user(session, "john")
        await create_user(session, "sam")
        await get_user_by_id(session, user_id=1)
        await get_user_by_id(session, user_id=5)
        await create_author_for_user(session, "john", "John Smith")
        await create_author_for_user(session, "sam", "Sam White")

        await create_posts_for_user(session, "john", "Lesson Django", "Lesson Flask")
        await create_posts_for_user(session, "sam", "Python News", "Lesson PyCharm")

        await create_tags(session, "news", "python", "django", "flask")
        await create_posts_tags_associations(session)
        await fetch_posts_with_tags(session)
        await fetch_posts_with_tags_and_authors(session)

    # await session.close()


def main():
    asyncio.run(main_async())


if __name__ == '__main__':
    main()

# if __name__ == "__main__":
#     if sys.platform == "win32":
#         asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#     asyncio.run(main())
