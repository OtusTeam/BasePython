from sqlalchemy import (
    Column,
    String,
)

from .base import Base
from .mixins import CreatedAtMixin


class Manager(CreatedAtMixin, Base):
    name = Column(String(64), unique=False, nullable=False, default="")

    def __str__(self):
        return f"{self.__class__.__name__}(" f"id={self.id}, " f"name={self.name} )"
