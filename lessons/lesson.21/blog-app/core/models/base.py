from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base, declared_attr


class Base:

    @declared_attr
    def __tablename__(cls):
        return f"blog_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)
