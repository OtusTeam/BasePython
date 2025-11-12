"""create product_kinds table

Revision ID: b618050179ef
Revises: 388acc72664f
Create Date: 2025-11-12 21:20:55.476301

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b618050179ef"
down_revision: Union[str, Sequence[str], None] = "388acc72664f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "product_kinds",
        sa.Column(
            "id",
            sa.BigInteger(),
            sa.Identity(always=True),
            nullable=False,
        ),
        sa.Column("name", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_product_kinds"),
        ),
        sa.UniqueConstraint(
            "name",
            name=op.f("uq_product_kinds_name"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("product_kinds")
