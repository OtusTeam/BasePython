"""create tags table

Revision ID: 9c8f84f7afe1
Revises: bf721fe535f4
Create Date: 2025-05-19 20:21:02.070317

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "9c8f84f7afe1"
down_revision: Union[str, None] = "bf721fe535f4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE EXTENSION IF NOT EXISTS citext;")

    op.create_table(
        "tags",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "name",
            postgresql.CITEXT(length=20),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_tags")),
        sa.UniqueConstraint("name", name=op.f("uq_tags_name")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("tags")

    op.execute("DROP EXTENSION IF EXISTS citext;")
