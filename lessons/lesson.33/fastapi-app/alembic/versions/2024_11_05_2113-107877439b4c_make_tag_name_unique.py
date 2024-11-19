"""make tag name unique

Revision ID: 107877439b4c
Revises: c0a4a16ed94d
Create Date: 2024-11-05 21:13:53.343859

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "107877439b4c"
down_revision: Union[str, None] = "c0a4a16ed94d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint(
        op.f("uq_tag_name"),
        "tag",
        ["name"],
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("uq_tag_name"),
        "tag",
        type_="unique",
    )
