"""
ORM - Object Relational Mapping
"""

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import (
    declarative_base,
)


DB_URL = "sqlite:///example2.db"

# DB_ECHO = False
DB_ECHO = True

engine = create_engine(
    url=DB_URL,
    echo=DB_ECHO,
)

Base = declarative_base()


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(180), unique=True, nullable=True)


def main():
    Base.metadata.drop_all(bind=engine)
    sql = """
    CREATE TABLE author (
        id INTEGER NOT NULL, 
        username VARCHAR(30) NOT NULL, 
        email VARCHAR(180), 
        PRIMARY KEY (id), 
        UNIQUE (username), 
        UNIQUE (email)
    )
    """
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
