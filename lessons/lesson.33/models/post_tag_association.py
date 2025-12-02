from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped

from models.base import Base
from models.mixins import CreatedAtMixin, IdIntPKMixin


# post_tag_association_table = Table(
#     "post_tag_association",
#     Base.metadata,
#     Column("post_id", ForeignKey("post.id"), primary_key=True),
#     Column("tag_id", ForeignKey("tag.id"), primary_key=True),
# )


class PostTagAssociation(IdIntPKMixin, CreatedAtMixin, Base):
    __tablename__ = "post_tag_association"

    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"))

    __table_args__ = (
        UniqueConstraint(
            post_id,
            tag_id,
            name="post_tag_pair",
        ),
    )
