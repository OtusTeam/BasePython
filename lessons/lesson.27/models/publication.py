from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column

from .mixins.int_pk_mixin import IntPkMixin
from .base import Base


if TYPE_CHECKING:
    from .author import Author


class Publication(IntPkMixin, Base):
    title: Mapped[str]
    body: Mapped[str] = mapped_column(
        default="",
        server_default="",
    )
    author_id: Mapped[int] = mapped_column(
        ForeignKey("author.id"),
        # unique=True,
    )
    author: Mapped["Author"] = relationship(
        back_populates="publications",
        # backref="publications",
    )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"id={self.id!r},"
            f" title={self.title!r},"
            f" author_id={self.author_id!r}"
            ")"
        )

    def __repr__(self) -> str:
        return str(self)


# Create SQL example
"""
CREATE TABLE publication (
    id INTEGER NOT NULL, 
    title VARCHAR NOT NULL, 
    body VARCHAR DEFAULT '' NOT NULL, 
    author_id INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(author_id) REFERENCES author (id)
)
"""


"""
CREATE TABLE publication (
	id SERIAL NOT NULL, 
	title VARCHAR NOT NULL, 
	body VARCHAR DEFAULT '' NOT NULL, 
	author_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(author_id) REFERENCES author (id)
)
"""