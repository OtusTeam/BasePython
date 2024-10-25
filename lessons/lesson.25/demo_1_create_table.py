from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from db import engine

metadata = MetaData()

authors = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), nullable=False, unique=True),
    Column("email", String(120), nullable=True, unique=True),
)

EXAMPLE_SQL_0 = """
CREATE TABLE authors (
    id INTEGER NOT NULL, 
    PRIMARY KEY (id)
)"""

EXAMPLE_SQL_1 = """
CREATE TABLE authors (
    id INTEGER NOT NULL, 
    username VARCHAR(32) NOT NULL, 
    email VARCHAR(120), 
    PRIMARY KEY (id), 
    UNIQUE (username), 
    UNIQUE (email)
)
"""


def create_authors_table():
    # authors.create(engine)
    print("Tables:", metadata.tables)
    metadata.create_all(bind=engine)


def main():
    create_authors_table()


if __name__ == "__main__":
    main()
