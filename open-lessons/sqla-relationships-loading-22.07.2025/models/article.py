from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.mixins import IdIntPKMixin, CreatedAtMixin

if TYPE_CHECKING:
    from models import User


class Article(IdIntPKMixin, CreatedAtMixin, Base):
    __tablename__ = "articles"

    title: Mapped[str] = mapped_column(
        String(100),
        index=True,
    )
    text: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    user: Mapped["User"] = relationship(
        back_populates="articles",
    )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, user_id={self.user_id!r})"

    def __repr__(self) -> str:
        return str(self)
