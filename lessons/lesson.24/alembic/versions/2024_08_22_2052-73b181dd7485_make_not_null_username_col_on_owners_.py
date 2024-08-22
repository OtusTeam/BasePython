"""Make not null username col on owners table

Revision ID: 73b181dd7485
Revises: 1b73fc0146b7
Create Date: 2024-08-22 20:52:27.343881

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "73b181dd7485"
down_revision: Union[str, None] = "1b73fc0146b7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    metadata = sa.MetaData()
    # metadata.reflect(bind=op.get_bind())
    table_owners = sa.Table(
        "owners",
        metadata,
        sa.Column("id", sa.Integer()),
        sa.Column("username", sa.String()),
    )

    stmt_set_random_usernames = (
        sa.update(
            table_owners,
        )
        .where(
            table_owners.c.username.is_(None),
        )
        .values(
            {
                # SUBSTR(md5(id::VARCHAR), 1, 6)
                table_owners.c.username: (
                    sa.func.substring(
                        # take hash from id
                        sa.func.md5(
                            # cast int as str
                            sa.cast(table_owners.c.id, sa.String())
                        ),
                        # start from 1
                        1,
                        # limit to 6
                        6,
                        # no comma!
                    )
                ),
            }
        )
    )
    op.execute(stmt_set_random_usernames)

    op.alter_column(
        "owners",
        "username",
        existing_type=sa.VARCHAR(),
        nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "owners",
        "username",
        existing_type=sa.VARCHAR(),
        nullable=True,
    )
