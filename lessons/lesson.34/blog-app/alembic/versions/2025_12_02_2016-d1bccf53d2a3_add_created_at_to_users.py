"""add created_at to users

Revision ID: d1bccf53d2a3
Revises: ab24fea21154
Create Date: 2025-12-02 20:16:27.484938

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d1bccf53d2a3"
down_revision: Union[str, Sequence[str], None] = "ab24fea21154"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "user",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("user", "created_at")
