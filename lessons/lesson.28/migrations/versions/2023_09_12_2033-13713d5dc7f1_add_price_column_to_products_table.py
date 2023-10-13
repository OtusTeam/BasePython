"""add price column to Products table

Revision ID: 13713d5dc7f1
Revises: c5ac56e77de7
Create Date: 2023-09-12 20:33:11.351747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "13713d5dc7f1"
down_revision = "c5ac56e77de7"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("product", schema=None) as batch_op:
        batch_op.add_column(sa.Column("price", sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("product", schema=None) as batch_op:
        batch_op.drop_column("price")

    # ### end Alembic commands ###