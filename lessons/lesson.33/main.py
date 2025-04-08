import asyncio
from datetime import datetime

from sqlalchemy import (
    select,
)
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.orm import (
    Session,
    joinedload,
    selectinload,
    noload,
)

from models import (
    User,
    Article,
    Source,
)
from models.article_source import ArticleSource
from models.db_async import async_session


async def create_user(
    session: AsyncSession,
    username: str,
    email: str,
) -> User:
    user = User(
        username=username,
        email=email,
    )
    session.add(user)
    await session.commit()
    # await session.refresh(user)
    print("Created user:", user)
    return user


async def create_users(
    session: AsyncSession,
):
    bob = User(
        username="bob",
        email="bob@example.com",
    )
    alice = User(
        username="alice",
    )
    john = User(
        username="john",
        full_name="John Smith",
    )
    session.add(bob)
    await session.commit()

    session.add(alice)
    session.add(john)

    await session.commit()


async def fetch_user_by_username(
    session: AsyncSession,
    username: str,
) -> User:
    stmt = select(User).where(User.username == username)
    return (await session.execute(stmt)).scalar_one()


async def create_article(
    session: AsyncSession,
    user: User,
    title: str,
    body: str,
) -> None:
    article = Article(
        title=title,
        body=body,
        author_id=user.id,
    )
    session.add(article)
    await session.commit()


async def create_articles_for_users(
    session: AsyncSession,
):
    bob: User = await fetch_user_by_username(
        session=session,
        username="bob",
    )
    alice: User = await fetch_user_by_username(
        session=session,
        username="alice",
    )
    await create_article(
        session,
        bob,
        "The Future of Technology",
        "In this article, we explore the advancements in technology that are shaping our future. From AI to quantum computing, the possibilities are endless.",
    )
    await create_article(
        session,
        alice,
        "Healthy Living: Tips and Tricks",
        "This publication provides practical tips for maintaining a healthy lifestyle, including diet, exercise, and mental well-being.",
    )
    await create_article(
        session,
        alice,
        "Traveling the World: A Guide",
        "A comprehensive guide to traveling the world, covering the best destinations, travel tips, and cultural experiences.",
    )


async def create_new_articles(
    session: AsyncSession,
):
    articles = [
        Article(
            title="The Future of Tech: Innovations to Watch in 2023",
            body="As technology continues to evolve, several innovations are set to change the landscape in 2023. From AI advancements to new consumer gadgets, this article explores the trends that are shaping the future.",
            published_at=datetime(2023, 10, 5),
            author_id=1,
        ),
        Article(
            title="Understanding Global Politics: Key Events of 2023",
            body="This year has seen significant shifts in global politics, with major elections and international agreements. This article provides an overview of the key events that have shaped the political landscape.",
            published_at=datetime(2023, 10, 6),
            author_id=2,
        ),
        Article(
            title="The Ethics of AI: Balancing Innovation and Responsibility",
            body="As artificial intelligence becomes more integrated into our daily lives, ethical considerations are paramount. This article discusses the challenges and responsibilities that come with AI development.",
            published_at=datetime(2023, 10, 7),
            author_id=3,
        ),
    ]
    session.add_all(articles)
    await session.commit()


async def fetch_all_articles(
    session: AsyncSession,
) -> list[Article]:
    stmt = select(Article).order_by(Article.id)
    return list((await session.scalars(stmt)).all())


async def fetch_articles_with_authors(
    session: AsyncSession,
) -> list[Article]:
    stmt = (
        select(Article)
        .order_by(Article.id)
        .options(
            joinedload(Article.author),
        )
    )
    return list((await session.scalars(stmt)))


async def fetch_users_with_articles(
    session: AsyncSession,
) -> list[User]:
    stmt = (
        select(User)
        # .where(func.length(User.username) < 5)
        .order_by(User.id).options(
            selectinload(User.articles),
        )
    )
    return list((await session.scalars(stmt)))


async def show_articles_with_authors(
    session: AsyncSession,
):
    articles: list[Article] = await fetch_articles_with_authors(session)
    for article in articles:
        print(
            article.id,
            "-",
            article.title,
            "@",
            article.author,
            # repr(article.author),
            article.author.email,
        )


async def create_sources(
    session: AsyncSession,
):
    sources = [
        Source(
            name="TechCrunch: Latest Innovations in Technology",
            url="https://techcrunch.com/2023/10/01/latest-tech-news/",
        ),
        Source(
            name="BBC News: Global Politics and Current Affairs",
            url="https://www.bbc.com/news/world-63012345",
        ),
        Source(
            name="The Verge: In-Depth Gadget Reviews and Analysis",
            url="https://www.theverge.com/2023/10/02/new-gadget-reviews",
        ),
        Source(
            name="Wired: Exploring the Ethics of Artificial Intelligence",
            url="https://www.wired.com/story/2023/10/ai-ethics-discussion/",
        ),
        Source(
            name="Reuters: Daily Update on Global Financial Markets",
            url="https://www.reuters.com/business/2023/10/03/global-markets-update/",
        ),
    ]
    session.add_all(sources)
    await session.commit()


words_blacklist = frozenset(
    {
        "the",
        "on",
        "in",
        "of",
        "and",
        "or",
        "to",
    }
)


async def auto_associate_articles_with_plain_sources(
    session: AsyncSession,
):
    all_articles = (
        await session.scalars(
            select(Article).options(
                noload(
                    Article.sources,
                )
            )
        )
    ).all()

    all_sources = (
        await session.scalars(
            select(Source).options(
                noload(
                    Source.articles,
                )
            )
        )
    ).all()

    for article in all_articles:
        for source in all_sources:
            for word in article.title.lower().split():
                if (
                    # allwoed
                    word not in words_blacklist
                    # matches
                    and word in source.name.lower().replace(":", "").split()
                    # and not added already
                    and source not in article.sources
                ):
                    article.sources.append(source)
                    print("Added source", source, "to article", article)

    await session.commit()


async def get_articles_with_sources(
    session: AsyncSession,
) -> list[Article]:
    statement = (
        select(Article)
        .options(
            selectinload(Article.sources),
        )
        .order_by(Article.id)
    )
    return list((await session.scalars(statement)).all())


async def get_articles_with_sources_details(
    session: AsyncSession,
) -> list[Article]:
    statement = (
        select(Article)
        .options(
            selectinload(
                Article.source_associations,
            ).joinedload(ArticleSource.source)
        )
        .order_by(Article.id)
    )
    return list((await session.scalars(statement)).all())


async def get_sources_with_articles(
    session: AsyncSession,
) -> list[Source]:
    statement = (
        select(Source)
        .options(
            selectinload(Source.articles),
        )
        .order_by(Source.id)
    )
    return list((await session.scalars(statement)).all())


async def show_articles_with_sources(
    session: AsyncSession,
):
    articles: list[Article] = await get_articles_with_sources(session)
    for article in articles:
        print("+", article)
        for source in article.sources:
            print(" •", source)
        print("=====")


async def show_articles_with_sources_and_details(
    session: AsyncSession,
):
    articles: list[Article] = await get_articles_with_sources_details(session)
    for article in articles:
        print("+", article)
        for assoc in article.source_associations:
            print(f" • {assoc.details!r}", assoc.source)
        print("=====")


async def show_sources_with_articles(
    session: AsyncSession,
):
    sources: list[Source] = await get_sources_with_articles(session)
    for source in sources:
        print("+", source)
        for article in source.articles:
            print(" •", article)
        print("=====")


async def get_articles_and_all_sources() -> tuple[list[Article], list[Source]]:
    select_sources = select(Source).order_by(Source.id)
    async with (
        async_session() as session_a,
        async_session() as session_b,
    ):
        result_articles, result_sources = await asyncio.gather(
            fetch_all_articles(session_a),
            session_b.scalars(select_sources),
        )
    return result_articles, result_sources.all()


async def main():
    articles, sources = await get_articles_and_all_sources()

    for article in articles:
        print("+", article)
    print()
    for source in sources:
        print("-", source)

    async with async_session() as session:
        await create_user(
            username="jack",
            email="jack@example.com",
            session=session,
        )
        await create_users(session)
        # fail = fetch_user_by_username(
        #     session=session,
        #     username="fail",
        # )
        await create_articles_for_users(session)
        await create_sources(session)
        await create_new_articles(session)
        articles: list[Article] = await fetch_all_articles(session)
        await show_articles_with_authors(session)
        await show_articles_with_authors(session)
        users: list[User] = await fetch_users_with_articles(session)
        for user in users:
            print("Articles", user.id, user.username, user.email)
            for article in user.articles:
                print(" +", article.id, article.title)
            print("---")
        await auto_associate_articles_with_plain_sources(session)
        await show_articles_with_sources(session)
        await show_sources_with_articles(session)
        await show_articles_with_sources_and_details(session)


if __name__ == "__main__":
    asyncio.run(main())
