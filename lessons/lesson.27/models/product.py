from sqlalchemy import Column, Integer, String, DateTime, Boolean, func

from .database import db


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    # updated_at = Column(DateTime, server_onupdate=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    is_new = Column(Boolean, default=False, server_default="FALSE", nullable=False)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name!r}>"
