from typing import TYPE_CHECKING

from sqlalchemy import (
    Text,
    ForeignKey,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base
from models.mixins import IdIntPKMixin, CreatedAtMixin
from models.post_tag_association import PostTagAssociation

if TYPE_CHECKING:
    from models import User, Tag


class Post(IdIntPKMixin, CreatedAtMixin, Base):

    title: Mapped[str] = mapped_column(
        Text,
        # TODO: length constraint
        unique=False,
        default="",
        server_default="",
    )
    slug: Mapped[str] = mapped_column(
        Text,
        unique=True,
    )
    body: Mapped[str] = mapped_column(
        Text,
        unique=False,
        default="",
        server_default="",
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
    )

    user: Mapped["User"] = relationship(
        back_populates="posts",
    )

    tags: Mapped[list["Tag"]] = relationship(
        secondary=PostTagAssociation.__table__,
        back_populates="posts",
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}"
            f", title={self.title!r}"
            # f"body={self.body!r}"
            f")"
        )


# вот такой SQL был сгенерирован:
SQL = """
CREATE TABLE post (
	id BIGINT GENERATED ALWAYS AS IDENTITY, 
	title TEXT DEFAULT '' NOT NULL, 
	body TEXT DEFAULT '' NOT NULL, 
	user_id BIGINT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES "user" (id)
);
"""
# вам не нужно это добавлять в код никогда!
# это только для демо на занятии.
