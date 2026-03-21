"""create table post

Revision ID: 97df48964125
Revises: 14184ba4a9dc
Create Date: 2026-03-17 21:38:13.058110

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "97df48964125"
down_revision: Union[str, Sequence[str], None] = "14184ba4a9dc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "post",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.Text(), server_default="", nullable=False),
        sa.Column("content", sa.Text(), server_default="", nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.CheckConstraint(
            "length(title) <= 100",
            name=op.f("ck_post_title_max_length"),
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name=op.f("fk_post_user_id_user"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_post")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("post")
