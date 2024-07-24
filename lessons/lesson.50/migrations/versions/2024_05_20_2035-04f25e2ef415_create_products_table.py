"""create products table

Revision ID: 04f25e2ef415
Revises: 
Create Date: 2024-05-20 20:35:04.615872

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "04f25e2ef415"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "product",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )


def downgrade():
    op.drop_table("product")
