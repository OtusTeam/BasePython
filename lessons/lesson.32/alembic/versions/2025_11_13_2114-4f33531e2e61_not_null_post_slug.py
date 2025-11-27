"""not null post.slug

Revision ID: 4f33531e2e61
Revises: 15b552bb6f57
Create Date: 2025-11-13 21:14:43.842095

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4f33531e2e61"
down_revision: Union[str, Sequence[str], None] = "15b552bb6f57"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    metadata = sa.MetaData()
    post_table = sa.Table(
        "post",
        metadata,
        sa.Column("id", sa.BigInteger),
        sa.Column("title", sa.Text),
        sa.Column("slug", sa.Text),
    )
    slug_expr = sa.func.regexp_replace(
        sa.func.regexp_replace(
            sa.func.lower(post_table.c.title),
            sa.literal("[^a-z0-9]+"),
            sa.literal("-"),
            sa.literal("g"),
        ),
        sa.literal("-"),
        sa.literal("-"),
    )
    statement = (
        sa.update(
            post_table,
        )
        .where(post_table.c.slug.is_(None))
        .values(
            {
                post_table.c.slug: slug_expr,
            }
        )
    )
    op.execute(statement)

    op.alter_column(
        "post",
        "slug",
        existing_type=sa.Text(),
        nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "post",
        "slug",
        existing_type=sa.Text(),
        nullable=True,
    )
