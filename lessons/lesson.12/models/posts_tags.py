from sqlalchemy import Table, Column, Integer, ForeignKey

from .base import Base


posts_tags_table = Table(
    "posts_tags_association_table",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), nullable=False),
    Column("tag_id", Integer, ForeignKey("tags.id"), nullable=False),
)
