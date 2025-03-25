"""move pk on article_source_association_table

Revision ID: 32587c7f0249
Revises: b70b73339b29
Create Date: 2025-03-25 21:12:38.739708

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "32587c7f0249"
down_revision: Union[str, None] = "b70b73339b29"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "article_source_association_table",
        sa.Column(
            "id",
            sa.Integer(),
            sa.Identity(always=True),
            nullable=False,
        ),
    )
    op.create_unique_constraint(
        op.f("uq_article_source_association_table_article_id"),
        "article_source_association_table",
        ["article_id", "source_id"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        op.f("uq_article_source_association_table_article_id"),
        "article_source_association_table",
        type_="unique",
    )
    op.drop_column("article_source_association_table", "id")
