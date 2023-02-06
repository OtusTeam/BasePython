from sqlalchemy import Table, Column, ForeignKey

from .base import Base

posts_tags_association = Table(
    "posts_tags_association",
    Base.metadata,
    Column("post_id", ForeignKey("blog_posts.id"), primary_key=True),
    Column("tag_id", ForeignKey("blog_tags.id"), primary_key=True),
)
