import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import joinedload, selectinload, sessionmaker

from blog_app.models import Base, User, Post, Tag


engine = create_async_engine(
    "postgresql+asyncpg://user:password@localhost/blog_app",
    echo=True,
)

# expire_on_commit=False will prevent attributes from being expired
# after commit.
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def create_tables():
    """
    If we aren't using alembic
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_admin_user():
    user = User(username="admin", is_staff=True)

    async with async_session() as session:  # type: AsyncSession
        # session.add(user)
        # await session.commit()
        async with session.begin():
            session.add(user)


async def get_user_by_pk():
    user_id = 1
    async with async_session() as session:  # type: AsyncSession
        user = await session.get(User, user_id)
        print(user)


async def create_some_users():
    user_sam = User(username="sam")

    async with async_session() as session:  # type: AsyncSession
        async with session.begin():
            session.add_all([
                user_sam,
                User(username="john"),
            ])

    print("user_sam", user_sam)


async def create_posts_for_users():
    # stmt_q_users = select(User)
    stmt_user_sam = select(User).where(User.username == "sam")
    stmt_user_john = select(User).where(User.username == "john")

    async with async_session() as session:  # type: AsyncSession
        async with session.begin():
            user_sam = (await session.execute(stmt_user_sam)).scalar_one_or_none()
            user_john = (await session.execute(stmt_user_john)).scalar_one_or_none()

            print(user_sam)
            print(user_john)

            # noinspection PyArgumentList
            post_django = Post(
                title="Django lesson",
                body="Hello Django..",
                author=user_john,
            )

            post_news = Post(
                title="Python news",
                body="Hello Python news..",
                author=user_sam,
            )

            # noinspection PyArgumentList
            session.add_all([
                Post(title="Flask lesson", body="Hello Flask..", author=user_sam),
                post_django,
                post_news,
            ])

    print(post_django.id, post_django.title, post_django.author)
    print(post_news.id, post_news.title, post_news.author)


async def fetch_posts_with_authors():
    stmt = select(Post).options(joinedload(Post.author)).order_by(Post.id)
    async with async_session() as session:  # type: AsyncSession
        result = await session.execute(stmt)

    # select users by ids
    # stmt = select(User).where(User.id.in_([1, 3, 5, 7]))

    for post in result.scalars():  # type: Post
        print("Post", post.id, post.title, post.author)


async def fetch_users_with_posts():
    stmt_users_with_posts = (
        select(User)
        .options(selectinload(User.posts))
        .order_by(User.id)
    )

    print("stmt_users_with_posts", stmt_users_with_posts)
    async with async_session() as session:  # type: AsyncSession
        result = await session.execute(stmt_users_with_posts)

    for user in result.scalars():  # type: User
        print(user)
        for post in user.posts:
            print("--", post.id, post.title)


async def create_tags():
    tag1 = Tag(name="news")
    tag2 = Tag(name="python")
    tag3 = Tag(name="flask")
    tag4 = Tag(name="django")

    # users_data = [{"user_id": 1, "username": "sam"}, {"user_id": 2, "username": "john"}]
    #
    # users = [
    #     User(id=data["user_id"], username=data["username"])
    #     for data in users_data
    # ]
    async with async_session() as session:  # type: AsyncSession
        async with session.begin():
            # session.add_all(users)
            session.add_all([
                tag1,
                tag2,
                tag3,
                tag4,
            ])

    print(
        tag1,
        tag2,
        tag3,
        tag4,
    )


async def add_tags_posts():
    async with async_session() as session:  # type: AsyncSession
        async with session.begin():
            tags = (await session.execute(select(Tag))).scalars()
            tags_map = {tag.name: tag for tag in tags}
            print("tags map", tags_map)
            stmt_posts = select(Post).options(selectinload(Post.tags))
            posts = (await session.execute(stmt_posts)).scalars()
            for post in posts:  # type: Post
                post_title = post.title.lower()
                for name, tag in tags_map.items():
                    if name in post_title:
                        post.tags.append(tag)
                        print("Added tag", tag, "to post", post.id, post.title)


async def fetch_posts_with_authors_and_tags():
    stmt = (
        select(Post)
        .options(joinedload(Post.author))
        .options(selectinload(Post.tags))
        .order_by(Post.id)
    )
    async with async_session() as session:  # type: AsyncSession
        result = await session.execute(stmt)

    for post in result.scalars():  # type: Post
        print("post #", post.id, post.title, "with author", post.author)
        print("post tags:", post.tags)


async def main_async():
    await create_admin_user()
    await get_user_by_pk()
    await create_some_users()
    await create_posts_for_users()
    await fetch_posts_with_authors()
    await fetch_users_with_posts()
    await create_tags()
    await add_tags_posts()
    await fetch_posts_with_authors_and_tags()


def main():
    asyncio.run(main_async())


if __name__ == '__main__':
    main()
