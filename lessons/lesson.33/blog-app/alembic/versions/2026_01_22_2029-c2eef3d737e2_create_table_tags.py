"""create table tags

Revision ID: c2eef3d737e2
Revises: 23e5bfc42332
Create Date: 2026-01-22 20:29:37.349424

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c2eef3d737e2"
down_revision: Union[str, Sequence[str], None] = "23e5bfc42332"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "tags",
        sa.Column("name", sa.Text(), nullable=False),
        sa.CheckConstraint(
            "length(name) <= 100",
            name=op.f("ck_tags_name_length"),
        ),
        sa.PrimaryKeyConstraint("name", name=op.f("pk_tags")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("tags")
