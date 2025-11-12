from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
from models.mixins import IdIntPkMixin


class ProductKind(IdIntPkMixin, Base):
    __tablename__ = "product_kinds"

    name: Mapped[str] = mapped_column(
        Text,
        unique=True,
    )
