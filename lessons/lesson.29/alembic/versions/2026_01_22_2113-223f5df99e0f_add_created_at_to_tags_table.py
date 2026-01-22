"""add created_at to tags table

Revision ID: 223f5df99e0f
Revises: 1f83be10e1c9
Create Date: 2026-01-22 21:13:08.435542

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "223f5df99e0f"
down_revision: Union[str, Sequence[str], None] = "1f83be10e1c9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "tags",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("tags", "created_at")
