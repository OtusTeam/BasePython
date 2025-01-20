"""add email col to author table

Revision ID: 9b2929a6afb3
Revises: 53356bff487f
Create Date: 2025-01-20 20:55:19.516844

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9b2929a6afb3"
down_revision: Union[str, None] = "53356bff487f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "author",
        sa.Column("email", sa.String(length=250), nullable=True),
    )

    # op.execute("SELECT COUNT(*) FROM author")

    op.create_unique_constraint(
        op.f("uq_author_email"), "author", ["email"]
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("uq_author_email"), "author", type_="unique"
    )
    op.drop_column("author", "email")

