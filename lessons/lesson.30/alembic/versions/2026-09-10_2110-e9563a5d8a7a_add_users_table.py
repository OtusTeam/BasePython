"""Add users table

Revision ID: e9563a5d8a7a
Revises:
Create Date: 2026-09-10 21:10:04.449873

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "e9563a5d8a7a"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.Integer(),
            sa.Identity(always=True),
            nullable=False,
        ),
        sa.Column("username", sa.Text(), nullable=False),
        sa.Column(
            "full_name",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.CheckConstraint(
            "length(full_name) <= 100",
            name=op.f("ck_users_full_name_length"),
        ),
        sa.CheckConstraint(
            "length(username) <= 32",
            name=op.f("ck_users_username_length"),
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_users"),
        ),
        sa.UniqueConstraint(
            "username",
            name=op.f("uq_users_username"),
        ),
    )


def downgrade() -> None:
    op.drop_table("users")
