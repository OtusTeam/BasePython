"""add bio to users

Revision ID: d7c62b9242fd
Revises: a3435736b6a7
Create Date: 2024-04-10 20:34:19.450540

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d7c62b9242fd"
down_revision: Union[str, None] = "a3435736b6a7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("bio", sa.String(length=200), nullable=True)
    )


def downgrade() -> None:
    op.drop_column("users", "bio")
