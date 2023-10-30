from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from config import engine

metadata = MetaData()

authors_table = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), nullable=False, unique=True),
    Column("email", String, nullable=True, unique=True),
)

SQL_1 = """
CREATE TABLE authors (
  id INTEGER NOT NULL, 
  username VARCHAR(32) NOT NULL, 
  PRIMARY KEY (id), 
  UNIQUE (username)
);
"""

SQL_2 = """
CREATE TABLE authors (
  id INTEGER NOT NULL, 
  username VARCHAR(32) NOT NULL, 
  email VARCHAR, 
  PRIMARY KEY (id), 
  UNIQUE (username), 
  UNIQUE (email)
);
"""

SQL_PG = """
CREATE TABLE authors (
  id SERIAL NOT NULL, 
  username VARCHAR(32) NOT NULL, 
  email VARCHAR, 
  PRIMARY KEY (id), 
  UNIQUE (username), 
  UNIQUE (email)
);
"""


def main():
    metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
