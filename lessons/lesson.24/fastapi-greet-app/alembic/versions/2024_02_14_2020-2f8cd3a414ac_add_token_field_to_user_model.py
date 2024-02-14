"""add token field to user model

Revision ID: 2f8cd3a414ac
Revises: 9734023a772a
Create Date: 2024-02-14 20:20:10.379052

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2f8cd3a414ac"
down_revision: Union[str, None] = "9734023a772a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "token",
            sa.String(length=36),
            nullable=True,
        ),
    )
    op.create_unique_constraint(
        "ix_unique_user_token",
        "users",
        ["token"],
    )


def downgrade() -> None:
    op.drop_constraint(
        "ix_unique_user_token",
        "users",
        type_="unique",
    )
    op.drop_column(
        "users",
        "token",
    )
