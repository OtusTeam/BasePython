from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload, selectinload

from models import (
    Base,
    engine,
    Author,
    Publication,
    Tag,
)


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
    stmt = select(Author).where(Author.username == username)
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


def fetch_publications_with_tags(
    session: Session,
) -> Sequence[Publication]:
    stmt = (
        select(Publication)
        .options(
            selectinload(Publication.tags),
        )
        .order_by(Publication.id)
    )
    return session.execute(stmt).scalars().all()


def create_tag(
    session: Session,
    name: str,
) -> Tag:
    tag = Tag(name=name)
    session.add(tag)
    session.commit()
    return tag


def fetch_tags(session: Session) -> Sequence[Tag]:
    stmt = select(Tag).order_by(Tag.id)
    return session.scalars(stmt).all()


def example_create_publication_with_tags(session: Session) -> Publication:
    tags = fetch_tags(session)
    bob = get_author(session, username="bob")
    publication = create_one_publication(session, bob, title="Another HowTo")
    print("created publication:", publication)
    print("publication's tags:", publication.tags)

    publication.tags.extend(tags)
    print("publication's tags before commit:", publication.tags)
    session.commit()
    print("publication's tags after commit:", publication.tags)
    return publication


def main():
    print(Base.metadata.tables)
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    # print(Author.mro())
    with Session(engine, expire_on_commit=False) as session:
        # create_entities(session)
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

        # publications = fetch_publications_with_authors(session)
        # for publication in publications:
        #     print(publication, "by", publication.author)

        #
        # create_author(session, name="Will", username="will")
        tag_spam = create_tag(session, "spam")
        tag_eggs = create_tag(session, "eggs")
        print("Tags:", [tag_spam, tag_eggs])
        example_create_publication_with_tags(session)
        pubs = fetch_publications_with_tags(session)
        for pub in pubs:
            print("+++", pub)
            print(pub.tags)
            for tag in pub.tags:
                if tag.name == "spam":
                    pub.tags.remove(tag)

        session.commit()


if __name__ == "__main__":
    main()
