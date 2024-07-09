"""not null ref code on users table

Revision ID: 1d0e0468114b
Revises: 0bee249a8c0e
Create Date: 2024-06-28 20:45:13.241636

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1d0e0468114b"
down_revision: Union[str, None] = "0bee249a8c0e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


table_name = "users"


def upgrade() -> None:
    metadata = sa.MetaData()
    # metadata.reflect(op.get_bind())
    # table_users = metadata.tables[table_name]
    table_users = sa.Table(
        "users",
        metadata,
        sa.Column("id", sa.Integer()),
        sa.Column("username", sa.String()),
        sa.Column("ref_code", sa.String()),
    )

    expression_random_ref_code = (
        # substring(md5(username), 1, 6)
        sa.func.substring(
            # value
            sa.func.md5(table_users.c.username),
            # start from start
            1,
            # limit 6 chars
            6,
        )
    )
    stmt = (
        sa.update(table_users)
        .where(
            # update only NULL fields
            table_users.c.ref_code.is_(None),
        )
        .values({
            table_users.c.ref_code: expression_random_ref_code,
        })
    )
    op.execute(stmt)

    op.alter_column(
        table_name,
        "ref_code",
        existing_type=sa.String(),
        nullable=False,
    )


def downgrade() -> None:
    # при желании делаем обнуление колонки
    op.alter_column(
        table_name,
        "ref_code",
        existing_type=sa.String(),
        nullable=True,
    )
