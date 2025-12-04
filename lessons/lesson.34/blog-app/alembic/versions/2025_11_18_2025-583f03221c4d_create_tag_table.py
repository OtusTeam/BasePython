"""create tag table

Revision ID: 583f03221c4d
Revises: 4f33531e2e61
Create Date: 2025-11-18 20:25:45.294852

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "583f03221c4d"
down_revision: Union[str, Sequence[str], None] = "4f33531e2e61"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "tag",
        sa.Column(
            "id",
            sa.BigInteger(),
            sa.Identity(always=True),
            nullable=False,
        ),
        sa.Column("name", sa.Text(), nullable=False),
        sa.CheckConstraint(
            "char_length(name) >= 1 AND char_length(name) <= 32",
            name=op.f("ck_tag_name_length"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_tag")),
        sa.UniqueConstraint(
            "name",
            name=op.f("uq_tag_name"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("tag")
