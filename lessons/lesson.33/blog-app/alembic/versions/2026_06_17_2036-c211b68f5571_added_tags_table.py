"""Added tags table

Revision ID: c211b68f5571
Revises: ef5f819366e4
Create Date: 2026-06-17 20:36:14.376414

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "c211b68f5571"
down_revision: Union[str, Sequence[str], None] = "ef5f819366e4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tags",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("slug", sa.Text(), nullable=False),
        sa.Column("display_name", sa.Text(), nullable=False),
        sa.CheckConstraint(
            "length(display_name) <= 64",
            name=op.f("ck_tags_display_name_length"),
        ),
        sa.CheckConstraint("length(slug) <= 32", name=op.f("ck_tags_slug_length")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_tags")),
        sa.UniqueConstraint("display_name", name=op.f("uq_tags_display_name")),
        sa.UniqueConstraint("slug", name=op.f("uq_tags_slug")),
    )


def downgrade() -> None:
    op.drop_table("tags")
