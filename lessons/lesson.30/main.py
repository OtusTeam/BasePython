import asyncio
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from models.db_async import async_engine, async_session
from models import (
    Base,
    engine,
    Author,
    Publication,
    Tag,
)


async def create_author(
    session: AsyncSession,
    name: str,
    username: str,
    email: str | None = None,
) -> Author:
    author = Author(name=name, username=username, email=email)
    session.add(author)
    await session.commit()
    return author


async def create_one_publication(
    session: AsyncSession,
    author: Author,
    title: str,
    body: str = "",
) -> Publication:
    publication = Publication(
        author=author,
        title=title,
        body=body,
    )
    session.add(publication)
    await session.commit()
    return publication


async def create_publications(
    session: AsyncSession,
    author: Author,
    *titles: str,
) -> list[Publication]:
    publications = [
        Publication(
            author=author,
            title=title,
        )
        for title in titles
    ]
    session.add_all(publications)
    await session.commit()
    return publications


async def create_entities(
    session: AsyncSession,
) -> None:
    bob: Author = await create_author(
        session=session,
        name="Bob",
        username="bob",
        email="bob@example.com",
    )
    print("New author:", bob)

    python_intro_publication: Publication = await create_one_publication(
        session=session,
        author=bob,
        title="Python Intro Publication",
        body="This is a Python intro publication",
    )
    print("Publication:", python_intro_publication)

    publications: Sequence[Publication] = await create_publications(
        session,
        bob,
        "SQL Intro",
        "SQLAlchemy Intro",
        "SQL Relationships Intro",
    )
    print("Publications:", publications)

    john: Author = await create_author(
        session=session,
        name="John",
        username="john",
    )
    print("New author:", john)
    sam: Author = await create_author(
        session=session,
        name="Sam",
        username="sam",
    )
    print("New author:", sam)

    publications: Sequence[Publication] = await create_publications(
        session,
        sam,
        "Python Intro",
        "Go intro",
    )
    print("Publications:", publications)


async def get_author(
    session: AsyncSession,
    username: str,
) -> Author | None:
    stmt = select(Author).where(Author.username == username)
    author: Author | None = await session.scalar(stmt)
    print(f"fetched author by username {username!r}: {author}")
    return author


async def fetch_authors(session: AsyncSession) -> Sequence[Author]:
    # return session.query(Author).all()
    stmt = select(Author).order_by(Author.id)
    result = await session.execute(stmt)
    return result.scalars().all()


async def fetch_authors_with_publications(
    session: AsyncSession,
) -> Sequence[Author]:
    stmt = (
        select(Author)
        .options(
            # joinedload(Author.publications)
            selectinload(Author.publications)
        )
        .order_by(Author.id)
    )
    # return session.execute(stmt).unique().scalars().all()
    # return (await session.execute(stmt)).scalars().all()
    # return (
    #     # open
    #     await session.scalars(
    #         # open
    #         stmt
    #     # close
    #     )
    # # close
    # ).all()
    return (await session.scalars(stmt)).all()


async def fetch_publications_with_authors(
    session: AsyncSession,
) -> Sequence[Publication]:
    stmt = (
        select(Publication)
        .options(
            # selectinload(Publication.author)
            joinedload(Publication.author)
        )
        .order_by(Publication.id)
    )
    result = await session.execute(stmt)
    return result.scalars().all()


async def fetch_publications_with_tags(
    session: AsyncSession,
) -> Sequence[Publication]:
    stmt = (
        select(Publication)
        .options(
            selectinload(Publication.tags),
        )
        .order_by(Publication.id)
    )
    result = await session.execute(stmt)
    return result.scalars().all()


async def create_tag(
    session: AsyncSession,
    name: str,
) -> Tag:
    tag = Tag(name=name)
    session.add(tag)
    await session.commit()
    return tag


async def fetch_tags(session: AsyncSession) -> Sequence[Tag]:
    stmt = select(Tag).order_by(Tag.id)
    return (await session.scalars(stmt)).all()


async def example_create_publication_with_tags(session: AsyncSession) -> Publication:
    tags = await fetch_tags(session)
    bob = await get_author(session, username="bob")
    publication = await create_one_publication(session, bob, title="Another HowTo")
    print("created publication:", publication)
    await session.refresh(publication, ("tags",))
    print("publication's tags:", publication.tags)

    publication.tags.extend(tags)
    print("publication's tags before commit:", publication.tags)
    await session.commit()
    print("publication's tags after commit:", publication.tags)
    return publication


async def main():
    async with async_session() as session:  # type: AsyncSession
        await create_entities(session)
        bob: Author = await get_author(session, username="bob")
        ken: Author = await get_author(session, username="ken")

        # authors = fetch_authors(session)
        authors: Sequence[Author] = await fetch_authors_with_publications(session)
        for author in authors:
            print(author)
            if author.publications:
                print(f"{author.name}'s publications:")
            else:
                print(author.name, "has no publications")

            for pub in author.publications:
                print("-", pub)

        publications = await fetch_publications_with_authors(session)
        for publication in publications:
            print(publication, "by", publication.author)

        await create_author(session, name="Will", username="will")
        tag_spam: Tag = await create_tag(session, "spam")
        tag_eggs: Tag = await create_tag(session, "eggs")
        # print("Tags:", [tag_spam, tag_eggs])
        await example_create_publication_with_tags(session)
        pubs = await fetch_publications_with_tags(session)
        for pub in pubs:
            print("+++", pub)
            print(pub.tags)
            for tag in pub.tags:
                if tag.name == "spam":
                    pub.tags.remove(tag)

        await session.commit()


if __name__ == "__main__":
    asyncio.run(main())
