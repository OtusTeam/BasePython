"""add created_at and updated_at cols to posts

Revision ID: 9312801b94ad
Revises: 159cd6e87db4
Create Date: 2026-02-02 20:59:37.964332

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9312801b94ad"
down_revision: Union[str, Sequence[str], None] = "159cd6e87db4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    op.add_column(
        "posts",
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "updated_at")
    op.drop_column("posts", "created_at")
