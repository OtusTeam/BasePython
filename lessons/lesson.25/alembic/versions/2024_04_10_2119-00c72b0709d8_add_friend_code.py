"""add friend_code

Revision ID: 00c72b0709d8
Revises: 0ff6b81dd0ac
Create Date: 2024-04-10 21:19:17.106831

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "00c72b0709d8"
down_revision: Union[str, None] = "0ff6b81dd0ac"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("friend_code", sa.String(length=10), nullable=True)
    )
    op.create_unique_constraint(
        "unique_ix_friend_code", "users", ["friend_code"]
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("unique_ix_friend_code", "users", type_="unique")
    op.drop_column("users", "friend_code")
    # ### end Alembic commands ###