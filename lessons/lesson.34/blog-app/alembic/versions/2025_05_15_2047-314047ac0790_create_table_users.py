"""create table users

Revision ID: 314047ac0790
Revises:
Create Date: 2025-05-15 20:47:26.383043

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "314047ac0790"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=32), nullable=False),
        sa.Column("email", sa.String(length=150), nullable=True),
        sa.Column(
            "full_name",
            sa.String(),
            server_default="",
            nullable=False,
        ),
        sa.Column("friend_code", sa.String(length=20), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
        sa.UniqueConstraint("email", name=op.f("uq_users_email")),
        sa.UniqueConstraint("friend_code", name=op.f("uq_users_friend_code")),
        sa.UniqueConstraint("username", name=op.f("uq_users_username")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
