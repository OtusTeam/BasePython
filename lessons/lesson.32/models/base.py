from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

import config


class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention=config.SQLA_NAMING_CONVENTION,
    )

    id: Mapped[int] = mapped_column(primary_key=True)
