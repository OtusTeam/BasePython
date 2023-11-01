from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from models.base import Base


class User(Base):

    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)

    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"username={self.username!r}, email={self.email!r})"
        )
