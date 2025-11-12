from datetime import datetime

from sqlalchemy import Text, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
from models.mixins import IdIntPkMixin


class Product(IdIntPkMixin, Base):
    __tablename__ = "products"

    title: Mapped[str] = mapped_column(
        Text,
    )
    description: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )

    kind_id: Mapped[int] = mapped_column(
        ForeignKey("product_kinds.id"),
    )
    supplier_id: Mapped[int] = mapped_column(
        ForeignKey("suppliers.id"),
    )
