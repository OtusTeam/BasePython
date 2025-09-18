from sqlalchemy import (
    Table,
    ForeignKey,
    Column,
    Integer,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import CITEXT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base
from models.mixins.id_int_pk import IdIntPkMixin


class PostTagsAssociation(IdIntPkMixin, Base):
    __tablename__ = "posts_tags_association"

    post_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("posts.id"),
    )
    tag_name: Mapped[str] = mapped_column(
        CITEXT(32),
        ForeignKey("tags.name"),
    )

    __table_args__ = (
        UniqueConstraint(
            post_id,
            tag_name,
        ),
    )
