"""add col email to user

Revision ID: b1893ec4e76c
Revises: 97df48964125
Create Date: 2026-03-17 21:38:45.425741

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "b1893ec4e76c"
down_revision: Union[str, Sequence[str], None] = "97df48964125"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "user",
        sa.Column(
            "email",
            sa.Text(),
            nullable=True,
        ),
    )
    op.create_unique_constraint(
        op.f("uq_user_email"),
        "user",
        ["email"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        op.f("uq_user_email"),
        "user",
        type_="unique",
    )
    op.drop_column("user", "email")
