from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.mixins import IdIntPKMixin, CreatedAtMixin

if TYPE_CHECKING:
    from models import User


class Profile(IdIntPKMixin, CreatedAtMixin, Base):
    __tablename__ = "profiles"

    about: Mapped[str] = mapped_column(
        default="",
        server_default="",
    )
    site: Mapped[str] = mapped_column(
        String(4096),
        default="",
        server_default="",
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
    )
    user: Mapped["User"] = relationship(
        back_populates="profile",
    )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self.id},"
            f" about={self.about!r},"
            f" site={self.site!r},"
            f" user_id={self.user_id!r}"
            ")"
        )

    def __repr__(self) -> str:
        return str(self)
