"""add posts_tags table

Revision ID: 0fb9701f23fa
Revises: 86213e6fdbea
Create Date: 2026-03-20 20:51:19.479286

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "0fb9701f23fa"
down_revision: Union[str, Sequence[str], None] = "86213e6fdbea"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "posts_tags_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("post_id", sa.Integer(), nullable=False),
        sa.Column("tag_name", postgresql.CITEXT(), nullable=False),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["post.id"],
            name=op.f("fk_posts_tags_association_post_id_post"),
        ),
        sa.ForeignKeyConstraint(
            ["tag_name"],
            ["tag.name"],
            name=op.f("fk_posts_tags_association_tag_name_tag"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_posts_tags_association")),
        sa.UniqueConstraint(
            "post_id",
            "tag_name",
            name="unique_pair",
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts_tags_association")
