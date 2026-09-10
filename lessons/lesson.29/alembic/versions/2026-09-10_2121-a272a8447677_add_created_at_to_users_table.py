"""Add created_at to users table

Revision ID: a272a8447677
Revises: 0b52641fcf44
Create Date: 2026-09-10 21:21:39.754521

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "a272a8447677"
down_revision: Union[str, Sequence[str], None] = "0b52641fcf44"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column("users", "created_at")
