from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase

from db import engine


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)


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


def create():
    Base.metadata.create_all(bind=engine)


def main():
    # create()
    print(repr(Base.metadata.tables[Author.__tablename__]))
    print(repr(Author.__table__))
    print(Base.metadata.tables[Author.__tablename__] is Author.__table__)


if __name__ == "__main__":
    main()
