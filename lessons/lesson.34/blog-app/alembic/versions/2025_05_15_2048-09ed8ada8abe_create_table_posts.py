"""create table posts

Revision ID: 09ed8ada8abe
Revises: 314047ac0790
Create Date: 2025-05-15 20:48:31.248240

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "09ed8ada8abe"
down_revision: Union[str, None] = "314047ac0790"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "title",
            sa.String(length=120),
            server_default="",
            nullable=False,
        ),
        sa.Column("body", sa.Text(), server_default="", nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name=op.f("fk_posts_user_id_users"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_posts")),
    )
    op.create_index(op.f("ix_posts_title"), "posts", ["title"], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f("ix_posts_title"), table_name="posts")
    op.drop_table("posts")
