"""create products table

Revision ID: daa0454765fc
Revises: 77da3c703906
Create Date: 2024-03-05 20:45:40.413616

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "daa0454765fc"
down_revision = "77da3c703906"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "product",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=32), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )


def downgrade():
    op.drop_table("product")
