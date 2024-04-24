from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
    Integer,
    UniqueConstraint,
)

from .base import Base
# class PostsTagsAssociation()

posts_tags_association_table = Table(
    "posts_tags_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("post_id", ForeignKey("posts.id"), nullable=False),
    Column("tag_id", ForeignKey("tags.id"), nullable=False),
    UniqueConstraint("post_id", "tag_id", name="unique_ix_post_tag"),
)
