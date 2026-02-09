"""add created_at col to users

Revision ID: 159cd6e87db4
Revises: 223f5df99e0f
Create Date: 2026-02-02 20:52:08.990356

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "159cd6e87db4"
down_revision: Union[str, Sequence[str], None] = "223f5df99e0f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "users",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("users", "created_at")
