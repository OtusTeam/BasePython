"""add joined_at col to authors table

Revision ID: eb4835baddf1
Revises: 8a43e923fd86
Create Date: 2024-11-01 21:11:53.485667

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "eb4835baddf1"
down_revision: Union[str, None] = "8a43e923fd86"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "author",
        sa.Column(
            "joined_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column("author", "joined_at")
