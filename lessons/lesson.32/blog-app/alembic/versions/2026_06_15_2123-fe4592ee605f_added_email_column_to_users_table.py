"""Added email column to users table

Revision ID: fe4592ee605f
Revises: 544cbac15bd9
Create Date: 2026-06-15 21:23:02.109290

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "fe4592ee605f"
down_revision: Union[str, Sequence[str], None] = "544cbac15bd9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "users",
        sa.Column("email", sa.String(length=150), nullable=True),
    )
    op.create_unique_constraint(
        op.f("uq_users_email"),
        "users",
        ["email"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(op.f("uq_users_email"), "users", type_="unique")
    op.drop_column("users", "email")
