"""add col full_name to users

Revision ID: e770c0edaaa8
Revises: b39bb783280d
Create Date: 2025-03-20 21:16:34.823957

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e770c0edaaa8"
down_revision: Union[str, None] = "b39bb783280d"
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
