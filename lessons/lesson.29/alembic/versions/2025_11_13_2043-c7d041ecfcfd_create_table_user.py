"""create table user

Revision ID: c7d041ecfcfd
Revises:
Create Date: 2025-11-13 20:43:46.779637

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c7d041ecfcfd"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "user",
        sa.Column(
            "id",
            sa.BigInteger(),
            sa.Identity(always=True),
            nullable=False,
        ),
        sa.Column("username", sa.Text(), nullable=False),
        sa.Column("email", sa.Text(), nullable=True),
        sa.Column(
            "full_name",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_user"),
        ),
        sa.UniqueConstraint(
            "email",
            name=op.f("uq_user_email"),
        ),
        sa.UniqueConstraint(
            "username",
            name=op.f("uq_user_username"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("user")
