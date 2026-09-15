"""add created_at to posts-tags assoc table

Revision ID: eacc080b0b21
Revises: a69d65327702
Create Date: 2026-09-15 20:59:02.065799

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "eacc080b0b21"
down_revision: Union[str, Sequence[str], None] = "a69d65327702"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts_tags_association_table",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column("posts_tags_association_table", "created_at")
