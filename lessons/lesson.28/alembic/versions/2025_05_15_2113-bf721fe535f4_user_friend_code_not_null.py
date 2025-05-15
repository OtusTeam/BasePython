"""user friend code not null

Revision ID: bf721fe535f4
Revises: 8c1ceb690e3d
Create Date: 2025-05-15 21:13:13.791897

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bf721fe535f4"
down_revision: Union[str, None] = "8c1ceb690e3d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    table_users = sa.Table(
        "users",
        sa.MetaData(),
        sa.Column("id", sa.Integer),
        sa.Column("friend_code", sa.String),
    )
    random_chars = sa.func.substring(
        sa.func.md5(
            sa.func.cast(
                sa.func.random(),
                sa.String(),
            )
        ),
        # start from the first char
        1,
        # length 6
        6,
    )
    update_statement = (
        sa.update(
            table_users,
        )
        .where(
            table_users.c.friend_code.is_(None),
        )
        .values(
            {
                table_users.c.friend_code: random_chars,
            }
        )
    )
    op.execute(update_statement)
    op.alter_column(
        "users",
        "friend_code",
        existing_type=sa.VARCHAR(length=20),
        nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "users",
        "friend_code",
        existing_type=sa.VARCHAR(length=20),
        nullable=True,
    )
