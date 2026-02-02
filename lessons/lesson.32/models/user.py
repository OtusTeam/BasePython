from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.mixins import CreatedAtMixin

if TYPE_CHECKING:
    from models.post import Post


class User(CreatedAtMixin, Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str | None] = mapped_column(String(150), unique=True)
    full_name: Mapped[str] = mapped_column(String(100), server_default="")

    posts: Mapped[list["Post"]] = relationship(
        back_populates="user",
    )

    def greet(self) -> str:
        return f"Hello, {self.username}!"

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self.id!r}"
            f", username={self.username!r}"
            f", email={self.email!r}"
            f", full_name={self.full_name!r}"
            f", created_at={self.created_at!r}"
            ")"
        )

    def __repr__(self) -> str:
        return str(self)
