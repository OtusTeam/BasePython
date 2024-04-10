"""title on posts now 80

Revision ID: c8f3228ed335
Revises: d7c62b9242fd
Create Date: 2024-04-10 20:39:23.814578

"""

from typing import (
    Sequence,
    Union,
)

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "c8f3228ed335"
down_revision: Union[str, None] = "d7c62b9242fd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

table_name = "posts"


def upgrade() -> None:
    # op.execute("""
    #     UPDATE posts
    #     SET title = substring(title, 0, 81)
    #     WHERE length(title) > 80
    # """)

    metadata = sa.MetaData()
    # metadata.reflect(bind=op.get_bind())
    # table_posts = metadata.tables[table_name]
    # table_posts = sa.Table(table_name, metadata, autoload_with=op.get_bind())

    table_posts = sa.Table(
        table_name,
        metadata,
        sa.Column("id", sa.Integer()),
        sa.Column("title", sa.String()),
    )
    stmt = (
        sa.update(table_posts)
        .where(sa.func.length(table_posts.c.title) > 80)
        .values({
            table_posts.c.title: sa.func.substring(table_posts.c.title, 0, 81)
        })
    )
    op.execute(stmt)

    op.alter_column(
        table_name,
        "title",
        existing_type=sa.String(length=100),
        type_=sa.String(length=80),
        existing_nullable=False,
        existing_server_default=sa.text("''::character varying"),
    )


def downgrade() -> None:
    op.alter_column(
        table_name,
        "title",
        existing_type=sa.String(length=80),
        type_=sa.String(length=100),
        existing_nullable=False,
        existing_server_default=sa.text("''::character varying"),
    )
