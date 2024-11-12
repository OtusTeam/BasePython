"""add email col to authors table

Revision ID: 8a43e923fd86
Revises: a14759fa29d6
Create Date: 2024-11-01 21:03:09.487594

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8a43e923fd86"
down_revision: Union[str, None] = "a14759fa29d6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "author", sa.Column("email", sa.String(), nullable=True)
    )
    op.create_unique_constraint(
        op.f("uq_author_email"), "author", ["email"]
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("uq_author_email"), "author", type_="unique"
    )
    op.drop_column("author", "email")
