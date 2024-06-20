from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table

from db import engine

metadata = MetaData()

authors_table = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), nullable=False, unique=True),
    Column("email", String, nullable=True, unique=True),
)


# будет скомпилировано примерно в следующее
# только при создании таблички через create_all
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


def create_tables():
    print(metadata.tables)
    # metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
