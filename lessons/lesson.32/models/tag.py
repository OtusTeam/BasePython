from typing import TYPE_CHECKING

from sqlalchemy import (
    Text,
    CheckConstraint,
    and_,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base
from models.mixins import IdIntPKMixin
from models.post_tag_association import PostTagAssociation

if TYPE_CHECKING:
    from models import Post


class Tag(IdIntPKMixin, Base):

    name: Mapped[str] = mapped_column(
        Text,
        # TODO: length constraint
        unique=True,
    )

    posts: Mapped[list["Post"]] = relationship(
        secondary=PostTagAssociation.__table__,
        back_populates="tags",
    )

    def __str__(self):
        return f"{self.__class__.__name__}({self.name!r})"

    def __repr__(self):
        return str(self)

    __table_args__ = (
        # добавляем ограничения
        CheckConstraint(
            and_(
                func.char_length(name) >= 1,
                func.char_length(name) <= 32,
            ),
            name="name_length",
        ),
    )
