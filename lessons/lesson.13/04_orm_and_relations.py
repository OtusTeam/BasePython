from typing import List
from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    create_engine,
    func,
    ForeignKey,
    or_,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, joinedload

engine = create_engine("sqlite:///example-04.db", echo=True)
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User(Base):
    __tablename__ = "users"

    # def __init__(self, username, is_staff):
    #     self.username = username
    #     self.is_staff = is_staff

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, nullable=False, default=False, server_default="0")
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, server_default=func.now())

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        # attrs = []
        # for attr_name, attr_value in self.__dict__.items():
        #     if not attr_name.startswith("_"):
        #         attrs.append(f"{attr_name}={attr_value!r}")
        # return f"{self.__class__.__name__}({', '.join(attrs)})"
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, is_staff={self.is_staff}, created_at={self.created_at!r})"

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False, default="", server_default="")

    # user_id = Column(Integer, ForeignKey("users.id"))
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)

    user = relationship(User, back_populates="posts")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, user={self.user})"

    def __repr__(self):
        return str(self)


def create_users():
    session = Session()

    username = "admin"
    admin = User(username=username, is_staff=True)
    print(admin)

    guest = User(username="guest")
    print(guest)

    session.add(admin)
    session.add(guest)
    session.commit()

    print(admin)
    print(guest)

    session.close()


def create_posts():
    session = Session()

    admin: User = session.query(User).filter_by(username="admin").one()
    print("admin:", admin)
    print("admin posts before:", admin.posts)

    post_flask = Post(title="Flask lesson", user=admin)
    post_django = Post(title="Django lesson", user_id=admin.id)

    session.add(post_flask)
    session.add(post_django)
    session.commit()

    print("post flask", post_flask)
    print("post django", post_django)

    print("admin posts after:", admin.posts)

    session.close()


def demo_joined_load():
    session = Session()

    admin: User = (
        session
        .query(User)
        .filter_by(username="admin")
        .options(joinedload(User.posts))
        .one()
    )

    print("admin", admin)
    print("admin's posts:", admin.posts)

    session.close()


def demo_filtering():
    session = Session()

    users: List[User] = (
        session
        .query(User)
        .join(Post)
        # .options(joinedload(User.posts))
        .filter(
            or_(
                Post.title.ilike("%django%"),
                Post.title.ilike("%flask%"),
            )
        )
        .all()
    )
    print("users:", users)
    session.close()


def main():
    Base.metadata.create_all()
    # create_users()
    # create_posts()
    # demo_joined_load()
    demo_filtering()


if __name__ == '__main__':
    main()
