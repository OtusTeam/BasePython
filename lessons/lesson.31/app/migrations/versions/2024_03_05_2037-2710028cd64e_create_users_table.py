"""create users table

Revision ID: 2710028cd64e
Revises: 
Create Date: 2024-03-05 20:37:46.490223

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2710028cd64e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=32), nullable=False),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("full_name", sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_user_full_name"),
            ["full_name"],
            unique=False,
        )


def downgrade():
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_user_full_name"))

    op.drop_table("user")
