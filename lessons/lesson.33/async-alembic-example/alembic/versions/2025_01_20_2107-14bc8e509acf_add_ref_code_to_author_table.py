"""add ref_code to author table

Revision ID: 14bc8e509acf
Revises: faa4416c842b
Create Date: 2025-01-20 21:07:57.228470

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "14bc8e509acf"
down_revision: Union[str, None] = "faa4416c842b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "author", sa.Column("ref_code", sa.String(), nullable=True)
    )
    op.create_unique_constraint(
        op.f("uq_author_ref_code"), "author", ["ref_code"]
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("uq_author_ref_code"), "author", type_="unique"
    )
    op.drop_column("author", "ref_code")
