"""add created_at col to posts

Revision ID: d1ce0e288d93
Revises: b087149931a3
Create Date: 2025-11-18 21:18:36.390458

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d1ce0e288d93"
down_revision: Union[str, Sequence[str], None] = "b087149931a3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "post",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("post", "created_at")
