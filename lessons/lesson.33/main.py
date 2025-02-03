import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload
from sqlalchemy.orm import joinedload

from models import Author, Publication, Tag
from models.db_sync import session_factory
from models.db_async import async_session_factory


async def create_author(
    session: AsyncSession,
    name: str,
    email: str | None = None,
    bio: str = "",
) -> Author:
    author = Author(
        name=name,
        email=email,
        bio=bio,
    )
    session.add(author)
    await session.commit()
    return author


async def create_publication(
    session: AsyncSession,
    title: str,
    author_id: int,
    body: str = "",
) -> Publication:
    publication = Publication(
        title=title,
        body=body,
        author_id=author_id,
    )
    session.add(publication)
    await session.commit()
    return publication


async def create_entities(session: AsyncSession) -> None:
    bob: Author = await create_author(
        session=session,
        name="Bob",
        email="bob@example.com",
    )
    sam: Author = await create_author(
        session=session,
        name="Sam",
    )
    # await session.refresh(sam)
    pub1: Publication = await create_publication(
        session=session,
        title="PyCharm News",
        author_id=bob.id,
    )
    pub2: Publication = await create_publication(
        session=session,
        title="PyCharm Tricks",
        author_id=bob.id,
    )
    john: Author = await create_author(
        session=session,
        name="John",
        email="john@example.com",
    )
    pub3: Publication = await create_publication(
        session=session,
        title="Python News",
        author_id=john.id,
    )
    pub4: Publication = await create_publication(
        session=session,
        title="Python Tricks",
        author_id=john.id,
    )
    pub5: Publication = await create_publication(
        session=session,
        title="Go Intro",
        author_id=john.id,
    )
    # print("Bob:", bob)
    # print("Sam:", sam)


async def get_authors_with_publications(
    session: AsyncSession,
) -> list[Author]:
    stmt = (
        # получить всех авторов
        select(Author)
        # join for ORM
        .options(
            # to many -> selectinload
            selectinload(Author.publications),
        )
        # всегда сортируем!
        .order_by(Author.id)
    )

    authors = (await session.scalars(stmt)).all()

    for author in authors:
        print("author:", author)
        print("author's publications:", author.publications)
        for publication in author.publications:
            print("+ publication:", publication)
    return list(authors)


async def get_publications_with_authors(
    session: AsyncSession,
) -> list[Publication]:
    stmt = (
        # берем все публикации
        select(Publication)
        # присоединяем для ORM
        .options(
            # to one -> joinedload
            joinedload(Publication.author)
        )
        # обязательно сортируем
        .order_by(Publication.title)
    )

    result = await session.scalars(stmt)
    publications = result.all()
    for pub in publications:
        print("Publication:", pub)
        print("- pub author:", pub.author)
    return list(publications)


async def create_tags(
    session: AsyncSession,
    *tags_names: str,
) -> list[Tag]:
    tags = [Tag(name=name) for name in tags_names]
    session.add_all(tags)
    await session.commit()
    print("Created tags:", tags)
    return tags


async def get_all_tags(session: AsyncSession) -> list[Tag]:
    stmt = select(Tag).order_by(Tag.name)
    result = await session.scalars(stmt)
    return list(result.all())


async def get_all_publications_with_tags(session: AsyncSession) -> list[Publication]:
    stmt = (
        select(Publication)
        .options(
            selectinload(Publication.tags),
        )
        .order_by(Publication.id)
    )
    result = await session.scalars(stmt)
    return list(result.all())


async def auto_associate_tags_with_publications(
    session: AsyncSession,
) -> None:
    tags = await get_all_tags(session)
    publications = await get_all_publications_with_tags(session)

    for publication in publications:
        title_words = set[str](publication.title.lower().split())
        for tag in tags:
            if tag.name.lower() in title_words and tag not in publication.tags:
                publication.tags.append(tag)

    await session.commit()


async def example_remove_tag(session: AsyncSession) -> None:
    stmt = select(Publication).where(Publication.title.contains("Go")).limit(1)
    result = await session.execute(stmt)
    publication: Publication = result.scalar_one()

    stmt_tag = select(Tag).where(Tag.name == "python")
    result = await session.execute(stmt_tag)
    tag_python: Tag = result.scalar_one()

    publication.tags.append(tag_python)
    await session.commit()
    print("saved association")

    publication.tags.remove(tag_python)
    await session.commit()
    print("removed association")


# def example_sync():
#     with session_factory() as session:
#         create_entities(session)


async def main() -> None:
    async with async_session_factory() as session:  # type: AsyncSession
        # await create_entities(session)
        await create_tags(
            session,
            "news",
            "python",
            "PyCharm",
            "tricks",
            "Go",
            "intro",
        )
        authors: list[Author] = await get_authors_with_publications(session)
        print("authors:", authors)
        publications: list[Publication] = await get_publications_with_authors(session)
        print("publications:", publications)
        await auto_associate_tags_with_publications(session)
        pubs: list[Publication] = await get_all_publications_with_tags(session)
        for pub in pubs:
            print(pub)
            print("+++", [tag.name for tag in pub.tags])
            print("!", pub.tags)

        await example_remove_tag(session)


if __name__ == "__main__":
    asyncio.run(main())
