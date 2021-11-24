from datetime import datetime

from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship, scoped_session, sessionmaker, joinedload
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///example-04.db", echo=True)
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


# class PostsTags(Base):


posts_tags_table = Table(
    "posts_tags_association_table",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    posts = relationship("Post", back_populates="author")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, " \
               f"username={self.username!r}, " \
               f"is_staff={self.is_staff}, " \
               f"created_at={self.created_at!r})"

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False, default="", server_default="")
    # body = Column(Text)
    # author_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey(User.id), nullable=False)

    author = relationship(User, back_populates="posts")
    tags = relationship(
        "Tag",
        secondary=posts_tags_table,
        back_populates="posts",
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, " \
               f"title={self.title!r}, " \
               f"author_id={self.author_id}, " \
               f"created_at={self.created_at!r})"

    def __repr__(self):
        return str(self)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=True)

    posts = relationship(
        "Post",
        secondary=posts_tags_table,
        back_populates="tags",
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


def create_user(username: str) -> User:
    """
    :param username: str
    :return: User
    """
    session = Session()
    user = User(username=username)
    print("creating user", user)
    session.add(user)
    session.commit()
    print("created user", user)

    session.close()
    return user


def get_user(username: str) -> User:
    """
    :param username:
    :return:
    """
    session = Session()
    user = session.query(User).filter_by(username=username).one()
    # user = session.query(User).filter_by(username=username).one_or_none()
    # user = session.query(User).filter_by(created_at="qwe").first()
    session.close()
    return user


def create_post(author: User, title: str) -> Post:
    """
    :param author:
    :param title:
    :return:
    """
    session = Session()

    post = Post(
        title=title,
        # author_id=author.id,
        author=author,
    )
    print("prepare post", post)
    session.add(post)
    session.commit()
    print("create post", post)

    session.close()
    return post


def get_posts_by_author() -> list[Post]:
    session = Session()

    posts = (
        session
        .query(Post)
        .join(User)
        .filter(
            User.username == "john",
            Post.title.ilike("%lesson%"),
        )
        .options(joinedload(Post.author).joinedload(User.posts))
        .all()
    )
    print("posts", posts)

    for post in posts:
        print("post", post)
        author: User = post.author
        print("post author", author)
        print("author posts", author.posts)

    session.close()

    return posts


def create_tags():
    session = Session()

    tag1 = Tag(name="news")
    tag2 = Tag(name="python")
    tag3 = Tag(name="flask")
    tag4 = Tag(name="django")
    session.add_all([
        tag1,
        tag2,
        tag3,
        tag4,
    ])
    session.commit()

    session.close()


def add_tags_to_posts():
    session = Session()

    q_tag = session.query(Tag)
    tag_news: Tag = q_tag.filter_by(name="news").one()
    tag_python: Tag = q_tag.filter_by(name="python").one()
    tag_flask: Tag = q_tag.filter_by(name="flask").one()
    tag_django: Tag = q_tag.filter_by(name="django").one()

    posts: list[Post] = session.query(Post).all()

    for post in posts:
        tag_news.posts.append(post)
        tag_python.posts.append(post)
        if "flask" in post.title.lower():
            post.tags.append(tag_flask)
        if "django" in post.title.lower():
            post.tags.append(tag_django)

    session.commit()

    session.close()


def fetch_posts_and_users_by_tags():
    session = Session()

    users: list[User] = (
        session
        .query(User)
        .join(Post)
        .join(Tag, Post.tags)
        .filter(Tag.name == "flask")
        .options(joinedload(User.posts).joinedload(Post.tags))
        .all()
    )
    print("users writing about flask:", users)
    for user in users:
        print("user", user)
        posts: list[Post] = user.posts
        for post in posts:
            print("-- post", post)
            print("--- with tags", post.tags)

    session.close()


def main():
    Base.metadata.create_all()
    create_user("john")
    create_user("sam")

    user_john = get_user("john")
    user_sam = get_user("sam")
    print(user_john)
    print(user_sam)

    create_post(user_john, "Flask lesson")
    create_post(user_sam, "Django lesson")
    create_post(user_john, "Flask demo")

    get_posts_by_author()
    create_tags()
    add_tags_to_posts()
    fetch_posts_and_users_by_tags()


if __name__ == '__main__':
    main()
