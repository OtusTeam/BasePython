from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from models.mixins import CreatedAtMixin

if TYPE_CHECKING:
    from models import User


class Datacenter(CreatedAtMixin, Base):
    __tablename__ = "datacenters"

    name: Mapped[str] = mapped_column(
        String(80),
        primary_key=True,
    )
    description: Mapped[str] = mapped_column(
        default="",
        server_default="",
    )

    users: Mapped[list["User"]] = relationship(
        back_populates="dc",
    )

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"

    def __repr__(self):
        return str(self)
