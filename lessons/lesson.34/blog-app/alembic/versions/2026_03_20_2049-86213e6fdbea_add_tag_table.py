"""add tag table

Revision ID: 86213e6fdbea
Revises: 63f3c4e96cd1
Create Date: 2026-03-20 20:49:01.816677

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "86213e6fdbea"
down_revision: Union[str, Sequence[str], None] = "63f3c4e96cd1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "tag",
        sa.Column(
            "name",
            postgresql.CITEXT(),
            nullable=False,
        ),
        sa.Column(
            "description",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.CheckConstraint("length(name) <= 16", name=op.f("ck_tag_name_length")),
        sa.PrimaryKeyConstraint("name", name=op.f("pk_tag")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("tag")
