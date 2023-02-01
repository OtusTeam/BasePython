"""merge author bio and rm created_at

Revision ID: dfe016ae0bdd
Revises: 37592d69b1f9, f883cbbe27ad
Create Date: 2023-02-01 20:58:08.873612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "dfe016ae0bdd"
down_revision = ("37592d69b1f9", "f883cbbe27ad")
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
