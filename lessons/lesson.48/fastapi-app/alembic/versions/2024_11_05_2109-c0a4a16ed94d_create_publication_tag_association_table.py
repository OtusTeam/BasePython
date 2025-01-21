"""create publication_tag_association table

Revision ID: c0a4a16ed94d
Revises: 7e99be1d877b
Create Date: 2024-11-05 21:09:36.301973

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c0a4a16ed94d"
down_revision: Union[str, None] = "7e99be1d877b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "publication_tag_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("publication_id", sa.Integer(), nullable=False),
        sa.Column("tag_id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["publication_id"],
            ["publication.id"],
            name=op.f("fk_publication_tag_association_publication_id_publication"),
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tag.id"],
            name=op.f("fk_publication_tag_association_tag_id_tag"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_publication_tag_association")),
        sa.UniqueConstraint(
            "publication_id",
            "tag_id",
            name=op.f("uq_publication_tag_association_publication_id"),
        ),
    )


def downgrade() -> None:
    op.drop_table("publication_tag_association")
