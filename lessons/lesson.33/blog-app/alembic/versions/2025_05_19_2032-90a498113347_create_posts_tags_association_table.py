"""create posts tags association table

Revision ID: 90a498113347
Revises: 9c8f84f7afe1
Create Date: 2025-05-19 20:32:27.016628

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "90a498113347"
down_revision: Union[str, None] = "9c8f84f7afe1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "posts_tags_association",
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
            "post_id",
            "tag_id",
            name=op.f("pk_posts_tags_association"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts_tags_association")
