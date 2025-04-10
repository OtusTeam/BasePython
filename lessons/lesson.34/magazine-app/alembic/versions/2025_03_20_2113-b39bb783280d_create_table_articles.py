"""create table articles

Revision ID: b39bb783280d
Revises: f4531d355c26
Create Date: 2025-03-20 21:13:17.684864

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b39bb783280d"
down_revision: Union[str, None] = "f4531d355c26"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "articles",
        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "title",
            sa.String(length=140),
            server_default="",
            nullable=False,
        ),
        sa.Column("published_at", sa.DateTime(), nullable=True),
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["users.id"],
            name=op.f("fk_articles_author_id_users"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_articles"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("articles")
