from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from db import engine


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    # id = Column(Integer, primary_key=True)
    # username = Column(String(32), nullable=False, unique=True)
    # email = Column(String, nullable=True, unique=True)

    # id = mapped_column(Integer, primary_key=True)
    # username = mapped_column(String(32), nullable=False, unique=True)
    # email = mapped_column(String, nullable=True, unique=True)

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str | None] = mapped_column(unique=True)


SQL_DROP = """
DROP TABLE authors;
"""

SQL_CRATE = """
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
    # print("table:", Author.__table__)
    # print("table repr:", repr(Author.__table__))
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
