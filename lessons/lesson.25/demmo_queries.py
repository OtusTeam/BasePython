from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from db import engine

from demo_3_declarative_base import Author


def create_author(
    session: Session,
    name: str,
    username: str,
    email: str | None = None,
) -> Author:
    author = Author(
        name=name,
        username=username,
        email=email,
    )
    session.add(author)
    session.commit()

    return author


def fetch_authors(session: Session) -> Sequence[Author]:
    # return session.query(Author).all()
    stmt = select(Author).order_by(Author.id)
    return session.execute(stmt).scalars().all()


def main():
    with Session(engine) as session:
        # bob = create_author(session, "Bob Gray", "bob")
        # print("New user:", bob.id, bob.name)
        authors = fetch_authors(session)
        print(authors)
        for author in authors:
            print(author.id, author.name)


if __name__ == "__main__":
    main()
