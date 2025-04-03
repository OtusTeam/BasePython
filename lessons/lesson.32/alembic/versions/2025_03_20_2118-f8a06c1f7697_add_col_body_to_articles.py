"""add col body to articles

Revision ID: f8a06c1f7697
Revises: e770c0edaaa8
Create Date: 2025-03-20 21:18:15.430077

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f8a06c1f7697"
down_revision: Union[str, None] = "e770c0edaaa8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "articles",
        sa.Column(
            "body",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("articles", "body")
