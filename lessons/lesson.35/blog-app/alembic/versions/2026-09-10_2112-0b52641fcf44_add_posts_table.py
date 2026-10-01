"""Add posts table

Revision ID: 0b52641fcf44
Revises: b6e7801a687b
Create Date: 2026-09-10 21:12:55.085685

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "0b52641fcf44"
down_revision: Union[str, Sequence[str], None] = "b6e7801a687b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column(
            "id",
            sa.Integer(),
            sa.Identity(always=True),
            nullable=False,
        ),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("body", sa.Text(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.CheckConstraint(
            "length(title) <= 80",
            name=op.f("ck_posts_title_length"),
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name=op.f("fk_posts_user_id_users"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_posts")),
    )


def downgrade() -> None:
    op.drop_table("posts")
