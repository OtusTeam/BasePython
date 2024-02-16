from sqlalchemy import Column, Integer
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    # @declared_attr
    # def id(cls) -> MappedColumn | None:
    #     if not cls._no_id:
    #         return Column(Integer, primary_key=True)
