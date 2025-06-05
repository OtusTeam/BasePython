"""create table user_status

Revision ID: 8764cd527aee
Revises: 09ed8ada8abe
Create Date: 2025-05-15 20:57:30.412234

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8764cd527aee"
down_revision: Union[str, None] = "09ed8ada8abe"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "user_status",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=10), nullable=False),
        sa.Column(
            "description",
            sa.String(length=255),
            server_default="",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_user_status")),
        sa.UniqueConstraint("name", name=op.f("uq_user_status_name")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("user_status")
