"""add length constraint to user.username

Revision ID: 76b622877569
Revises: c0f46d3bfc1f
Create Date: 2025-11-13 21:02:57.076973

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "76b622877569"
down_revision: Union[str, Sequence[str], None] = "c0f46d3bfc1f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_check_constraint(
        "username_length",
        "user",
        sa.and_(
            sa.func.char_length(sa.text("username")) <= 32,
            sa.func.char_length(sa.text("username")) >= 3,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "username_length",
        "user",
        type_="check",
    )
