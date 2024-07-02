"""create posts_tags_association table

Revision ID: b5f241c8c0e6
Revises: 0de8895d4781
Create Date: 2024-07-02 20:22:23.682962

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b5f241c8c0e6"
down_revision: Union[str, None] = "0de8895d4781"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
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
            "id", name=op.f("pk_posts_tags_association")
        ),
        sa.UniqueConstraint(
            "post_id",
            "tag_id",
            name=op.f("uq_posts_tags_association_post_id_tag_id"),
        ),
    )


def downgrade() -> None:
    op.drop_table("posts_tags_association")
