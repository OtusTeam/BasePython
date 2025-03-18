from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)

import config


engine = create_engine(
    config.SQLA_PG_URL,
    echo=config.SQLA_ECHO,
)


class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention=config.SQLA_NAMING_CONVENTION,
    )

    id: Mapped[int] = mapped_column(primary_key=True)
