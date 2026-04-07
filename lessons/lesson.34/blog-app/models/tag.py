from typing import TYPE_CHECKING

from sqlalchemy import (
    Text,
    ForeignKey,
    CheckConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import CITEXT

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models import Post
from models.base import Base
from models.mixins import IdIntPk
from models.post_tag_association import PostTagAssociation

# if TYPE_CHECKING:
#     from models import User


class Tag(Base):

    name: Mapped[str] = mapped_column(
        CITEXT,
        primary_key=True,
    )
    description: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )

    posts: Mapped[list[Post]] = relationship(
        secondary=PostTagAssociation.__table__,
        back_populates="tags",
    )

    __table_args__ = (
        CheckConstraint(
            func.length(name) <= 16,
            name=f"name_length",
        ),
    )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r})"

    def __repr__(self) -> str:
        return str(self)
