from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
from models.mixins import IdIntPk


class PostTagAssociation(IdIntPk, Base):
    __tablename__ = "posts_tags_association"

    post_id: Mapped[int] = mapped_column(
        ForeignKey("post.id"),
    )
    tag_name: Mapped[str] = mapped_column(
        ForeignKey("tag.name"),
    )
    # added_at: Mapped[datetime]
    # added_by: Mapped[User]

    __table_args__ = (
        UniqueConstraint(
            post_id,
            tag_name,
            name="unique_pair",
        ),
    )
