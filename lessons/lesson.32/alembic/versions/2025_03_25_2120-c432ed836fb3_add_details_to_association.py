"""add details to association

Revision ID: c432ed836fb3
Revises: 5ea5c6984ddf
Create Date: 2025-03-25 21:20:55.662610

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c432ed836fb3"
down_revision: Union[str, None] = "5ea5c6984ddf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "article_source_association_table",
        sa.Column(
            "details",
            sa.String(length=200),
            server_default="",
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("article_source_association_table", "details")
