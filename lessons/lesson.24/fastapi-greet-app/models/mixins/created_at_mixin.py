from datetime import datetime

from sqlalchemy import Column, DateTime, func

# from sqlalchemy.orm import declared_attr


class CreatedAtMixin:
    """
    @declared_attr
    def created_at(cls):
        return Column(
            DateTime,
            nullable=False,
            default=datetime.utcnow,
            server_default=func.now(),
        )
    """

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )
