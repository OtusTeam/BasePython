from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from models.mixins import IntIdPkMixin

if TYPE_CHECKING:
    from models import Owner, Visit, MedicalRecord


class Pet(IntIdPkMixin, Base):

    name: Mapped[str] = mapped_column(String)
    species: Mapped[str] = mapped_column(String)
    owner_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("owners.id"),
    )

    owner: Mapped["Owner"] = relationship(back_populates="pets")
    visits: Mapped[list["Visit"]] = relationship(back_populates="pet")
    medical_record: Mapped["MedicalRecord"] = relationship(
        back_populates="pet",
        uselist=False,
    )
