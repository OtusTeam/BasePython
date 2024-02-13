from sqlalchemy import Table, Column, ForeignKey, UniqueConstraint

from models import Base
from models.mixins.created_at_mixin import CreatedAtMixin

# posts_tags_association_table = Table(
#     "posts_tags_association",
#     Base.metadata,
#     # Column("id", primary_key=True),
#     Column(
#         "post_id",
#         ForeignKey("posts.id"),
#         # nullable=False,
#         primary_key=True,
#     ),
#     Column(
#         "tag_id",
#         ForeignKey("tags.id"),
#         #         nullable=False,
#         primary_key=True,
#     ),
#
#     UniqueConstraint(
#         "post_id",
#         "tag_id",
#         name="unique_posts_tags_association",
#     ),
# )


class PostsTagsAssociation(CreatedAtMixin, Base):
    __tablename__ = "posts_tags_association"
    # __table_args__ = (
    #     UniqueConstraint(
    #         "post_id",
    #         "tag_id",
    #         name="unique_posts_tags_association",
    #     ),
    # )
    post_id = Column(
        ForeignKey("posts.id"),
        nullable=False,
    )
    tag_id = Column(
        ForeignKey("tags.id"),
        nullable=False,
    )
    __table_args__ = (
        UniqueConstraint(
            post_id,
            tag_id,
            name="unique_posts_tags_association",
        ),
    )
