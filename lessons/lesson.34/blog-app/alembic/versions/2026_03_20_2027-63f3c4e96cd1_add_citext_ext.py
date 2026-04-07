"""add citext ext

Revision ID: 63f3c4e96cd1
Revises: b1893ec4e76c
Create Date: 2026-03-20 20:27:30.189290

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "63f3c4e96cd1"
down_revision: Union[str, Sequence[str], None] = "b1893ec4e76c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE EXTENSION IF NOT EXISTS citext;")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP EXTENSION IF EXISTS citext;")
