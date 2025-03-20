"""create table users

Revision ID: f4531d355c26
Revises:
Create Date: 2025-03-20 21:04:46.358637

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f4531d355c26"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "username",
            sa.String(length=32),
            nullable=False,
        ),
        sa.Column(
            "email",
            sa.String(length=120),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_users"),
        ),
        sa.UniqueConstraint(
            "email",
            name=op.f("uq_users_email"),
        ),
        sa.UniqueConstraint(
            "username",
            name=op.f("uq_users_username"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
