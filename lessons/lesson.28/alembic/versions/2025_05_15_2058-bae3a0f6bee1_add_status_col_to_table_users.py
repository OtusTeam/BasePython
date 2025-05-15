"""add status col to table users

Revision ID: bae3a0f6bee1
Revises: 8764cd527aee
Create Date: 2025-05-15 20:58:41.153278

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bae3a0f6bee1"
down_revision: Union[str, None] = "8764cd527aee"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "users",
        sa.Column("status", sa.String(length=10), nullable=True),
    )
    op.create_foreign_key(
        op.f("fk_users_status_user_status"),
        "users",
        "user_status",
        ["status"],
        ["name"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        op.f("fk_users_status_user_status"),
        "users",
        type_="foreignkey",
    )
    op.drop_column("users", "status")
