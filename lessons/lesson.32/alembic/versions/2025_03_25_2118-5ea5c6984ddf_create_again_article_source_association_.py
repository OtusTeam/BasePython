"""create again article_source_association_table

Revision ID: 5ea5c6984ddf
Revises: f8352f65acff
Create Date: 2025-03-25 21:18:19.345936

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5ea5c6984ddf"
down_revision: Union[str, None] = "f8352f65acff"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "article_source_association_table",
        sa.Column(
            "id",
            sa.Integer(),
            sa.Identity(always=True),
            nullable=False,
        ),
        sa.Column("article_id", sa.Integer(), nullable=False),
        sa.Column("source_id", sa.Integer(), nullable=False),
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
            "id",
            name=op.f("pk_article_source_association_table"),
        ),
        sa.UniqueConstraint(
            "article_id",
            "source_id",
            name=op.f("uq_article_source_association_table_article_id"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("article_source_association_table")
