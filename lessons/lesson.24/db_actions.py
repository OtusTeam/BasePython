import asyncio
from sqlalchemy import select, func
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import joinedload, selectinload, aliased

from models import Base, User, Author, Post, Tag

from models.db_async import async_engine, async_session


async def create_tables():
    async with async_engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(session: AsyncSession, username: str, is_staff=False) -> User:
    user = User(username=username, is_staff=is_staff)
    session.add(user)
    await session.commit()
    print("created user", user)
    return user


async def create_author(session: AsyncSession, name: str, user: User) -> User:
    author = Author(user=user, name=name)
    session.add(author)
    await session.commit()
    print("created author", author)
    return author


async def find_user(session: AsyncSession, username: str) -> User | None:
    stmnt = select(User).where(User.username == username)
    result: Result = await session.execute(stmnt)
    # print(result)
    # for i in result:
    #     print("i", i)
    # print("result.all()", result.all())
    # print("result.scalars().all()", result.scalars().all())
    # user = result.scalars().one()
    # user = result.scalar_one()
    user = result.scalar_one_or_none()
    print(user)

    return user


async def find_author_by_user_username(
    session: AsyncSession, user_name: str
) -> Author | None:
    stmnt = select(Author).join(Author.user).where(User.username == user_name)
    result: Result = await session.execute(stmnt)
    author = result.scalar_one_or_none()
    print("author for", user_name, author)
    return author


async def create_posts(
    session: AsyncSession, author: Author, *titles: str
) -> list[Post]:
    posts = [Post(author=author, title=title) for title in titles]
    session.add_all(posts)
    await session.commit()
    print(posts)
    return posts


async def get_posts_with_authors_and_users(session: AsyncSession) -> list[Post]:
    stmnt = select(Post).options(
        joinedload(Post.author).joinedload(Author.user),
    )
    result: Result = await session.execute(stmnt)
    posts = result.scalars().all()

    for post in posts:  # type: Post
        print("--", post)
        print("****", post.author)
        print("=====", post.author.user)

    return posts


async def get_authors_with_posts_and_user(session: AsyncSession) -> list[Author]:
    stmnt = (
        select(Author)
        .options(
            joinedload(Author.user),
            selectinload(Author.posts),
        )
        .order_by(Author.id)
    )
    result: Result = await session.execute(stmnt)
    authors = result.scalars().all()

    for author in authors:
        print("-", author)
        print("**", author.user)
        for post in author.posts:  # type: Post
            print("===", post)

    return authors


async def create_tags(session: AsyncSession, *names: str) -> list[Tag]:
    tags = [Tag(name=name) for name in names]
    session.add_all(tags)
    await session.commit()
    print(tags)
    return tags


async def auto_assign_tags_to_posts(session: AsyncSession) -> None:
    posts_stmt = select(Post).options(selectinload(Post.tags))
    tags_stmt = select(Tag).options()

    result_posts: Result = await session.execute(posts_stmt)
    posts: list[Post] = result_posts.scalars().all()

    result_tags: Result = await session.execute(tags_stmt)
    tags: list[Tag] = result_tags.scalars().all()

    for post in posts:
        post_title = post.title.lower()
        for tag in tags:
            if tag.name.lower() in post_title and tag not in post.tags:
                post.tags.append(tag)

    await session.commit()


async def find_users_by_tag_name(session: AsyncSession, tag_name: str) -> list[User]:
    users_stmt = (
        select(User)
        .join(User.author)
        .join(Author.posts)
        .join(Post.tags)
        .where(
            func.lower(Tag.name) == tag_name.lower(),
        )
    )
    result_users: Result = await session.execute(users_stmt)
    users = result_users.scalars().all()

    print("users for tag", tag_name, users)
    return users


async def find_posts_by_tags_names(
    session: AsyncSession, *tags_names: str
) -> list[Post]:
    posts_stmt = (
        select(Post)
        .join(Post.tags)
        # .join(Tag, Post.tags)
        .where(
            func.lower(Tag.name).in_(tags_names),
            # Tag.name.in_(tags_names),
        )
        .options(
            joinedload(Post.author),
            selectinload(Post.tags),
        )
        .order_by(Tag.name)
    )
    result_posts: Result = await session.execute(posts_stmt)
    posts = result_posts.scalars().all()

    print("posts for tags", tags_names)
    for post in posts:
        print("---", post)
        print("- author", post.author)
        print("* tags", post.tags)
    return posts


async def find_posts_by_all_tags(session: AsyncSession, *tags_names: str) -> list[Post]:
    posts_stmt = select(Post)
    tags_names = list(set(tags_names))
    filters = []
    for name in tags_names:
        tbl = aliased(Tag, name=f"table_tags_search_{name}")
        posts_stmt = posts_stmt.join(tbl, Post.tags)
        filters.append(func.lower(tbl.name) == name.lower())

    posts_stmt = posts_stmt.filter(*filters,).options(
        joinedload(Post.author),
        selectinload(Post.tags),
    )

    result_posts: Result = await session.execute(posts_stmt)
    posts = result_posts.scalars().all()

    print("posts for all tags", tags_names)
    if not posts:
        print("not found")
    for post in posts:
        print("---", post)
        print("- author", post.author)
        print("* tags", post.tags)
    return posts


async def main():
    async with async_session() as session:
        john = await create_user(session, "john")
        bob = await create_user(session, "bob")
        sam = await create_user(session, "sam")
        author_bob = await create_author(session, "bob", user=bob)
        sam = await find_user(session, "sam")
        bob = await find_user(session, "bob")
        john = await find_user(session, "john")
        author_john = await create_author(session, "John", user=john)
        author_sam = await create_author(session, "sam", user=sam)

        author_bob = await find_author_by_user_username(session, "bob")
        author_john = await find_author_by_user_username(session, "john")
        author_sam = await find_author_by_user_username(session, "sam")

        await create_posts(session, author_john, "PyCharm News", "Python News")
        await create_posts(session, author_john, "Golang Lesson")
        await create_posts(session, author_bob, "Lesson SQL", "Lesson PG")
        await create_posts(
            session, author_sam, "Python Django Lesson", "Python Flask Lesson"
        )

        await create_tags(session, "python", "pycharm", "sql", "pg", "news", "lesson")
        await create_tags(session, "golang", "django", "flask")

        await get_posts_with_authors_and_users(session)
        await get_authors_with_posts_and_user(session)

        await create_tags(session, "python", "pycharm", "sql", "pg", "news", "lesson")
        await create_tags(session, "golang", "django", "flask")
        await auto_assign_tags_to_posts(session)
        await find_users_by_tag_name(session, "news")
        await find_posts_by_tags_names(session, "news", "pg", "lesson")
        await find_posts_by_all_tags(session, "news", "pg")
        await find_posts_by_all_tags(session, "lesson", "python")


if __name__ == "__main__":
    # asyncio.run(create_tables())
    asyncio.run(main())
