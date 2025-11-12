"""create products table

Revision ID: 0ea8b3587b57
Revises: b618050179ef
Create Date: 2025-11-12 21:24:29.969503

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0ea8b3587b57"
down_revision: Union[str, Sequence[str], None] = "b618050179ef"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "products",
        sa.Column(
            "id",
            sa.BigInteger(),
            sa.Identity(always=True),
            nullable=False,
        ),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column(
            "description",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "kind_id",
            sa.BigInteger(),
            nullable=False,
        ),
        sa.Column(
            "supplier_id",
            sa.BigInteger(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["kind_id"],
            ["product_kinds.id"],
            name=op.f("fk_products_kind_id_product_kinds"),
        ),
        sa.ForeignKeyConstraint(
            ["supplier_id"],
            ["suppliers.id"],
            name=op.f("fk_products_supplier_id_suppliers"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_products")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("products")
