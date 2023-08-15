"""merge create posts tags association and add user bio

Revision ID: e4b99a20cc49
Revises: 18db0d1507e6, 9f9101820123
Create Date: 2023-08-08 20:47:02.320990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e4b99a20cc49"
down_revision: Union[str, None, tuple[str, ...]] = ("18db0d1507e6", "9f9101820123")
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
