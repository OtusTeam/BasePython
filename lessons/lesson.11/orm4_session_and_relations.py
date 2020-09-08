from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship

engine = create_engine("sqlite:///example2.db")
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


posts_tags_table = Table(
    "posts_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)

# class Profile(Base):
#     first


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    posts = relationship("Post", back_populates="author")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"

    def __repr__(self):
        return str(self)

    # def create_post(self):

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    # user_id = Column(Integer, ForeignKey("users.id"))
    author_id = Column(Integer, ForeignKey(User.id), nullable=False)

    author =  relationship(User, back_populates="posts")
    tags = relationship("Tag", secondary=posts_tags_table, back_populates="posts")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, author={self.author})"

    def __repr__(self):
        return str(self)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)

    posts = relationship("Post", secondary=posts_tags_table, back_populates="tags")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return str(self)


def create_user(username: str) -> User:
    """
    :param username:
    :return:
    """

    u = User(username=username)
    print("id before:", u.id)
    session.add(u)
    session.commit()
    print("id after:", u.id)
    return u


def author_posts():
    user = session.query(User).filter_by(username="sam").one()
    print(user)

    post = Post(title="First post!", author=user)
    session.add(post)
    session.commit()
    print(post)
    print(user.posts)

    post = Post(title="Second post!")

    # user_posts: List[Post] = user.posts
    user.posts.append(post)

    session.commit()
    print(user.posts)


def create_tags():
    user = session.query(User).filter_by(username="john").one()
    user.is_staff = True

    tags = [Tag(name=name) for name in ("news", "flask", "django", "python")]
    post = Post(title="News Flask vs Django", author=user)
    post.tags.extend(tags)

    session.commit()

    print(post, post.tags)

    for tag in tags:
        print(tag, tag.posts)


if __name__ == "__main__":
    Base.metadata.create_all()

    session = Session()

    # u = create_user("sam")
    # author_posts()
    # create_tags()

    users = session.query(User).filter(
        User.id > 1,
        User.username != "john",
    ).all()

    print(users)


    posts = session.query(Post).all()
    for post in posts:
        print(post, type(post.tags), post.tags)

    users_query = session.query(
        User,
    ).join(
        Post,
        User.id == Post.author_id,
    ).filter(
        Post.tags.any(
            # Tag.name.ilike("new%"),
            Tag.name != "django",
        )
    )

    print()
    print()
    print(repr(users_query))
    print(users_query)
    print()
    print(users_query.all())
    print()


    posts_query = session.query(
        Post,
    ).filter(
        Post.tags.any(
            # Tag.name.ilike("new%"),
            # Tag.name != "django",
            Tag.name == "flask",
        )
    )
    print()
    print()
    print(posts_query)
    print(list(posts_query))
    print([post for post in posts_query])
    print()
    print(posts_query.all())
    print()

    session.close()
