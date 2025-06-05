"""create posts tags association table

Revision ID: c2035423b06f
Revises: e3b2d698ca83
Create Date: 2025-05-19 21:07:25.459523

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c2035423b06f"
down_revision: Union[str, None] = "e3b2d698ca83"
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
        sa.PrimaryKeyConstraint("id", name=op.f("pk_posts_tags_association")),
        sa.UniqueConstraint(
            "post_id",
            "tag_id",
            name=op.f("uq_posts_tags_association_post_id"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts_tags_association")
