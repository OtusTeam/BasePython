from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base
from models.mixins import IdIntPk

if TYPE_CHECKING:
    from models.user import User


class Post(IdIntPk, Base):

    title: Mapped[str] = mapped_column(
        String(100),
        default="",
        server_default="",
    )
    content: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    user: Mapped["User"] = relationship(
        back_populates="posts",
    )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}"
            f", user_id={self.user_id!r}"
            f", title={self.title!r}"
            f", content={self.content!r}"
            ")"
        )

    def __repr__(self):
        return str(self)
