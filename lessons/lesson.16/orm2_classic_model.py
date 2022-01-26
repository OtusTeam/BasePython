from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
)
from sqlalchemy.orm import mapper

# http://abc.com
DB_URL = "sqlite:///example-02.db"
engine = create_engine(DB_URL, echo=True)
metadata = MetaData()


users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), unique=True),
    Column("is_staff", Boolean, default=False, nullable=False),
)


class User:
    def __init__(self, id: int, username: str, is_staff: bool):
        """
        :param id:
        :param username:
        :param is_staff:
        """
        self.id = id
        self.username = username
        self.is_staff = is_staff


mapper(User, users_table)
# user = User(id=1, username="john", is_staff=False)


def create_table():
    """
    CREATE TABLE users (
        id INTEGER NOT NULL,
        username VARCHAR(32),
        is_staff BOOLEAN NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (username)
    )
    """
    metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_table()
