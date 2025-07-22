from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.mixins import IdIntPKMixin, CreatedAtMixin

if TYPE_CHECKING:
    from models import Article, Profile, Datacenter


class User(IdIntPKMixin, CreatedAtMixin, Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        String(32),
        unique=True,
    )
    datacenter: Mapped[str] = mapped_column(
        ForeignKey("datacenters.name"),
    )
    dc: Mapped["Datacenter"] = relationship(
        back_populates="users",
    )
    articles: Mapped[list["Article"]] = relationship(
        back_populates="user",
    )
    profile: Mapped["Profile"] = relationship(
        back_populates="user",
        # lazy="joined",
        lazy="raise_on_sql",
        # lazy="raise",
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, datacenter={self.datacenter!r})"

    def __repr__(self):
        return str(self)
