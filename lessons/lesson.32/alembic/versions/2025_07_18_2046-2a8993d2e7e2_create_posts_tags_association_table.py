"""Create posts_tags_association table

Revision ID: 2a8993d2e7e2
Revises: 14db2566568f
Create Date: 2025-07-18 20:46:26.877410

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2a8993d2e7e2"
down_revision: Union[str, Sequence[str], None] = "14db2566568f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "posts_tags_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("post_id", sa.Integer(), nullable=False),
        sa.Column("tag_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["posts.id"],
            name=op.f("fk_posts_tags_association_post_id_posts"),
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tags.id"],
            name=op.f("fk_posts_tags_association_tag_id_tags"),
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_posts_tags_association"),
        ),
        sa.UniqueConstraint(
            "post_id",
            "tag_id",
            name=op.f("uq_posts_tags_association_post_id"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts_tags_association")
