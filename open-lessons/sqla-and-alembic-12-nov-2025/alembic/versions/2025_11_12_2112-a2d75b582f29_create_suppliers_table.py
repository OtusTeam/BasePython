"""create suppliers table

Revision ID: a2d75b582f29
Revises:
Create Date: 2025-11-12 21:12:40.179393

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a2d75b582f29"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "suppliers",
        sa.Column(
            "id",
            sa.BigInteger(),
            sa.Identity(always=True),
            nullable=False,
        ),
        sa.Column("name", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_suppliers"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("suppliers")
