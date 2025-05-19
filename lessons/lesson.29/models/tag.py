from typing import TYPE_CHECKING

from sqlalchemy.dialects.postgresql import CITEXT
from sqlalchemy.orm import mapped_column, Mapped, relationship

from models.base import Base

from models.post_tag_association import PostTagAssociation

# from models.post_tag_association import posts_tags_association
from models.mixins import CreatedAtMixin

if TYPE_CHECKING:
    from models import Post


class Tag(CreatedAtMixin, Base):
    __tablename__ = "tags"
    name: Mapped[str] = mapped_column(
        CITEXT(length=20),
        unique=True,
    )
    posts: Mapped[list["Post"]] = relationship(
        back_populates="tags",
        # secondary=posts_tags_association,
        secondary=PostTagAssociation.__table__,
    )

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r})"
