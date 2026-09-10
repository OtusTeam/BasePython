"""Add email col to users table

Revision ID: b6e7801a687b
Revises: e9563a5d8a7a
Create Date: 2026-09-10 21:11:10.847104

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "b6e7801a687b"
down_revision: Union[str, Sequence[str], None] = "e9563a5d8a7a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("email", sa.Text(), nullable=True),
    )
    op.create_unique_constraint(op.f("uq_users_email"), "users", ["email"])


def downgrade() -> None:
    op.drop_constraint(op.f("uq_users_email"), "users", type_="unique")
    op.drop_column("users", "email")
