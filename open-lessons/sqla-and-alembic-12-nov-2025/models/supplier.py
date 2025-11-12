from sqlalchemy import BigInteger, Identity, Text
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
from models.mixins import IdIntPkMixin


class Supplier(IdIntPkMixin, Base):
    __tablename__ = "suppliers"

    name: Mapped[str] = mapped_column(
        Text,
    )
    tax_number: Mapped[str | None] = mapped_column(
        Text,
        unique=True,
    )
