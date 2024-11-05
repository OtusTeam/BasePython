"""add promocode col to authors table

Revision ID: d11bee117a5d
Revises: eb4835baddf1
Create Date: 2024-11-01 21:16:13.743561

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Integer

# revision identifiers, used by Alembic.
revision: str = "d11bee117a5d"
down_revision: Union[str, None] = "eb4835baddf1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "author", sa.Column("promocode", sa.String(), nullable=True)
    )
    op.create_unique_constraint(
        op.f("uq_author_promocode"), "author", ["promocode"]
    )
    table = sa.Table(
        "author",
        sa.MetaData(),
        sa.Column("id", Integer, primary_key=True),
        sa.Column("promocode", sa.String(), nullable=True),
    )

    # SELECT substring(md5(random()::text), 1, 6) AS random_string;
    rnd_val = sa.func.substring(
        sa.func.md5(sa.func.cast(sa.func.random(), sa.String)),
        # from 1
        1,
        # to 6
        6,
    )

    stmt = sa.update(table).where(
        table.c.promocode.is_(None),
    ).values({
        table.c.promocode: rnd_val,
    })
    op.execute(stmt)
    op.alter_column(
        "author",
        "promocode",
        existing_type=sa.String(),
        nullable=False,
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("uq_author_promocode"), "author", type_="unique"
    )
    op.drop_column("author", "promocode")
