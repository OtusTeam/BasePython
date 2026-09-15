from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base

from models.mixins import CreatedAt


class PostsTagsAssociation(Base, CreatedAt):
    __tablename__ = "posts_tags_association_table"

    post_id: Mapped[int] = mapped_column(
        ForeignKey("posts.id"),
        primary_key=True,
    )
    tag_name: Mapped[str] = mapped_column(
        ForeignKey("tags.name"),
        primary_key=True,
    )
