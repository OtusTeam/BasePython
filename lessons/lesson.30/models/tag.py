from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship, mapped_column

from .mixins.created_at_mixin import CreatedAtMixin
from .mixins.int_pk_mixin import IntPkMixin
from .base import Base
from .publication_tag_association import PublicationTagAssociation

if TYPE_CHECKING:
    from .publication import Publication


class Tag(IntPkMixin, CreatedAtMixin, Base):
    name: Mapped[str] = mapped_column(unique=True)

    publications: Mapped[list["Publication"]] = relationship(
        secondary=PublicationTagAssociation.__table__,
        back_populates="tags",
    )
    # publication_associations: Mapped[list[PublicationTagAssociation]] = relationship(
    #     back_populates=
    # )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"id={self.id!r}, "
            f"name={self.name!r}, "
            f"created_at={self.created_at!r}"
            f")"
        )

    def __repr__(self) -> str:
        return str(self)
