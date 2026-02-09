"""create post_tag_association table

Revision ID: 1f83be10e1c9
Revises: c2eef3d737e2
Create Date: 2026-01-22 20:38:37.376406

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1f83be10e1c9"
down_revision: Union[str, Sequence[str], None] = "c2eef3d737e2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "post_tag_association",
        sa.Column("post_id", sa.Integer(), nullable=False),
        sa.Column("tag_name", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["posts.id"],
            name=op.f("fk_post_tag_association_post_id_posts"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["tag_name"],
            ["tags.name"],
            name=op.f("fk_post_tag_association_tag_name_tags"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint(
            "post_id",
            "tag_name",
            name=op.f("pk_post_tag_association"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("post_tag_association")
