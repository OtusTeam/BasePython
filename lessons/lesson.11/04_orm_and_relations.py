from datetime import datetime
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, joinedload

engine = create_engine("sqlite:///example-orm.db", echo=True)
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, nullable=False, default=False, server_default="0")
    created_at = Column(DateTime, default=datetime.utcnow)

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, is_staff={self.is_staff})"

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, default="", server_default="")

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


def update_user():
    session = Session()

    # user = session.query(User).filter_by(id=2)
    guest: User = session.query(User).filter_by(username="guest").one()
    print(guest)

    guest.created_at = datetime.now()
    session.commit()

    session.close()


def create_posts():
    session = Session()

    guest: User = session.query(User).filter_by(username="guest").one()
    print("guest posts before:", guest.posts)

    post1 = Post(title="Flask lesson", user_id=guest.id)
    post2 = Post(title="Django lesson", user=guest)

    session.add(post1)
    session.add(post2)
    session.commit()

    print(post1)
    print(post2)
    print("guest posts after:", guest.posts)

    session.close()


def demo_joined_load():
    session = Session()

    # guest: User = session.query(User).filter_by(username="guest").one()
    # print("guest posts:", guest.posts)

    guest: User = (
        session
            .query(User)
            .filter_by(username="guest")
            .options(joinedload(User.posts))
            .one()
    )
    print("guest posts:", guest.posts)

    session.close()


def demo_use_join():
    session = Session()

    results = (
        session
            .query(User, Post)
            .filter_by(username="guest")
            .join(Post)
            # .outerjoin(Post, User.id == Post.user_id)
            # .one()
            .all()
    )
    # print("results:", results)
    print("results")
    for res in results:
        print(res)

    session.close()


def demo_query_by_join():
    session = Session()

    user: User = (
        session
            .query(User)
            .join(Post)
            .filter(
                Post.title.ilike("%flask%")
            )
            .first()
    )
    print("user with flask post:", user)


    result: User = (
        session
            .query(User, Post)
            .join(Post)
            .filter(
                Post.title.ilike("%flask%"),
                # Post.id <= 10,
                # Post.user_id.isnot(None),
            )
            .first()
    )
    print("user with flask post:", result)

    session.close()


if __name__ == "__main__":
    # print("create tables")
    # Base.metadata.create_all()
    # create_users()
    # update_user()
    # print("create posts")
    # create_posts()
    # demo_joined_load()
    # demo_use_join()
    demo_query_by_join()
