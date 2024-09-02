from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from models.mixins import IntIdPkMixin

if TYPE_CHECKING:
    from models import Pet


class Visit(IntIdPkMixin, Base):

    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey("pets.id"))
    reason: Mapped[str] = mapped_column(String)
    visit_date: Mapped[date]

    pet: Mapped["Pet"] = relationship("Pet", back_populates="visits")
