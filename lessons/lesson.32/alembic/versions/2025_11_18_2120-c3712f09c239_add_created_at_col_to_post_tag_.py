"""add created_at col to post_tag association

Revision ID: c3712f09c239
Revises: d1ce0e288d93
Create Date: 2025-11-18 21:20:07.874875

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c3712f09c239"
down_revision: Union[str, Sequence[str], None] = "d1ce0e288d93"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "post_tag_association",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("post_tag_association", "created_at")
