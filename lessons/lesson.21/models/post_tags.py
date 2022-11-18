from sqlalchemy import Table, Column, ForeignKey
from .base import Base

post_tags_association_table = Table(
    "post_tags_association_table",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)
