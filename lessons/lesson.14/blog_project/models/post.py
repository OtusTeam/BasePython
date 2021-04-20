from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from blog_project.models import Base
from blog_project.models.posts_tags import posts_tags_table


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False, default="", server_default="")

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="posts")
    tags = relationship(
        "Tag",
        secondary=posts_tags_table,
        back_populates="posts"
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, tags={self.tags})"

    def __repr__(self):
        return str(self)
