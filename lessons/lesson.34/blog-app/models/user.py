from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.mixins.created_at import CreatedAtMixin
from models.mixins.id_int_pk import IdIntPkMixin

if TYPE_CHECKING:
    from models import Post


class User(IdIntPkMixin, CreatedAtMixin, Base):
    username: Mapped[str] = mapped_column(
        String(32),
        unique=True,
    )
    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
    )
    full_name: Mapped[str] = mapped_column(
        String(100),
        default="",
        server_default="",
    )

    posts: Mapped[list["Post"]] = relationship(
        back_populates="user",
    )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, email={self.email!r}, full_name={self.full_name!r})"

    def __repr__(self) -> str:
        return str(self)
