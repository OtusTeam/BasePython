"""add token field to users table

Revision ID: 6dc8719d3457
Revises: b5f241c8c0e6
Create Date: 2024-07-11 20:14:16.945873

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6dc8719d3457"
down_revision: Union[str, None] = "b5f241c8c0e6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users", sa.Column("token", sa.String(), nullable=True)
    )
    op.create_unique_constraint(
        op.f("uq_users_token"), "users", ["token"]
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("uq_users_token"), "users", type_="unique"
    )
    op.drop_column("users", "token")
