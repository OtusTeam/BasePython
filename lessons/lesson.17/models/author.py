from sqlalchemy import (
    Column, String, Integer, ForeignKey, Boolean,
)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import CreatedAtMixin


class Author(CreatedAtMixin, Base):
    name = Column(String(64), unique=False, nullable=False, default='')
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
    is_mentor = Column(
        Boolean,
        default=False,
        server_default="FALSE",
        nullable=False,
    )

    # orm
    user = relationship('User', back_populates='author', uselist=False)
    posts = relationship('Post', back_populates='author', uselist=True)

    def __str__(self):
        return f'{self.__class__.__name__}(' \
               f'id={self.id}, ' \
               f'name={self.name} )'
