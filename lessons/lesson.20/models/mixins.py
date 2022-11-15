from datetime import datetime
from sqlalchemy import (
    Column,
    DateTime,
    func,
)


class CreatedAtMixin:
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        server_default=func.now(),
        nullable=False,
    )
