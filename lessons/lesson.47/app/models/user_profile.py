from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from models.base import Base
from models.mixins.created_at_mixin import CreatedAtMixin
from models.mixins.user_relation_mixin import UserRelationMixin


class UserProfile(CreatedAtMixin, UserRelationMixin, Base):
    __tablename__ = "user_profiles"
    _user_relation_unique = True

    delivery_address = Column(String)
    family_status = Column(String)

    user = relationship(
        "User",
        back_populates="profile",
        uselist=False,
    )
