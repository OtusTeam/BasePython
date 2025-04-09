"""create author table

Revision ID: 9fa798bcaa83
Revises: 
Create Date: 2025-01-20 20:48:11.640679

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9fa798bcaa83"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "author",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "name",
            sa.String(length=200),
            nullable=False,
        ),
        sa.Column(
            "bio",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_author")),
    )


def downgrade() -> None:
    op.drop_table("author")
