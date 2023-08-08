from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
)

from models import Base


posts_tags_association_table = Table(
    "posts_tags_association",
    Base.metadata,
    # Column("id", primary_key=True),
    Column("post_id", ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)
