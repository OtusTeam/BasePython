from sqlalchemy import MetaData
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
)

from config import sqla_naming_convention


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=sqla_naming_convention)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
