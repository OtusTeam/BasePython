"""create table post

Revision ID: c0f46d3bfc1f
Revises: c7d041ecfcfd
Create Date: 2025-11-13 20:45:26.456420

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c0f46d3bfc1f"
down_revision: Union[str, Sequence[str], None] = "c7d041ecfcfd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "post",
        sa.Column(
            "id",
            sa.BigInteger(),
            sa.Identity(always=True),
            nullable=False,
        ),
        sa.Column(
            "title",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.Column(
            "body",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.Column(
            "user_id",
            sa.BigInteger(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name=op.f("fk_post_user_id_user"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_post")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("post")
