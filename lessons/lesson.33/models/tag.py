from typing import TYPE_CHECKING

from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import CITEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.posts_tags import PostTagsAssociation

if TYPE_CHECKING:
    from models import Post


class Tag(Base):
    name: Mapped[str] = mapped_column(
        CITEXT(32),
        primary_key=True,
    )
    description: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )

    posts: Mapped[list["Post"]] = relationship(
        back_populates="tags",
        secondary=PostTagsAssociation.__table__,
    )

    def __str__(self):
        return f"{self.__class__.__name__}<{self.name}>"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, description={self.description!r})"
