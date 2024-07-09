"""add full name to users table

Revision ID: f99585d52984
Revises: 515a0d758e1b
Create Date: 2024-06-28 20:33:32.509205

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f99585d52984"
down_revision: Union[str, None] = "515a0d758e1b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "full_name",
            sa.String(),
            server_default="",
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column("users", "full_name")
