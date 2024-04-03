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


"""
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
    # print(Base.metadata.tables)
    print(Author.__table__, repr(Author.__table__))
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
