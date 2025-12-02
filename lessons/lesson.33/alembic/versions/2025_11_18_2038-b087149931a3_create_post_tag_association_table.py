"""create post_tag association table

Revision ID: b087149931a3
Revises: 583f03221c4d
Create Date: 2025-11-18 20:38:49.749458

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b087149931a3"
down_revision: Union[str, Sequence[str], None] = "583f03221c4d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "post_tag_association",
        sa.Column(
            "post_id",
            sa.BigInteger(),
            nullable=False,
        ),
        sa.Column(
            "tag_id",
            sa.BigInteger(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["post.id"],
            name=op.f("fk_post_tag_association_post_id_post"),
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tag.id"],
            name=op.f("fk_post_tag_association_tag_id_tag"),
        ),
        sa.PrimaryKeyConstraint(
            "post_id",
            "tag_id",
            name=op.f("pk_post_tag_association"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("post_tag_association")
