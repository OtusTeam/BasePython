from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from db import engine

metadata = MetaData()

authors_table = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), nullable=False, unique=True),
    Column("email", String, nullable=True, unique=True),
)


SQL = """
CREATE TABLE authors (
    id SERIAL NOT NULL, 
    username VARCHAR(32) NOT NULL, 
    email VARCHAR, 
    PRIMARY KEY (id), 
    UNIQUE (username), 
    UNIQUE (email)
);
"""


def create_table():
    metadata.create_all(bind=engine)


if __name__ == '__main__':
    print("tables:", metadata.tables)
    create_table()

