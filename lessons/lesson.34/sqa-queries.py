import asyncio

from sqlalchemy import select, exists, func, text, Result, ScalarResult
from sqlalchemy.orm import Session, selectinload, joinedload, noload
from sqlalchemy.ext.asyncio import AsyncSession

from models import Base, engine, User, Post, Tag
from models.db_async import async_engine, async_session


async def example_sql(
    session: AsyncSession,
):
    res = await session.execute(text("SELECT 1;"))
    # print(res.all())
    # print(res.one())
    print(res.scalar())

    res = await session.execute(select(2))
    print(res.scalar())

    total = await session.execute(text("SELECT 1 + 2;"))
    print(total.scalar())

    total = await session.execute(select(text("3 + 4;")))
    print(total.scalar())


async def create_user(
    session: AsyncSession,
    name: str,
    username: str,
    email: str | None = None,
) -> User:
    user = User(
        name=name,
        username=username,
        email=email,
    )
    print("new user:", user)
    session.add(user)
    print("committing...")
    await session.commit()
    # await session.refresh(user)
    print("created a new user:", user)
    return user


async def create_users(
    session: AsyncSession,
    *names_and_usernames: tuple[str, str],
) -> list[User]:
    users = [
        User(
            name=name,
            username=username,
            email=f"{username}@site.com",
        )
        for name, username in names_and_usernames
    ]
    print("new users:", users)
    session.add_all(users)
    print("committing...")
    await session.commit()
    print("created new users:", users)
    return users


async def create_posts(
    session: AsyncSession,
    user,
    *titles: str,
) -> list[Post]:
    posts = [Post(title=title, user_id=user.id) for title in titles]
    print("new posts:", posts)
    session.add_all(posts)
    print("committing...")
    await session.commit()
    print("created new posts:", posts)
    return posts


async def create_tag(
    session: AsyncSession,
    name: str,
) -> Tag:
    tag = Tag(name=name)
    print("new tag:", tag)
    session.add(tag)
    print("committing...")
    await session.commit()
    print("created a new tag:", tag)
    return tag


async def create_tags(
    session: AsyncSession,
    *names: str,
) -> list[Tag]:
    tags = [Tag(name=name) for name in names]
    print("new tags:", tags)
    session.add_all(tags)
    print("committing...")
    await session.commit()
    print("created new tags:", tags)
    return tags


async def find_user(
    session: AsyncSession,
    username: str,
) -> User:
    statement = select(User).where(
        User.username == username,
    )
    # return session.scalar(statement)
    result = await session.execute(statement)
    return result.scalar_one()


async def get_users_with_posts(
    session: AsyncSession,
) -> list[User]:
    statement = (
        select(User)
        .options(
            selectinload(User.posts),
        )
        .order_by(User.id)
    )

    result = await session.scalars(statement)
    return list(result.all())


async def get_posts_with_all(
    session: AsyncSession,
) -> list[Post]:
    statement = (
        select(Post)
        .options(
            joinedload(Post.user),
            selectinload(Post.tags),
            # noload(Post.tags),
        )
        .order_by(Post.title)
    )
    result = await session.scalars(statement)
    return list(result.all())


async def get_users_by_post_title_match(
    session: AsyncSession,
    title_match: str,
) -> list[User]:
    # statement = (
    #     select(User)
    #     .join(Post)
    #     # .join(Post, Post.user_id == User.id)
    #     .where(
    #         Post.title.ilike(f"%{title_match}%"),
    #     )
    #     .order_by(User.id)
    # )
    # return list(session.scalars(statement).unique().all())

    statement = (
        select(User)
        .where(
            exists(1).where(
                Post.user_id == User.id,
                Post.title.ilike(f"%{title_match}%"),
            )
        )
        .order_by(User.id)
    )
    result = await session.scalars(statement)
    return list(result.all())


async def demo_create_users(
    session: AsyncSession,
):
    await create_user(
        session,
        name="Bob",
        username="bob",
        email="bob@example.com",
    )
    await create_user(
        session,
        name="Alice",
        username="alice",
        email="alice@example.com",
    )

    await create_users(
        session,
        ("Jack Black", "jack"),
        ("Kyle White", "kyle"),
        ("Nick Grey", "nick"),
    )


async def demo_create_posts(
    session: AsyncSession,
):
    bob: User = await find_user(session, "bob")
    await create_posts(
        session,
        bob,
        "Python Intro",
        "SQLAlchemy Intro",
        "Postgres tutorial",
    )
    alice: User = await find_user(session, "alice")
    await create_posts(
        session,
        alice,
        "JS Intro",
        "drizzle orm intro",
    )
    kyle: User = await find_user(session=session, username="kyle")
    await create_posts(session, kyle, "PyCharm Intro")
    users: list[User] = await get_users_with_posts(session)
    for user in users:
        print("==", user)
        print("** posts **")
        for post in user.posts:
            print("-", post.id, post.title)
        print()


async def demo_fetch_with_relationships(
    session: AsyncSession,
):
    posts: list[Post] = await get_posts_with_all(session)
    for post in posts:
        print("+", post.id, post.title)
        print("author:", post.user)
        print(" * Post tags:", post.tags)
        print()

    authors_intro = await get_users_by_post_title_match(
        session,
        "intro",
    )
    print("Intro authors:")
    for user in authors_intro:
        print("==", user)


async def get_posts_with_tags(
    session: AsyncSession,
) -> list[Post]:
    statement = select(Post).options(
        selectinload(Post.tags),
    )
    result = await session.scalars(statement)
    return list(result.all())


async def get_all_tags(
    session: AsyncSession,
):
    statement = select(Tag)
    result = await session.scalars(statement)
    return list(result.all())


async def auto_associate_posts_with_tags(
    session: AsyncSession,
):
    posts = await get_posts_with_tags(session)
    tags = await get_all_tags(session)
    tags_map = {tag.name.lower(): tag for tag in tags}
    for post in posts:
        post_title = post.title.lower()
        for word in post_title.split():
            if word.lower() not in tags_map:
                new_tag: Tag = await create_tag(session, word)
                tags_map[word.lower()] = new_tag
            tag = tags_map[word.lower()]
            if tag not in post.tags:
                post.tags.append(tag)
                print("Added tag", tag, "to post", post)

    await session.commit()


async def fetch_posts_has_tag(
    session: AsyncSession,
    tag_name: str,
) -> list[Post]:
    statement = (
        select(Post)
        .join(
            Post.tags,
        )
        .where(
            func.lower(Tag.name) == tag_name.lower(),
        )
        .options(
            selectinload(Post.tags),
        )
        .order_by(Post.title)
    )

    result: ScalarResult[Post] = await session.scalars(statement)
    return list(result.all())


async def main():
    # async with async_engine.connect() as conn:
    #     await conn.run_sync(Base.metadata.create_all)

    # with Session(engine, expire_on_commit=False) as session:
    # with Session(engine) as session:
    async with async_session() as session:
        await example_sql(session)
        await demo_create_users(session)
        await demo_create_posts(session)
        await demo_fetch_with_relationships(session)

        await create_tags(
            session,
            "python",
            "js",
            "Postgres",
        )
        await auto_associate_posts_with_tags(session)
        await demo_fetch_with_relationships(session)

        posts: list[Post] = await fetch_posts_has_tag(session, "intro")
        for post in posts:
            print("+", post.id, post.title)
            print(" * Post tags:", post.tags)
            print()


if __name__ == "__main__":
    asyncio.run(main())
