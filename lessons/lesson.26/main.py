from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload, selectinload

from models import Base, engine, Author, Publication


def create_author(
    session: Session,
    name: str,
    username: str,
    email: str | None = None,
) -> Author:
    author = Author(name=name, username=username, email=email)
    session.add(author)
    session.commit()
    return author


def create_one_publication(
    session: Session,
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
    session.commit()
    return publication


def create_publications(
    session: Session,
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
    session.commit()
    return publications


def create_entities(
    session: Session,
) -> None:
    bob = create_author(
        session=session,
        name="Bob",
        username="bob",
        email="bob@example.com",
    )
    print("New author:", bob)

    python_intro_publication = create_one_publication(
        session=session,
        author=bob,
        title="Python Intro Publication",
        body="This is a Python intro publication",
    )
    print("Publication:", python_intro_publication)

    publications = create_publications(
        session,
        bob,
        "SQL Intro",
        "SQLAlchemy Intro",
        "SQL Relationships Intro",
    )
    print("Publications:", publications)

    john = create_author(
        session=session,
        name="John",
        username="john",
    )
    print("New author:", john)
    sam = create_author(
        session=session,
        name="Sam",
        username="sam",
    )
    print("New author:", sam)

    publications = create_publications(
        session,
        sam,
        "Python Intro",
        "Go intro",
    )
    print("Publications:", publications)


def get_author(
    session: Session,
    username: str,
) -> Author | None:
    stmt = (
        select(Author)
        .where(Author.username == username)
    )
    author: Author | None = session.scalar(stmt)
    print(f"fetched author by username {username!r}: {author}")
    return author


def fetch_authors(session: Session) -> Sequence[Author]:
    # return session.query(Author).all()
    stmt = select(Author).order_by(Author.id)
    return session.execute(stmt).scalars().all()


def fetch_authors_with_publications(
    session: Session,
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
    return session.execute(stmt).scalars().all()


def fetch_publications_with_authors(
    session: Session,
) -> Sequence[Publication]:
    stmt = (
        select(Publication)
        .options(
            # selectinload(Publication.author)
            joinedload(Publication.author)
        )
        .order_by(Publication.id)
    )
    return session.execute(stmt).scalars().all()


def main():
    print(Base.metadata.tables)
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    # print(Author.mro())
    with Session(engine) as session:
        # # create_entities(session)
        # bob = get_author(session, username="bob")
        # ken = get_author(session, username="ken")
        #
        # if bob:
        #     print("bob's publications:")
        #     for pub in bob.publications:
        #         print("-", pub)

        # authors = fetch_authors(session)
        # authors = fetch_authors_with_publications(session)
        # for author in authors:
        #     print(author)
        #     if author.publications:
        #         print(f"{author.name}'s publications:")
        #     else:
        #         print(author.name, "has no publications")
        #
        #     for pub in author.publications:
        #         print("-", pub)

        publications = fetch_publications_with_authors(session)
        for publication in publications:
            print(publication, "by", publication.author)


if __name__ == "__main__":
    main()
