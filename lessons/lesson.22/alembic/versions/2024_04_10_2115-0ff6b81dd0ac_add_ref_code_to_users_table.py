"""add ref_code to users table

Revision ID: 0ff6b81dd0ac
Revises: c8f3228ed335
Create Date: 2024-04-10 21:15:07.020745

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0ff6b81dd0ac"
down_revision: Union[str, None] = "c8f3228ed335"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("ref_code", sa.String(length=10), nullable=True)
    )
    op.create_unique_constraint("unique_ix_ref_code", "users", ["ref_code"])


def downgrade() -> None:
    op.drop_constraint("unique_ix_ref_code", "users", type_="unique")
    op.drop_column("users", "ref_code")
