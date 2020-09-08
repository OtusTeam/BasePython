from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Boolean
from sqlalchemy.orm import mapper

engine = create_engine("sqlite:///example.db")
metadata = MetaData()


users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), unique=True),
    Column("is_staff", Boolean, default=False),
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


if __name__ == "__main__":
    metadata.create_all(engine)
