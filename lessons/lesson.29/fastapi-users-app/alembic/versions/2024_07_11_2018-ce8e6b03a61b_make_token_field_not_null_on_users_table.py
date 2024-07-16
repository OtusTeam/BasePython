"""make token field not null on users table

Revision ID: ce8e6b03a61b
Revises: 6dc8719d3457
Create Date: 2024-07-11 20:18:30.919198

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ce8e6b03a61b"
down_revision: Union[str, None] = "6dc8719d3457"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


table_name = "users"


def upgrade() -> None:
    metadata = sa.MetaData()
    table_users = sa.Table(
        table_name,
        metadata,
        sa.Column("id", sa.Integer()),
        sa.Column("token", sa.String()),
    )

    stmt = (
        sa.update(table_users)
        .where(
            # update only NULL fields
            table_users.c.token.is_(None),
        )
        .values(
            {
                table_users.c.token: sa.func.gen_random_uuid(),
            }
        )
    )
    op.execute(stmt)

    op.alter_column(
        table_name,
        "token",
        existing_type=sa.VARCHAR(),
        nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "users",
        "token",
        existing_type=sa.VARCHAR(),
        nullable=True,
    )
