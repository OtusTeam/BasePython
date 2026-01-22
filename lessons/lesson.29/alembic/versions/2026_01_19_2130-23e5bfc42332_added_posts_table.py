"""Added posts table

Revision ID: 23e5bfc42332
Revises: 1d83fb123341
Create Date: 2026-01-19 21:30:47.816211

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "23e5bfc42332"
down_revision: Union[str, Sequence[str], None] = "1d83fb123341"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "title",
            sa.String(length=100),
            server_default="",
            nullable=False,
        ),
        sa.Column(
            "text",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name=op.f("fk_posts_user_id_users"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_posts")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts")
