from sqlalchemy import (
    Column,
    Integer,
)
from sqlalchemy.orm import declared_attr, InstrumentedAttribute
from sqlalchemy.ext.declarative import declarative_base


class Base:

    @declared_attr
    def __tablename__(cls):
        return f"blog_app__{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __str__(self):
        attributes = [
            f"{name}={(getattr(self, name))!r}"
            for name, value in vars(self.__class__).items()
            if not name.startswith("_") and isinstance(value, InstrumentedAttribute)
        ]
        return f"{self.__class__.__name__}({', '.join(attributes)})"

    def __repr__(self):
        return str(self)


Base = declarative_base(cls=Base)
