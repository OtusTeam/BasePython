"""drop article_source_association_table

Revision ID: f8352f65acff
Revises: 32587c7f0249
Create Date: 2025-03-25 21:17:44.235136

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f8352f65acff"
down_revision: Union[str, None] = "32587c7f0249"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_table("article_source_association_table")


def downgrade() -> None:
    """Downgrade schema."""
    op.create_table(
        "article_source_association_table",
        sa.Column(
            "article_id",
            sa.INTEGER(),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "source_id",
            sa.INTEGER(),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "id",
            sa.INTEGER(),
            sa.Identity(
                always=True,
                start=1,
                increment=1,
                minvalue=1,
                maxvalue=2147483647,
                cycle=False,
                cache=1,
            ),
            autoincrement=True,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["article_id"],
            ["articles.id"],
            name="fk_article_source_association_table_article_id_articles",
        ),
        sa.ForeignKeyConstraint(
            ["source_id"],
            ["sources.id"],
            name="fk_article_source_association_table_source_id_sources",
        ),
        sa.PrimaryKeyConstraint(
            "article_id",
            "source_id",
            name="pk_article_source_association_table",
        ),
        sa.UniqueConstraint(
            "article_id",
            "source_id",
            name="uq_article_source_association_table_article_id",
        ),
    )
