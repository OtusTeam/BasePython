from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .posts_tags_association import posts_tags_association_table


if TYPE_CHECKING:
    from .post import Post


class Tag(Base):

    name: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    posts: Mapped[list["Post"]] = relationship(
        secondary=posts_tags_association_table,
        back_populates="tags",
        order_by="asc(Post.id)",
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"name={self.name!r}"
            ")"
        )
