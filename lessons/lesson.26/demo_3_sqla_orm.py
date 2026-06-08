from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    insert,
    select,
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session,
)

import config

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
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
    full_name: Mapped[str] = mapped_column(
        String(100),
        default="",
        server_default="",
    )

    def hello(self):
        print(f"Hi from {self.full_name!r} ({self.username})")

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}"
            f", username={self.username!r}"
            f", email={self.email!r}"
            f", full_name={self.full_name!r}"
            ")"
        )

    def __repr__(self):
        return str(self)


# примерно такое будет сгенерировано
# руками писать это не нужно
# и копировать сюда из терминала тоже не нужно
some_name = """
CREATE TABLE authors (
	id INTEGER NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	email VARCHAR(150), 
	full_name VARCHAR(100) DEFAULT '' NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
);
"""


def create_tables():
    print({"authors": Author.__table__})
    print(Base.metadata.tables)
    Base.metadata.drop_all(engine)  # удалит всё! безвозвратно
    Base.metadata.create_all(engine)


def insert_authors():
    john = Author(
        username="john",
        email="john@example.com",
    )
    john.hello()
    print(john)

    with Session(engine) as session:
        session.add(john)
        session.commit()
        print("committed")
        print("new john:", john)

    bob = Author(
        username="bob",
        email="bob@example.com",
        full_name="Bob Black",
    )
    alice = Author(
        username="alice",
        full_name="Alice",
    )
    new_authors = [bob, alice]
    with Session(engine) as session:
        session.add_all(new_authors)
        session.commit()
        print("committed")
        print("new authors:", new_authors)


def fetch_values():
    statement = (
        select(Author)
        .where(
            Author.email.isnot(None),
        )
        .order_by(
            Author.username.desc(),
        )
    )
    print(statement)
    print(repr(statement))

    with Session(engine) as session:
        result = session.scalars(statement).all()

    for author in result:
        print(author)
        print(author.hello())


def main():
    create_tables()
    insert_authors()
    fetch_values()


if __name__ == "__main__":
    main()
