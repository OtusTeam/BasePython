from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import settings


class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )

    id: Mapped[int] = mapped_column(primary_key=True)
