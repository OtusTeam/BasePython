__all__ = ("Base",)

from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base, declared_attr

import config


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{config.DB_APP_PREFIX}{cls.__name__.lower()}s"

    @declared_attr
    def id(self):
        return Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)
