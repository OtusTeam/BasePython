from typing import TYPE_CHECKING

from sqlalchemy import (
    Text,
    func,
    CheckConstraint,
    ForeignKey,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base

from models.mixins import IdIdentity

if TYPE_CHECKING:
    from models.user import User


class Post(Base, IdIdentity):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column(
        Text,
    )
    body: Mapped[str] = mapped_column(
        Text,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            # ondelete="RESTRICT",
        ),
    )
    user: Mapped["User"] = relationship(
        back_populates="posts",
    )

    __table_args__ = (
        #
        CheckConstraint(func.length(title) <= 80),
    )
