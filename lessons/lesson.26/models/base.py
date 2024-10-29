from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declared_attr


class Base(DeclarativeBase):

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
