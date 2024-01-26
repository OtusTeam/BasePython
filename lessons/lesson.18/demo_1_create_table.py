from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import insert
from sqlalchemy import select

from db import engine


metadata = MetaData()


authors_table = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), nullable=False, unique=True),
    Column("email", String, nullable=True, unique=True),
)

SQL_EXAMPLE_1 = """
CREATE TABLE authors (
    id INTEGER NOT NULL, 
    username VARCHAR(32) NOT NULL, 
    email VARCHAR, 
    PRIMARY KEY (id), 
    UNIQUE (username), 
    UNIQUE (email)
);
"""

SQL_EXAMPLE_2 = """
INSERT INTO authors (username, email) 
VALUES 
    ('john', 'john@example.com'), 
    ('sam', 'sam@example.com') 
RETURNING id, username
"""


def create():
    metadata.create_all(bind=engine)


def add():
    stmt = (
        insert(authors_table)
        .values(
            [
                {
                    "username": "john",
                    "email": "john@example.com",
                },
                {
                    "username": "sam",
                    "email": "sam@example.com",
                },
            ]
        )
        .returning(
            authors_table.c.id,
            authors_table.c.username,
        )
    )
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            print(row)
        conn.commit()


def show():
    stmt = select(
        authors_table.c.id,
        authors_table.c.username,
        authors_table.c.email,
    ).where(authors_table.c.username != "bob")
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            print(row)


def main():
    print(metadata.tables)
    create()
    add()
    # show()


if __name__ == "__main__":
    main()
