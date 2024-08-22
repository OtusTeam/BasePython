"""Add pets table

Revision ID: fa9f1d96a536
Revises: 73b181dd7485
Create Date: 2024-08-22 21:13:55.160109

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fa9f1d96a536"
down_revision: Union[str, None] = "73b181dd7485"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "pets",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("species", sa.String(), nullable=False),
        sa.Column("owner_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["owners.id"],
            name=op.f("fk_pets_owner_id_owners"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_pets")),
    )


def downgrade() -> None:
    op.drop_table("pets")
