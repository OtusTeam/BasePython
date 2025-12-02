"""add id pk tp post_tag association table

Revision ID: ab24fea21154
Revises: c3712f09c239
Create Date: 2025-11-18 21:22:19.422560

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ab24fea21154"
down_revision: Union[str, Sequence[str], None] = "c3712f09c239"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "post_tag_association",
        sa.Column(
            "id",
            sa.BigInteger(),
            sa.Identity(always=True),
            nullable=False,
        ),
    )
    op.drop_constraint(
        constraint_name=op.f("pk_post_tag_association"),
        table_name="post_tag_association",
        type_="primary",
    )
    op.create_primary_key(
        constraint_name=op.f("pk_post_tag_association"),
        table_name="post_tag_association",
        columns=["id"],
    )
    op.create_unique_constraint(
        "post_tag_pair",
        "post_tag_association",
        ["post_id", "tag_id"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "post_tag_pair",
        "post_tag_association",
        type_="unique",
    )
    op.drop_column("post_tag_association", "id")
    op.create_primary_key(
        constraint_name=op.f("pk_post_tag_association"),
        table_name="post_tag_association",
        columns=["post_id", "tag_id"],
    )
