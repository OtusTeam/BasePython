from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    email = Column(String, nullable=True)

    bio = relationship(
        "UserBio",
        back_populates="user",
        uselist=False,
    )
