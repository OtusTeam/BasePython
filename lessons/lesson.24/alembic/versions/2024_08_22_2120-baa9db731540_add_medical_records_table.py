"""Add medical records table

Revision ID: baa9db731540
Revises: f9ece6ae47a8
Create Date: 2024-08-22 21:20:02.061865

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "baa9db731540"
down_revision: Union[str, None] = "f9ece6ae47a8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "medical_records",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("pet_id", sa.Integer(), nullable=False),
        sa.Column("notes", sa.Text(), nullable=False),
        sa.Column("last_visit", sa.Date(), nullable=False),
        sa.ForeignKeyConstraint(
            ["pet_id"],
            ["pets.id"],
            name=op.f("fk_medical_records_pet_id_pets"),
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_medical_records"),
        ),
    )


def downgrade() -> None:
    op.drop_table("medical_records")
