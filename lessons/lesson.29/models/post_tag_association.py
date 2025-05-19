from sqlalchemy import Table, Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped

from models.base import Base


# posts_tags_association = Table(
#     "posts_tags_association",
#     Base.metadata,
#     Column("post_id", ForeignKey("posts.id"), primary_key=True),
#     Column("tag_id", ForeignKey("tags.id"), primary_key=True),
# )


class PostTagAssociation(Base):
    __tablename__ = "posts_tags_association"

    post_id: Mapped[int] = mapped_column(
        ForeignKey("posts.id"),
    )
    tag_id: Mapped[int] = mapped_column(
        ForeignKey("tags.id"),
    )

    __table_args__ = (
        #
        UniqueConstraint(
            # "post_id",
            # "tag_id",
            post_id,
            tag_id,
        ),
    )
