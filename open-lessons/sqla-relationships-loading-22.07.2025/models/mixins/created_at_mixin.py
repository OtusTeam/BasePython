from datetime import datetime, UTC

from sqlalchemy import func
from sqlalchemy.orm import mapped_column, Mapped


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(tz=UTC).replace(tzinfo=None),
        server_default=func.now(),
    )
