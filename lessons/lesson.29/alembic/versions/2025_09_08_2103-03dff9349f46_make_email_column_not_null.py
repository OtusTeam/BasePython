"""make email column not null

Revision ID: 03dff9349f46
Revises: 02efe881123b
Create Date: 2025-09-08 21:03:12.180455

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "03dff9349f46"
down_revision: Union[str, Sequence[str], None] = "02efe881123b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    metadata = sa.MetaData()
    table_users = sa.Table(
        "users",
        metadata,
        sa.Column("id", sa.Integer),
        sa.Column("email", sa.String),
        sa.Column("username", sa.String),
    )
    statement = (
        sa.update(table_users)
        .where(
            table_users.c.email.is_(None),
        )
        .values(
            {
                table_users.c.email: (table_users.c.username + "@invalid.mail"),
            }
        )
    )
    op.execute(statement)
    op.alter_column(
        "users",
        "email",
        existing_type=sa.String(length=150),
        nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "users",
        "email",
        existing_type=sa.String(length=150),
        nullable=True,
    )
