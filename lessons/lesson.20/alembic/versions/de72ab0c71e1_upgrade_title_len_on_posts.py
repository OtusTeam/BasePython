"""upgrade title len on posts

Revision ID: de72ab0c71e1
Revises: e4b99a20cc49
Create Date: 2023-08-08 20:51:02.856437

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "de72ab0c71e1"
down_revision: Union[str, None] = "e4b99a20cc49"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "posts",
        "title",
        existing_type=sa.VARCHAR(length=100),
        type_=sa.String(length=120),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "posts",
        "title",
        existing_type=sa.String(length=120),
        type_=sa.VARCHAR(length=100),
        existing_nullable=False,
    )
    # ### end Alembic commands ###