"""create tags table

Revision ID: 0de8895d4781
Revises: 1d0e0468114b
Create Date: 2024-07-02 20:15:14.262376

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0de8895d4781"
down_revision: Union[str, None] = "1d0e0468114b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tags",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=32), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_tags")),
        sa.UniqueConstraint("name", name=op.f("uq_tags_name")),
    )


def downgrade() -> None:
    op.drop_table("tags")
