import asyncio
from datetime import datetime

import asyncpg
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, joinedload, selectinload

from blog_project.models import User, Author, Article


engine = create_async_engine(
    "postgresql+asyncpg://user:password@localhost:5432/blog_project",
    echo=True,
)

# expire_on_commit=False will prevent attributes from being expired
# after commit.
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def run_queries_asyncpg():
    conn = await asyncpg.connect(
        user="user",
        password="password",
        database="blog_project",
        host="127.0.0.1",
    )
    # conn = await asyncpg.connect(
    #     "postgresql://user:password@localhost:5432/blog_project",
    # )
    stmt = """
        INSERT INTO blog_users("username", "is_staff", "created_at")
        VALUES ($1, $2, $3);
        """
    result_insert = await conn.execute(
        stmt,
        "admin",
        True,
        datetime.now(),
    )
    print("result_insert", result_insert)
    admin_row = await conn.fetchrow(
        """SELECT * FROM blog_users WHERE username = $1""",
        "admin",
    )
    print("admin", admin_row)
    print("admin", admin_row["id"], "created at", admin_row["created_at"])

    await conn.close()


async def create_users_and_and_authors():

    async with async_session() as session:
        async with session.begin():
            sam_author = Author(name="Sam White", bio="I like docker")
            session.add_all(
                [
                    User(username="john", author=Author(name="John Smith", bio="I like Python")),
                    User(username="sam", author=sam_author),
                ]
            )


async def query_authors():
    stmt = select(User).options(joinedload(User.author))

    async with async_session() as session:
        result = await session.execute(stmt)

    for user in result.scalars():
        user: User
        print(user)
        print(f"username #{user.id} {user.username} created at: {user.created_at}")
        print("user author:", user.author)


async def create_articles():

    stmt_author_with_user = select(Author).join(Author.user)
    stmt_author_john = stmt_author_with_user.where(User.username == "john")
    stmt_author_sam = stmt_author_with_user.where(User.username == "sam")

    async with async_session() as session:
        author_john = (await session.execute(stmt_author_john)).scalars().first()
        author_sam = (await session.execute(stmt_author_sam)).scalars().first()

    article_1 = Article(
        title="Docker intro",
        body="Hello..",
        author=author_sam,
    )

    article_2 = Article(
        title="docker-compose intro",
        body="Hello again..",
        author=author_sam,
    )

    article_3 = Article(
        title="Python intro",
        body="Hello there..",
        author=author_john,
    )

    print(article_1)
    print(article_2)
    print(article_3)

    async with async_session() as session:
        async with session.begin():
            session.add_all(
                [
                    article_1,
                    article_2,
                    article_3,
                ]
            )

    print(article_1)
    print(article_2)
    print(article_3)


async def load_select_in():
    stmt = select(Author).options(joinedload(Author.user)).options(
        selectinload(Author.articles).selectinload(Article.tags))

    print(stmt)

    async with async_session() as session:
        result = await session.execute(stmt)

    for author in result.scalars():
        author: Author
        print("author", author, "user", author.user)
        print("-- articles:")
        for article in author.articles:
            article: Article
            print("article", article)
            print("tags", article.tags)


async def main():
    await run_queries_asyncpg()
    await create_users_and_and_authors()
    await query_authors()
    await create_articles()
    await load_select_in()

    # await asyncio.gather(
    #     load_select_in(),
    #     query_authors(),
    # )


if __name__ == '__main__':
    asyncio.run(main())
