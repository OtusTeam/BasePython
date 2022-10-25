from sqlalchemy import (
    Column, String, Integer, ForeignKey,
)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import CreatedAtMixin


class Author(CreatedAtMixin, Base):
    name = Column(String(64), unique=False, nullable=False, default='')
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)

    # orm
    user = relationship('User', back_populates='author', uselist=False)
    posts = relationship('Post', back_populates='author', uselist=True)

    def __str__(self):
        return f'{self.__class__.__name__}(' \
               f'id={self.id}, ' \
               f'name={self.name} )'
