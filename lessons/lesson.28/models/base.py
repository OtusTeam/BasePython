from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declared_attr

from config import SQLA_NAMING_CONVENTIONS


class Base(DeclarativeBase):

    metadata = MetaData(naming_convention=SQLA_NAMING_CONVENTIONS)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
