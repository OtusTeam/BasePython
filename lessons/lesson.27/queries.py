from sqlalchemy import (
    create_engine,
    String,
    text,
    select,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

db_url = "sqlite:///example.db"
db_echo = False

# только для демо и отладки!!
db_echo = True
engine = create_engine(
    url=db_url,
    echo=db_echo,
)


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(32),
        unique=True,
    )
    email: Mapped[str | None] = mapped_column(
        String(150),
        unique=True,
    )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, email={self.email!r})"

    def __repr__(self) -> str:
        return str(self)


def example_sql(session: Session):
    res = session.execute(text("SELECT 1;"))
    # print(res.all())
    # print(res.one())
    print(res.scalar())

    res = session.execute(select(2))
    print(res.scalar())

    total = session.execute(text("SELECT 1 + 2;"))
    print(total.scalar())

    total = session.execute(select(text("3 + 4;")))
    print(total.scalar())



def create_author(
    session: Session,
    username: str,
    email: str | None = None,
) -> Author:
    author = Author(
        username=username,
        email=email,
    )
    print("new author:", author)
    session.add(author)
    print("committing...")
    session.commit()
    print("created a new author:", author)
    return author


def create_authors(
    session: Session,
    *usernames: str,
) -> list[Author]:
    authors = [
        Author(username=username)
        for username in usernames
    ]
    print("new authors:", authors)
    session.add_all(authors)
    print("committing...")
    session.commit()
    print("created new authors:", authors)
    return authors


def get_author(
    session: Session,
    author_id: int,
) -> Author | None:
    return session.get(Author, author_id)


def find_author(
    session: Session,
    username: str,
) -> Author | None:
    statement = (
        select(Author)
        .where(
            Author.username == username,
        )
    )
    # return session.scalar(statement)
    result = session.execute(statement)
    return result.scalar()


def get_authors(session: Session) -> list[Author]:
    statement = (
        select(Author)
        # .order_by(Author.id)
        .order_by(Author.username)
    )
    # result = session.execute(statement)
    # return result.scalars()
    return list(session.scalars(statement).all())


def create_tables():
    Base.metadata.create_all(engine)


def main():
    # create_tables()

    with Session(engine) as session:
        # example_sql(session)
        # create_author(session, username="bob")
        # create_author(session, username="alice", email="alice@example.com")
        #
        # create_authors(
        #     session,
        #     "jack",
        #     "kyle",
        #     "nick",
        # )

        # user_with_id_3 = get_author(session, author_id=3)
        # print("one", user_with_id_3)
        #
        # user_with_id_3 = get_author(session, author_id=3)
        # print("two", user_with_id_3)

        # bob = find_author(session, "bob")
        # print("found bob:", bob)
        # sam = find_author(session, "sam")
        # print("found sam:", sam)

        authors = get_authors(session)
        for author in authors:
            print("-", author)


if __name__ == '__main__':
    main()
