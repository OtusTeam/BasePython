from typing import TYPE_CHECKING

from sqlalchemy import (
    Text,
    ForeignKey,
    CheckConstraint,
    func,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base
from models.mixins import IdIntPk

if TYPE_CHECKING:
    from models import User


class Post(IdIntPk, Base):

    title: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )

    content: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
    )

    user: Mapped[User] = relationship(
        back_populates="posts",
        lazy="raise_on_sql",
    )
    __table_args__ = (
        CheckConstraint(
            func.length(title) <= 100,
            name="title_max_length",
        ),
    )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}"
            f", title={self.title!r}"
            f", user_id={self.user_id!r}"
            ")"
        )

    def __repr__(self) -> str:
        return str(self)
