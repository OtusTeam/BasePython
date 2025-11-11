from typing import TYPE_CHECKING

from sqlalchemy import (
    Text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base
from models.mixins import IdIntPKMixin

if TYPE_CHECKING:
    from models import Post


class User(IdIntPKMixin, Base):

    username: Mapped[str] = mapped_column(
        Text,
        unique=True,
    )
    email: Mapped[str | None] = mapped_column(
        Text,
        unique=True,
    )
    full_name: Mapped[str] = mapped_column(
        Text,
        server_default="",
    )

    posts: Mapped[list["Post"]] = relationship(
        back_populates="user",
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id!r}"
            f", username={self.username!r}"
            f", email={self.email!r}"
            f", full_name={self.full_name!r})"
        )


# вот такой SQL был сгенерирован:
SQL = """
CREATE TABLE "user" (
	id BIGINT GENERATED ALWAYS AS IDENTITY, 
	username TEXT NOT NULL, 
	email TEXT, 
	full_name TEXT DEFAULT '' NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
);
"""
# вам не нужно это добавлять в код никогда!
# это только для демо на занятии.
