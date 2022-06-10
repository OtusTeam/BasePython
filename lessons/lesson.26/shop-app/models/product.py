from sqlalchemy import Column, String, Integer, Boolean

from .database import db


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    is_new = Column(Boolean, nullable=True, default=False)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name!r}>"
