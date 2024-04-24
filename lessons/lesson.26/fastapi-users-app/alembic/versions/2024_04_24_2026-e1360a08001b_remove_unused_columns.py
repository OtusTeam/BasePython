"""remove unused columns

Revision ID: e1360a08001b
Revises: 2cbda9aa24ac
Create Date: 2024-04-24 20:26:14.422546

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e1360a08001b"
down_revision: Union[str, None] = "2cbda9aa24ac"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint("unique_ix_friend_code", "users", type_="unique")
    op.drop_constraint("unique_ix_ref_code", "users", type_="unique")
    op.drop_column("users", "friend_code")
    op.drop_column("users", "ref_code")


def downgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "ref_code",
            sa.VARCHAR(length=10),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.add_column(
        "users",
        sa.Column(
            "friend_code",
            sa.VARCHAR(length=10),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.create_unique_constraint("unique_ix_ref_code", "users", ["ref_code"])
    op.create_unique_constraint(
        "unique_ix_friend_code", "users", ["friend_code"]
    )
