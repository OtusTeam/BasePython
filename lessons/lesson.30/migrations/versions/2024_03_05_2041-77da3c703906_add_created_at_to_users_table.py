"""add created_at to users table

Revision ID: 77da3c703906
Revises: 2710028cd64e
Create Date: 2024-03-05 20:41:51.302650

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "77da3c703906"
down_revision = "2710028cd64e"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "created_at",
                sa.DateTime(),
                server_default=sa.text("now()"),
                nullable=False,
            )
        )


def downgrade():
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.drop_column("created_at")
