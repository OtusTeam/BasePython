from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.mixins import CreatedAtMixin

if TYPE_CHECKING:
    from models.post import Post


class User(CreatedAtMixin, Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(
        String(100),
        default="",
        server_default="",
    )
    username: Mapped[str] = mapped_column(
        String(32),
        unique=True,
    )
    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
    )

    posts: Mapped[list["Post"]] = relationship(
        back_populates="user",
    )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r}, username={self.username!r}, email={self.email!r})"

    def __repr__(self) -> str:
        return str(self)


# generated code:
GENERATED_SQL = """
CREATE TABLE users (
	id SERIAL NOT NULL, 
	name VARCHAR(100) DEFAULT '' NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	email VARCHAR(150), 
	created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
);
"""
