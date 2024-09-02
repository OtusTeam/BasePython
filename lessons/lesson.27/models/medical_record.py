from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from models.mixins import IntIdPkMixin

if TYPE_CHECKING:
    from models import Pet


class MedicalRecord(IntIdPkMixin, Base):

    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey("pets.id"))
    notes: Mapped[str] = mapped_column(Text)
    last_visit: Mapped[date]

    pet: Mapped["Pet"] = relationship(
        back_populates="medical_record",
        uselist=False,
    )
