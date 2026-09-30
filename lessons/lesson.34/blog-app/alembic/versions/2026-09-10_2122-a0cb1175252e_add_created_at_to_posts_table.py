"""Add created_at to posts table

Revision ID: a0cb1175252e
Revises: a272a8447677
Create Date: 2026-09-10 21:22:27.095500

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "a0cb1175252e"
down_revision: Union[str, Sequence[str], None] = "a272a8447677"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column("posts", "created_at")
