"""create posts-tags assoc table

Revision ID: a69d65327702
Revises: 4345de281c86
Create Date: 2026-09-15 20:49:36.712746

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "a69d65327702"
down_revision: Union[str, Sequence[str], None] = "4345de281c86"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts_tags_association_table",
        sa.Column("post_id", sa.Integer(), nullable=False),
        sa.Column("tag_name", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["posts.id"],
            name=op.f("fk_posts_tags_association_table_post_id_posts"),
        ),
        sa.ForeignKeyConstraint(
            ["tag_name"],
            ["tags.name"],
            name=op.f("fk_posts_tags_association_table_tag_name_tags"),
        ),
        sa.PrimaryKeyConstraint(
            "post_id",
            "tag_name",
            name=op.f("pk_posts_tags_association_table"),
        ),
    )


def downgrade() -> None:
    op.drop_table("posts_tags_association_table")
