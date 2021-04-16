from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Boolean,
)
from sqlalchemy.orm import mapper

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), unique=True),
    Column("is_staff", Boolean, nullable=False, default=False),
)


class User:
    def __init__(self, id: int, username: str, is_staff: bool = False):
        """
        :param id:
        :param username:
        :param is_staff:
        """
        self.id = id
        self.username = username
        self.is_staff = is_staff


mapper(User, users_table)
