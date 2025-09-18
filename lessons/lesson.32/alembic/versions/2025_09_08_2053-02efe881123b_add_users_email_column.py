"""add users.email column

Revision ID: 02efe881123b
Revises: 9bc596839c76
Create Date: 2025-09-08 20:53:10.541396

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "02efe881123b"
down_revision: Union[str, Sequence[str], None] = "9bc596839c76"
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
