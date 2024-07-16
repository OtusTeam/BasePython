"""add ref code to users table

Revision ID: 0bee249a8c0e
Revises: c3fee50afafe
Create Date: 2024-06-28 20:43:29.619302

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0bee249a8c0e"
down_revision: Union[str, None] = "c3fee50afafe"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users", sa.Column("ref_code", sa.String(), nullable=True)
    )
    op.create_unique_constraint(
        op.f("uq_users_ref_code"), "users", ["ref_code"]
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("uq_users_ref_code"), "users", type_="unique"
    )
    op.drop_column("users", "ref_code")
