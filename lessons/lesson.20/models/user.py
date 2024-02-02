from sqlalchemy import Column
from sqlalchemy import String

from sqlalchemy.orm import relationship

from models.base import Base


class User(Base):
    # id = Column(
    #     UUID(as_uuid=True),
    #     primary_key=True,
    #     default=uuid.uuid4,
    # )
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)
    full_name = Column(String(50), nullable=True, index=True)

    posts = relationship(
        # accessed through `Post.author`
        "Post",
        back_populates="author",
        uselist=True,
        # cascade="all, delete-orphan",
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            "User("
            f"id={self.id}"
            f", username={self.username!r}"
            # f", email={self.email!r}"
            ")"
        )
