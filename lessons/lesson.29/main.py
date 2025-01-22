from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload
from sqlalchemy.orm import joinedload

from models import engine, Author, Publication, Tag


def create_author(
    session: Session,
    name: str,
    email: str | None = None,
    bio: str = "",
) -> Author:
    author = Author(
        name=name,
        # email=email,
        bio=bio,
    )
    session.add(author)
    session.commit()
    return author


def create_publication(
    session: Session,
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
    session.commit()
    return publication


def create_entities(session: Session) -> None:
    bob: Author = create_author(
        session=session,
        name="Bob",
        email="bob@example.com",
    )
    sam: Author = create_author(
        session=session,
        name="Sam",
    )
    pub1: Publication = create_publication(
        session=session,
        title="PyCharm News",
        author_id=bob.id,
    )
    pub2: Publication = create_publication(
        session=session,
        title="PyCharm Tricks",
        author_id=bob.id,
    )
    john: Author = create_author(
        session=session,
        name="John",
        email="john@example.com",
    )
    pub3: Publication = create_publication(
        session=session,
        title="Python News",
        author_id=john.id,
    )
    pub4: Publication = create_publication(
        session=session,
        title="Python Tricks",
        author_id=john.id,
    )
    pub5: Publication = create_publication(
        session=session,
        title="Go Intro",
        author_id=john.id,
    )


def get_authors_with_publications(
    session: Session,
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

    authors = session.scalars(stmt).all()

    for author in authors:
        print("author:", author)
        print("author's publications:", author.publications)
        for publication in author.publications:
            print("+ publication:", publication)
    return list(authors)


def get_publications_with_authors(
    session: Session,
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

    publications = session.scalars(stmt).all()
    for pub in publications:
        print("Publication:", pub)
        print("- pub author:", pub.author)
    return list(publications)


def create_tags(
    session: Session,
    *tags_names: str,
) -> list[Tag]:
    tags = [Tag(name=name) for name in tags_names]
    session.add_all(tags)
    session.commit()
    print("Created tags:", tags)
    return tags


def get_all_tags(session: Session) -> list[Tag]:
    stmt = select(Tag).order_by(Tag.name)
    return list(session.scalars(stmt).all())


def get_all_publications_with_tags(session: Session) -> list[Publication]:
    stmt = (
        select(Publication)
        .options(
            selectinload(Publication.tags),
        )
        .order_by(Publication.id)
    )
    return list(session.scalars(stmt).all())


def auto_associate_tags_with_publications(
    session: Session,
) -> None:
    tags = get_all_tags(session)
    publications = get_all_publications_with_tags(session)

    for publication in publications:
        title_words = set[str](publication.title.lower().split())
        for tag in tags:
            if tag.name.lower() in title_words and tag not in publication.tags:
                publication.tags.append(tag)

    session.commit()


def example_remove_tag(session: Session) -> None:
    stmt = select(Publication).where(Publication.title.contains("Go")).limit(1)
    result = session.execute(stmt)
    publication: Publication = result.scalar_one()

    stmt_tag = select(Tag).where(Tag.name == "python")
    result = session.execute(stmt_tag)
    tag_python: Tag = result.scalar_one()

    publication.tags.append(tag_python)
    session.commit()
    print("saved association")

    publication.tags.remove(tag_python)
    session.commit()
    print("removed association")


def main() -> None:
    with Session(engine) as session:
        # create_entities(session)
        # create_tags(
        #     session,
        #     "news",
        #     "python",
        #     "PyCharm",
        #     "tricks",
        #     "Go",
        #     "intro",
        # )
        # authors = get_authors_with_publications(session)
        # print("authors:", authors)
        # publications = get_publications_with_authors(session)
        # print("publications:", publications)
        # auto_associate_tags_with_publications(session)
        pubs = get_all_publications_with_tags(session)
        for pub in pubs:
            print(pub)
            print("+++", [tag.name for tag in pub.tags])
            print("!", pub.tags)

        example_remove_tag(session)


if __name__ == "__main__":
    main()
