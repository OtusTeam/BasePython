from typing import TYPE_CHECKING

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import CITEXT

from .base import Base
from .mixins import CreatedAtMixin

# from .publication_tag_association import publication_tag_association_table
from .publication_tag_association import PublicationTagAssociation

if TYPE_CHECKING:
    from .publication import Publication


class Tag(CreatedAtMixin, Base):
    name: Mapped[str] = mapped_column(
        CITEXT,
        unique=True,
    )

    publications: Mapped[list["Publication"]] = relationship(
        # secondary=publication_tag_association_table,
        secondary=PublicationTagAssociation.__table__,
        back_populates="tags",
    )

    def __str__(self) -> str:
        return (
            # fmt: off
            f"{self.__class__.__name__}("
            f"id={self.id!r}, name={self.name!r}"
            f")"
            # fmt: on
        )

    def __repr__(self) -> str:
        return str(self)
