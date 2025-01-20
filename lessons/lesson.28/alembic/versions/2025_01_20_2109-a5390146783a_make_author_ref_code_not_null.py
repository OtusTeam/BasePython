"""make author.ref_code not null

Revision ID: a5390146783a
Revises: 14bc8e509acf
Create Date: 2025-01-20 21:09:27.112722

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a5390146783a"
down_revision: Union[str, None] = "14bc8e509acf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    table = sa.Table(
        "author",
        sa.MetaData(),
        sa.Column("id", sa.Integer()),
        sa.Column("ref_code", sa.String()),
    )
    # substring(md5(random()::VARCHAR), 1, 6)
    rnd_val = sa.func.substring(
        sa.func.md5(
            sa.func.cast(
                sa.func.random(),
                sa.String(),
            ),
        ),
        # from the first
        1,
        # length 6
        6,
    )
    stmt = (
        sa.update(table)
        .where(
            table.c.ref_code.is_(None),
        )
        .values(
            {
                # table.c.email: sa.func.concat(
                #     sa.func.lower(table.c.username),
                #     '@example.com',
                # )
                table.c.ref_code: rnd_val,
            }
        )
    )
    op.execute(stmt)
    op.alter_column(
        "author",
        "ref_code",
        existing_type=sa.VARCHAR(),
        nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "author",
        "ref_code",
        existing_type=sa.VARCHAR(),
        nullable=True,
    )
