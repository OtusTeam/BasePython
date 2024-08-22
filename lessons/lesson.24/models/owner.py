from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.mixins import IntIdPkMixin

if TYPE_CHECKING:
    from models import Pet


class Owner(IntIdPkMixin, Base):

    name: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[str | None] = mapped_column(
        String,
        unique=True,
    )
    pets: Mapped[list["Pet"]] = relationship(back_populates="owner")
