from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
)


class Base(DeclarativeBase):

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)
