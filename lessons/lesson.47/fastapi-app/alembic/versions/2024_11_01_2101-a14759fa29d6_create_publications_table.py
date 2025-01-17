"""Create publications table

Revision ID: a14759fa29d6
Revises: e5d0603a26e4
Create Date: 2024-11-01 21:01:33.898176

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a14759fa29d6"
down_revision: Union[str, None] = "e5d0603a26e4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "publication",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("body", sa.String(), server_default="", nullable=False),
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
