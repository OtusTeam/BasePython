"""
Add books table

Revision ID: 56ff499433b6
Revises: 2726350f8fbc
Create Date: 2026-08-11 21:26:27.262442
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "56ff499433b6"
down_revision: str | Sequence[str] | None = "2726350f8fbc"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "book",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.CheckConstraint(
            "length(title) <= 200", name=op.f("ck_book_ck_book_title_length")
        ),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["author.id"],
            name=op.f("fk_book_author_id_author"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_book")),
    )
    op.create_index(op.f("ix_book_author_id"), "book", ["author_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_book_author_id"), table_name="book")
    op.drop_table("book")
