"""create books table

Revision ID: 410fe10ed73c
Revises:
Create Date: 2026-02-07 13:12:28.185291

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "410fe10ed73c"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "books",
        sa.Column(
            "id",
            sa.Uuid(),
            server_default=sa.text("uuidv7()"),
            nullable=False,
        ),
        sa.Column(
            "title",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.Column(
            "pub_date",
            sa.Date(),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_books"),
        ),
    )
    op.create_index(
        op.f("ix_books_title"),
        "books",
        ["title"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f("ix_books_title"), table_name="books")
    op.drop_table("books")
