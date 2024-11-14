"""create products table

Revision ID: 71d0d1f82f71
Revises: 
Create Date: 2024-09-23 20:34:14.145502

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "71d0d1f82f71"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "products",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )


def downgrade():
    op.drop_table("products")
