from sqlalchemy import (
    Column,
    String,
    Boolean,
    # Integer,
)
from sqlalchemy.orm import relationship
# from sqlalchemy.dialects.postgresql import ARRAY

from .base import Base
from .mixins import TimestampMixin


class User(TimestampMixin, Base):

    def __init__(self, username: str, is_staff: bool = False):
        self.username = username
        self.is_staff = is_staff

    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False)
    # type = Column(String(20), unique=False, nullable=True)
    # # type = "manager"
    # management_users = Column(ARRAY(Integer))

    posts = relationship("Post", back_populates="author")


# BAD!!
# m = User()
# m.type = "manager"
#
# m.management_users.append(u1.id)
# m.management_users.append(u2.id)

