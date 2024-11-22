from sqlalchemy import ForeignKey, UniqueConstraint

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base
from .mixins.created_at_mixin import CreatedAtMixin
from .mixins.int_pk_mixin import IntPkMixin


class PublicationTagAssociation(IntPkMixin, CreatedAtMixin, Base):
    __tablename__ = "publication_tag_association"

    publication_id: Mapped[int] = mapped_column(
        ForeignKey("publication.id"),
    )
    tag_id: Mapped[int] = mapped_column(
        ForeignKey("tag.id"),
    )

    __table_args__ = (
        UniqueConstraint(
            # "publication_id",
            # "tag_id",
            publication_id,
            tag_id,
            # name="publication_tag_association_publication_id_tag_id",
        ),
    )
