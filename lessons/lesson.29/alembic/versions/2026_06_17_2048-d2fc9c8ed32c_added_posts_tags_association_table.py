"""Added posts_tags_association table

Revision ID: d2fc9c8ed32c
Revises: c211b68f5571
Create Date: 2026-06-17 20:48:58.188030

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "d2fc9c8ed32c"
down_revision: Union[str, Sequence[str], None] = "c211b68f5571"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
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
    op.drop_table("posts_tags_association")
