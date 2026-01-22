"""Added email col to users table

Revision ID: 1d83fb123341
Revises: 46674e28d78a
Create Date: 2026-01-19 21:30:02.630904

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1d83fb123341"
down_revision: Union[str, Sequence[str], None] = "46674e28d78a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "users",
        sa.Column("email", sa.String(length=150), nullable=True),
    )
    op.create_unique_constraint(op.f("uq_users_email"), "users", ["email"])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(op.f("uq_users_email"), "users", type_="unique")
    op.drop_column("users", "email")
