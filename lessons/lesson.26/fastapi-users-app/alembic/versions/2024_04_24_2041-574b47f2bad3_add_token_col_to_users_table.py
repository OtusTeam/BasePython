"""add token col to users table

Revision ID: 574b47f2bad3
Revises: e1360a08001b
Create Date: 2024-04-24 20:41:53.485903

"""

from typing import (
    Sequence,
    Union,
)

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "574b47f2bad3"
down_revision: Union[str, None] = "e1360a08001b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "token",
            sa.String(length=36),
            nullable=True,
        ),
    )
    op.create_unique_constraint(
        op.f("uq_users_token"),
        "users",
        ["token"],
    )


def downgrade() -> None:
    op.drop_constraint(op.f("uq_users_token"), "users", type_="unique")
    op.drop_column("users", "token")
