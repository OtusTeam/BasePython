"""
Add authors table

Revision ID: 2726350f8fbc
Revises:
Create Date: 2026-08-11 21:21:08.254124
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2726350f8fbc"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "author",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.CheckConstraint(
            "length(name) <= 120", name=op.f("ck_author_ck_author_name_length")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_author")),
        sa.UniqueConstraint("name", name=op.f("uq_author_name")),
    )


def downgrade() -> None:
    op.drop_table("author")
