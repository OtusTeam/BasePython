"""create citext extension

Revision ID: 7b61752b734a
Revises: 03dff9349f46
Create Date: 2025-09-10 20:28:21.311804

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "7b61752b734a"
down_revision: Union[str, Sequence[str], None] = "03dff9349f46"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE EXTENSION IF NOT EXISTS citext;")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP EXTENSION IF EXISTS citext;")
