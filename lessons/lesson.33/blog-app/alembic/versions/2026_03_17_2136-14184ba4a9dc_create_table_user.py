"""create table user

Revision ID: 14184ba4a9dc
Revises:
Create Date: 2026-03-17 21:36:08.927909

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "14184ba4a9dc"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.Text(), nullable=False),
        sa.Column("full_name", sa.Text(), server_default="", nullable=False),
        sa.CheckConstraint(
            "length(full_name) <= 100",
            name=op.f("ck_user_full_name_max_length"),
        ),
        sa.CheckConstraint(
            "length(username) <= 32",
            name=op.f("ck_user_username_max_length"),
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_user"),
        ),
        sa.UniqueConstraint(
            "username",
            name=op.f("uq_user_username"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("user")
