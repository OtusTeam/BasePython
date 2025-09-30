"""add created_at to user

Revision ID: 65e2f8cf8494
Revises: 844cb55c7859
Create Date: 2025-09-18 20:53:37.032138

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "65e2f8cf8494"
down_revision: Union[str, Sequence[str], None] = "844cb55c7859"
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
