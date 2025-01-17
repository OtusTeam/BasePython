"""Create authors table

Revision ID: e5d0603a26e4
Revises: 
Create Date: 2024-11-01 20:57:34.503805

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e5d0603a26e4"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "author",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_author")),
        sa.UniqueConstraint("username", name=op.f("uq_author_username")),
    )


def downgrade() -> None:
    op.drop_table("author")
