"""add col email to users table

Revision ID: 43ce78fc9340
Revises: 2ab278d05356
Create Date: 2025-07-15 20:36:29.916543

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "43ce78fc9340"
down_revision: Union[str, Sequence[str], None] = "2ab278d05356"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "users",
        sa.Column(
            "email",
            sa.String(length=150),
            nullable=True,
        ),
    )
    op.create_unique_constraint(
        op.f("uq_users_email"),
        "users",
        ["email"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        op.f("uq_users_email"),
        "users",
        type_="unique",
    )
    op.drop_column(
        "users",
        "email",
    )
