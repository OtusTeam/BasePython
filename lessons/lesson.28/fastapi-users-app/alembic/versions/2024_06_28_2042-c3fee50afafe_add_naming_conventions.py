"""add naming conventions

Revision ID: c3fee50afafe
Revises: f99585d52984
Create Date: 2024-06-28 20:42:04.295478

"""
from os import getenv
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c3fee50afafe"
down_revision: Union[str, None] = "f99585d52984"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


SURE_RECREATE_CONSTRAINTS = getenv("SURE_RECREATE_CONSTRAINTS_c3fee50afafe")


def upgrade() -> None:
    if SURE_RECREATE_CONSTRAINTS:
        op.drop_constraint("users_email_key", "users", type_="unique")
        op.drop_constraint("users_username_key", "users", type_="unique")
        op.create_unique_constraint(
            op.f("uq_users_email"), "users", ["email"]
        )
        op.create_unique_constraint(
            op.f("uq_users_username"), "users", ["username"]
        )


def downgrade() -> None:
    if SURE_RECREATE_CONSTRAINTS:
        op.drop_constraint(
            op.f("uq_users_username"), "users", type_="unique"
        )
        op.drop_constraint(
            op.f("uq_users_email"), "users", type_="unique"
        )
        op.create_unique_constraint(
            "users_username_key", "users", ["username"]
        )
        op.create_unique_constraint(
            "users_email_key", "users", ["email"]
        )
