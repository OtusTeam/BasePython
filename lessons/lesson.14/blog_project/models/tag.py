from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from blog_project.models import Base
from blog_project.models.posts_tags import posts_tags_table


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False, default="", server_default="")

    posts = relationship(
        "Post",
        secondary=posts_tags_table,
        back_populates="tags"
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
