"""Add visits table

Revision ID: f9ece6ae47a8
Revises: fa9f1d96a536
Create Date: 2024-08-22 21:16:09.523852

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f9ece6ae47a8"
down_revision: Union[str, None] = "fa9f1d96a536"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "visits",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("pet_id", sa.Integer(), nullable=False),
        sa.Column("reason", sa.String(), nullable=False),
        sa.Column("date", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["pet_id"],
            ["pets.id"],
            name=op.f("fk_visits_pet_id_pets"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_visits")),
    )


def downgrade() -> None:
    op.drop_table("visits")
