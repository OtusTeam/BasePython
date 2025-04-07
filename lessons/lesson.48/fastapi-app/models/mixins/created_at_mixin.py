from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import func

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        # default=func.now(),
        server_default=func.now(),
        nullable=False,
    )
