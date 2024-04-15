"""create posts table

Revision ID: a3435736b6a7
Revises: 19d1c7dc0b4f
Create Date: 2024-04-10 20:30:06.396718

"""

from typing import (
    Sequence,
    Union,
)

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "a3435736b6a7"
down_revision: Union[str, None] = "19d1c7dc0b4f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "title",
            sa.String(length=100),
            server_default="",
            nullable=False,
        ),
        sa.Column(
            "published_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("posts")
