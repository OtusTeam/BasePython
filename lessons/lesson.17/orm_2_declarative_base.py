"""
ORM - object relational mapping

object (??) - class
"""


from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
)

from sqlalchemy.orm import declarative_base

DB_URL = "sqlite:///example2.db"
# DB_ECHO = False
DB_ECHO = True

engine = create_engine(url=DB_URL, echo=DB_ECHO)


Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String(100), nullable=True, unique=True)

    # def send_hi(self):
    #     send_email(self.email, "Hi")


def main():
    Base.metadata.create_all(bind=engine)
    sql = """
    CREATE TABLE authors (
        id INTEGER NOT NULL, 
        username VARCHAR(32) NOT NULL, 
        email VARCHAR(100), 
        PRIMARY KEY (id), 
        UNIQUE (username), 
        UNIQUE (email)
    );
    """


if __name__ == "__main__":
    main()
