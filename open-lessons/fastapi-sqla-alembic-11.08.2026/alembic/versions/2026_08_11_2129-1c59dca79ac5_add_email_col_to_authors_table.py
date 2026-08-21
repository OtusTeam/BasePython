"""
Add email col to authors table

Revision ID: 1c59dca79ac5
Revises: 56ff499433b6
Create Date: 2026-08-11 21:29:49.056183
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1c59dca79ac5"
down_revision: str | Sequence[str] | None = "56ff499433b6"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("author", sa.Column("email", sa.Text(), nullable=True))
    op.create_unique_constraint(op.f("uq_author_email"), "author", ["email"])


def downgrade() -> None:
    op.drop_constraint(op.f("uq_author_email"), "author", type_="unique")
    op.drop_column("author", "email")
