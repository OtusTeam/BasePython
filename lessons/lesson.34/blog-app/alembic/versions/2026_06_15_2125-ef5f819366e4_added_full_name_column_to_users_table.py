"""Added full_name column to users table

Revision ID: ef5f819366e4
Revises: 9e7d908b8f2e
Create Date: 2026-06-15 21:25:25.796792

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "ef5f819366e4"
down_revision: Union[str, Sequence[str], None] = "9e7d908b8f2e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "users",
        sa.Column(
            "full_name",
            sa.String(length=100),
            server_default="",
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("users", "full_name")
