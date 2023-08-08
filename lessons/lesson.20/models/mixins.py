from datetime import datetime

from sqlalchemy import Column, DateTime, func, ForeignKey
from sqlalchemy.orm import declared_attr, relationship


class CreatedAtMixin:
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )


class RelatedToUserMixin:
    _user_back_populates = ""

    @declared_attr
    def user_id(cls):
        return Column(ForeignKey("users.id"))

    @declared_attr
    def user(cls):
        return relationship(
            "User",
            back_populates=cls._user_back_populates,
        )
