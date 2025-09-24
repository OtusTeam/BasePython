"""create tags table

Revision ID: 802ef522353b
Revises: 7b61752b734a
Create Date: 2025-09-10 20:30:09.571909

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "802ef522353b"
down_revision: Union[str, Sequence[str], None] = "7b61752b734a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "tags",
        sa.Column(
            "name",
            postgresql.CITEXT(length=32),
            nullable=False,
        ),
        sa.Column(
            "description",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("name", name=op.f("pk_tags")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("tags")
