from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
)

from .base import Base


posts_tags_table = Table(
    "blog_app__posts_tags_association_table",
    Base.metadata,
    Column("post_id", ForeignKey("blog_app__posts.id"), primary_key=True),
    Column("tag_id", ForeignKey("blog_app__tags.id"), primary_key=True),
)
