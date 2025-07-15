"""require users email

Revision ID: b0eea4ddd07e
Revises: afe5f2bb7d8a
Create Date: 2025-07-15 20:49:39.669212

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b0eea4ddd07e"
down_revision: Union[str, Sequence[str], None] = "afe5f2bb7d8a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    metadata = sa.MetaData()
    table_users = sa.Table(
        "users",
        metadata,
        sa.Column("id", sa.Integer),
        sa.Column("username", sa.String),
        sa.Column("email", sa.String),
    )

    update_statement = (
        sa.update(
            table_users,
        )
        .where(
            table_users.c.email.is_(None),
        )
        .values(
            {
                table_users.c.email: (table_users.c.username + "@invalid.email"),
            }
        )
    )

    op.execute(update_statement)

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
