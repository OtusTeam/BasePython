from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import select

# from sqlalchemy import true

from db import engine

metadata = MetaData()

authors = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), nullable=False, unique=True),
    Column("email", String(120), nullable=True, unique=True),
    # Column("foobar", String(120)),
)


def create_authors_table():
    # authors.create(engine)
    print("authors table:", repr(authors))
    print("Tables:", metadata.tables)
    metadata.create_all(bind=engine)


def query_all_items():
    stmt = (
        # statement
        select(authors)
        # .where(authors.c.username != "john")
        # .where(authors.c.email.isnot(None))
        .where(
            authors.c.username != "john",
            authors.c.email.isnot(None),
            # authors.c.username.isnot(true()),
        ).order_by(authors.c.id)
    )
    with engine.connect() as conn:
        with conn.begin():
            result = conn.execute(stmt)
            for row in result.all():
                print(row.id, "\t", row.username, "\t", row.email)


def main():
    create_authors_table()
    query_all_items()


if __name__ == "__main__":
    main()
