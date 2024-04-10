from sqlalchemy import (
    Column,
    String,
    UniqueConstraint,
    Index,
)
from sqlalchemy.orm import relationship

from models.base import Base


class User(Base):

    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)
    bio = Column(String(200), nullable=True, unique=False)

    ref_code = Column(String(10), nullable=True, unique=True)
    friend_code = Column(String(10), nullable=True, unique=True)

    posts = relationship(
        # to class name
        "Post",
        # how to access to this model[s]: post.`author`
        back_populates="author",
        # user can have any number of posts
        uselist=True,
    )

    __table_args__ = (
        # UniqueConstraint(ref_code, friend_code, name="unique_pair_ref_and_friend_code"),
        # UniqueConstraint("ref_code", "friend_code", name="unique_pair_ref_and_friend_code"),
        UniqueConstraint(friend_code, name="unique_ix_friend_code"),
        # Index("ix_friend_code", friend_code, mssql_clustered=True)
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"username={self.username!r}, "
            f"email={self.email!r}"
            f")"
        )
