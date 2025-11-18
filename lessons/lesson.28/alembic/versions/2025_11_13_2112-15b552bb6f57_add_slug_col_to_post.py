"""add slug col to post

Revision ID: 15b552bb6f57
Revises: 76b622877569
Create Date: 2025-11-13 21:12:53.442502

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "15b552bb6f57"
down_revision: Union[str, Sequence[str], None] = "76b622877569"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "post",
        sa.Column(
            "slug",
            sa.Text,
            nullable=True,
        ),
    )
    op.create_unique_constraint(
        op.f("uq_post_slug"),
        "post",
        ["slug"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        op.f("uq_post_slug"),
        "post",
        type_="unique",
    )
    op.drop_column("post", "slug")
