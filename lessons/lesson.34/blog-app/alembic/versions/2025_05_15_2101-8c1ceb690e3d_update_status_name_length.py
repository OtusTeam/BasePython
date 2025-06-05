"""update status name length

Revision ID: 8c1ceb690e3d
Revises: bae3a0f6bee1
Create Date: 2025-05-15 21:01:06.287591

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8c1ceb690e3d"
down_revision: Union[str, None] = "bae3a0f6bee1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "user_status",
        "name",
        existing_type=sa.VARCHAR(length=10),
        type_=sa.String(length=20),
        existing_nullable=False,
    )
    op.alter_column(
        "users",
        "status",
        existing_type=sa.VARCHAR(length=10),
        type_=sa.String(length=20),
        existing_nullable=True,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "users",
        "status",
        existing_type=sa.String(length=20),
        type_=sa.VARCHAR(length=10),
        existing_nullable=True,
    )
    op.alter_column(
        "user_status",
        "name",
        existing_type=sa.String(length=20),
        type_=sa.VARCHAR(length=10),
        existing_nullable=False,
    )
