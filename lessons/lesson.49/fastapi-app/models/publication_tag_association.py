from sqlalchemy import (
    Table,
    Column,
    Integer,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from . import Base

# publication_tag_association_table = Table(
#     "publication_tag_association",
#     Base.metadata,
#     Column("id", Integer, primary_key=True),
#     Column("publication_id", ForeignKey("publication.id"), nullable=False),
#     Column("tag_id", ForeignKey("tag.id"), nullable=False),
#     UniqueConstraint("publication_id", "tag_id"),
# )


class PublicationTagAssociation(Base):
    __tablename__ = "publication_tag_association"
    publication_id: Mapped[int] = mapped_column(
        ForeignKey("publication.id"),
    )
    tag_id: Mapped[int] = mapped_column(
        ForeignKey("tag.id"),
    )

    __table_args__ = (
        #
        UniqueConstraint(
            # "publication_id",
            # "tag_id",
            publication_id,
            tag_id,
        ),
    )
