"""add created_at col to publication table

Revision ID: faa4416c842b
Revises: 9b2929a6afb3
Create Date: 2025-01-20 20:56:32.892292

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "faa4416c842b"
down_revision: Union[str, None] = "9b2929a6afb3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "publication",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column("publication", "created_at")
