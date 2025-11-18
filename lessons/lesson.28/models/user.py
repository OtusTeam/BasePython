from typing import TYPE_CHECKING

from sqlalchemy import (
    Text,
    CheckConstraint,
    func,
    and_,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base
from models.mixins import IdIntPKMixin

if TYPE_CHECKING:
    from models import Post


class User(IdIntPKMixin, Base):

    username: Mapped[str] = mapped_column(
        Text,
        unique=True,
    )
    email: Mapped[str | None] = mapped_column(
        Text,
        unique=True,
    )
    full_name: Mapped[str] = mapped_column(
        Text,
        server_default="",
    )

    # foobar: Mapped[str | None] = mapped_column(
    #     unique=True,
    # )

    posts: Mapped[list["Post"]] = relationship(
        back_populates="user",
    )

    __table_args__ = (
        # добавляем ограничения
        CheckConstraint(
            and_(
                func.char_length(username) <= 32,
                func.char_length(username) >= 3,
            ),
            name="username_length",
        ),
        # CheckConstraint(
        #     and_(
        #         func.char_length(foobar) <= 32,
        #         func.char_length(foobar) >= 3,
        #     ),
        #     name="foobar_length",
        # ),
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id!r}"
            f", username={self.username!r}"
            f", email={self.email!r}"
            f", full_name={self.full_name!r})"
        )
