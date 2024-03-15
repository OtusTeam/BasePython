from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import func

from sqlalchemy.orm import relationship

from models.posts_tags_association import PostsTagsAssociation
from models.base import Base
from models.mixins.user_relation_mixin import UserRelationMixin
from models.mixins.created_at_mixin import CreatedAtMixin


class Post(CreatedAtMixin, UserRelationMixin, Base):
    title = Column(
        String(100),
        nullable=False,
        default="",
        server_default="",
    )
    # body = Column(Text, nullable=False)
    published_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )

    author = relationship(
        # accessed through `User.posts`
        "User",
        back_populates="posts",
        uselist=False,
    )

    tags = relationship(
        "Tag",
        secondary=PostsTagsAssociation.__table__,
        back_populates="posts",
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"Post(id={self.id}, "
            f"title={self.title!r}, "
            f"published_at={self.published_at!r}, "
            f"user_id={self.user_id})"
        )
