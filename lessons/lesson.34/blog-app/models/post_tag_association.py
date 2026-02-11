from sqlalchemy import Table, Column, ForeignKey

from models.base import Base

post_tag_association_table = Table(
    "post_tag_association",
    Base.metadata,
    Column(
        "post_id",
        ForeignKey("posts.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "tag_name",
        ForeignKey("tags.name", ondelete="CASCADE"),
        primary_key=True,
    ),
)
