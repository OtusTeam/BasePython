"""Add email col to owners table

Revision ID: 132879f495e8
Revises: ce51c4eae412
Create Date: 2024-08-22 20:45:49.618814

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "132879f495e8"
down_revision: Union[str, None] = "ce51c4eae412"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "owners",
        sa.Column("email", sa.String(), nullable=True),
    )
    op.create_unique_constraint(
        op.f("uq_owners_email"),
        "owners",
        ["email"],
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("uq_owners_email"),
        "owners",
        type_="unique",
    )
    op.drop_column("owners", "email")
