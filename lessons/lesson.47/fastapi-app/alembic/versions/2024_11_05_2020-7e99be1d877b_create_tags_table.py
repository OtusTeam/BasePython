"""create tags table

Revision ID: 7e99be1d877b
Revises: d11bee117a5d
Create Date: 2024-11-05 20:20:33.150494

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7e99be1d877b"
down_revision: Union[str, None] = "d11bee117a5d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tag",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_tag")),
    )


def downgrade() -> None:
    op.drop_table("tag")
