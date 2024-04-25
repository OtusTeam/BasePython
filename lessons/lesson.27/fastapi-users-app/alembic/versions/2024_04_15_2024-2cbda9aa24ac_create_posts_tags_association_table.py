"""create posts tags association table

Revision ID: 2cbda9aa24ac
Revises: 668e519dd476
Create Date: 2024-04-15 20:24:20.095267

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2cbda9aa24ac"
down_revision: Union[str, None] = "668e519dd476"
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
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tags.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("post_id", "tag_id", name="unique_ix_post_tag"),
    )


def downgrade() -> None:
    op.drop_table("posts_tags_association")
