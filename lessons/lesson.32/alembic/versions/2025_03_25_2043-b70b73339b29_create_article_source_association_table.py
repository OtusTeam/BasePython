"""create article_source_association_table

Revision ID: b70b73339b29
Revises: 9883b58f78e0
Create Date: 2025-03-25 20:43:26.638147

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b70b73339b29"
down_revision: Union[str, None] = "9883b58f78e0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "article_source_association_table",
        sa.Column(
            "article_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "source_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["article_id"],
            ["articles.id"],
            name=op.f("fk_article_source_association_table_article_id_articles"),
        ),
        sa.ForeignKeyConstraint(
            ["source_id"],
            ["sources.id"],
            name=op.f("fk_article_source_association_table_source_id_sources"),
        ),
        sa.PrimaryKeyConstraint(
            "article_id",
            "source_id",
            name=op.f("pk_article_source_association_table"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("article_source_association_table")
