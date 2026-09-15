"""create tags table

Revision ID: 4345de281c86
Revises: a0cb1175252e
Create Date: 2026-09-15 20:33:06.325457

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "4345de281c86"
down_revision: Union[str, Sequence[str], None] = "a0cb1175252e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tags",
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("display_name", sa.Text(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.CheckConstraint(
            "length(display_name) BETWEEN 1 AND 100",
            name=op.f("ck_tags_display_name_length"),
        ),
        sa.CheckConstraint(
            "length(name) BETWEEN 1 AND 64",
            name=op.f("ck_tags_name_length"),
        ),
        sa.PrimaryKeyConstraint("name", name=op.f("pk_tags")),
        sa.UniqueConstraint(
            "display_name",
            name=op.f("uq_tags_display_name"),
        ),
    )


def downgrade() -> None:
    op.drop_table("tags")
