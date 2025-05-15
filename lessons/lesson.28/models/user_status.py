from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base
from models.mixins import CreatedAtMixin

# if TYPE_CHECKING:
#     from models import User


class UserStatus(CreatedAtMixin, Base):
    __tablename__ = "user_status"

    name: Mapped[str] = mapped_column(
        String(20),
        unique=True,
    )
    description: Mapped[str] = mapped_column(
        String(255),
        default="",
        server_default="",
    )
