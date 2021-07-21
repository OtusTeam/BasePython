from sqlalchemy import (
    MetaData,
    create_engine,
    Table,
    Column,
    Integer,
    String,
    Boolean,
)
from sqlalchemy.orm import mapper

# engine = create_engine("postgresql://user:password@localhost:5432/app")

engine = create_engine("sqlite:///example-db-01.sqlite", echo=True)


metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), unique=True),
    Column("is_staff", Boolean, nullable=False, default=False),
)


class User:
    def __init__(self, id, username, is_staff):
        self.id = id
        self.username = username
        self.is_staff = is_staff


# mapper(User, users_table)

if __name__ == "__main__":
    metadata.create_all(engine)
