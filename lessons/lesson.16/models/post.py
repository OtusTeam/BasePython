from sqlalchemy import (
    Column, String, Text,
    Integer, ForeignKey,
)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import CreatedAtMixin


class Post(CreatedAtMixin, Base):
    title = Column(String(200), unique=False, nullable=False)
    body = Column(Text, nullable=False, default='')
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)

    # orm
    author = relationship('Author', back_populates='posts', uselist=False)

    def __str__(self):
        return f'{self.__class__.__name__}(' \
               f'id={self.id}, ' \
               f'title={self.title} )'
