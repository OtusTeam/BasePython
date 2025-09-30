"""create posts_tags association table

Revision ID: 844cb55c7859
Revises: 802ef522353b
Create Date: 2025-09-10 21:20:36.128073

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "844cb55c7859"
down_revision: Union[str, Sequence[str], None] = "802ef522353b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "posts_tags_association",
        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "post_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "tag_name",
            postgresql.CITEXT(length=32),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["posts.id"],
            name=op.f("fk_posts_tags_association_post_id_posts"),
        ),
        sa.ForeignKeyConstraint(
            ["tag_name"],
            ["tags.name"],
            name=op.f("fk_posts_tags_association_tag_name_tags"),
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_posts_tags_association"),
        ),
        sa.UniqueConstraint(
            "post_id",
            "tag_name",
            name=op.f("uq_posts_tags_association_post_id"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts_tags_association")
