"""Add username col to owners table

Revision ID: 1b73fc0146b7
Revises: 132879f495e8
Create Date: 2024-08-22 20:50:56.790422

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1b73fc0146b7"
down_revision: Union[str, None] = "132879f495e8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "owners",
        sa.Column("username", sa.String(), nullable=True),
    )
    op.create_unique_constraint(
        op.f("uq_owners_username"),
        "owners",
        ["username"],
    )


def downgrade() -> None:

    op.drop_constraint(
        op.f("uq_owners_username"),
        "owners",
        type_="unique",
    )
    op.drop_column("owners", "username")
