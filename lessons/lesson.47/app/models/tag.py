from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from models.posts_tags_association import PostsTagsAssociation
from models.base import Base
from models.mixins.created_at_mixin import CreatedAtMixin


class Tag(CreatedAtMixin, Base):
    name = Column(
        String,
        unique=True,
        nullable=False,
    )
    # posts = relationship(
    #     "Post",
    #     secondary=posts_tags_association_table,
    #     back_populates="tags",
    # )
    posts = relationship(
        "Post",
        # secondary=PostsTagsAssociation.__table__,
        secondary=PostsTagsAssociation.__tablename__,
        # secondary="posts_tags_association",
        back_populates="tags",
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Tag(name={self.name!r})"
