"""add tax_number column to suppliers table

Revision ID: 388acc72664f
Revises: a2d75b582f29
Create Date: 2025-11-12 21:14:43.930927

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "388acc72664f"
down_revision: Union[str, Sequence[str], None] = "a2d75b582f29"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "suppliers",
        sa.Column(
            "tax_number",
            sa.Text(),
            nullable=True,
        ),
    )
    op.create_unique_constraint(
        op.f("uq_suppliers_tax_number"),
        "suppliers",
        ["tax_number"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        op.f("uq_suppliers_tax_number"),
        "suppliers",
        type_="unique",
    )
    op.drop_column(
        "suppliers",
        "tax_number",
    )
