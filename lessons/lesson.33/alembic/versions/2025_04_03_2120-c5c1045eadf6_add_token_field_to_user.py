"""add token field to user

Revision ID: c5c1045eadf6
Revises: c432ed836fb3
Create Date: 2025-04-03 21:20:00.190243

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c5c1045eadf6"
down_revision: Union[str, None] = "c432ed836fb3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "users",
        sa.Column(
            "token",
            sa.String(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
            unique=True,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("users", "token")
