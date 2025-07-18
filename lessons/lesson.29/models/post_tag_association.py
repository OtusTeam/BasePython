from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from models import Base


class PostTagAssociation(Base):
    __tablename__ = "posts_tags_association"

    post_id: Mapped[int] = mapped_column(
        ForeignKey("posts.id"),
    )
    tag_id: Mapped[int] = mapped_column(
        ForeignKey("tags.id"),
    )
    __table_args__ = (
        # уникальная пара
        UniqueConstraint(
            # "post_id",
            # "tag_id",
            post_id,
            tag_id,
        ),
    )
