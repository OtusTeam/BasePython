from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import declarative_base

from config import engine

# Base = declarative_base()


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)


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


def main():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
