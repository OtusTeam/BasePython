"""create publication table

Revision ID: 53356bff487f
Revises: 9fa798bcaa83
Create Date: 2025-01-20 20:51:11.281855

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "53356bff487f"
down_revision: Union[str, None] = "9fa798bcaa83"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "publication",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column(
            "body", sa.Text(), server_default="", nullable=False
        ),
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["author.id"],
            name=op.f("fk_publication_author_id_author"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_publication")),
    )


def downgrade() -> None:
    op.drop_table("publication")
