from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload
from sqlalchemy.orm import joinedload

from models import Base, engine, Author, Publication


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
        title="Pub 1",
        author_id=bob.id,
    )
    pub2: Publication = create_publication(
        session=session,
        title="Pub 2",
        author_id=bob.id,
    )
    john: Author = create_author(
        session=session,
        name="John",
        email="john@example.com",
    )
    pub: Publication = create_publication(
        session=session,
        title="John's Pub",
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


def main() -> None:
    with Session(engine) as session:
        # create_entities(session)
        authors = get_authors_with_publications(session)
        print("authors:", authors)
        publications = get_publications_with_authors(session)
        print("publications:", publications)


if __name__ == "__main__":
    main()
