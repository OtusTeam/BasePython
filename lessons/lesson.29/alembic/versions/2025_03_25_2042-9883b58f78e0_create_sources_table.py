"""create sources table

Revision ID: 9883b58f78e0
Revises: f8a06c1f7697
Create Date: 2025-03-25 20:42:36.684173

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9883b58f78e0"
down_revision: Union[str, None] = "f8a06c1f7697"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "sources",
        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "name",
            sa.String(length=300),
            nullable=False,
        ),
        sa.Column(
            "url",
            sa.String(length=4000),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_sources"),
        ),
        sa.UniqueConstraint(
            "url",
            name=op.f("uq_sources_url"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("sources")
