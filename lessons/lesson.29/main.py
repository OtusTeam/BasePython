from itertools import cycle
from typing import Sequence

from sqlalchemy import select, func
from sqlalchemy.orm import Session, joinedload, selectinload

from models import Base, User, Post, Tag
from models.db import engine
import re
import unicodedata


def slugify(s, sep="-", max_len=None):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", sep, s).strip(sep)
    if max_len and len(s) > max_len:
        s = s[:max_len].rstrip(sep)
    return s


def create_users():
    user_john = User(
        username="john",
        email="john@example.com",
    )
    with Session(engine) as session:
        session.add(user_john)
        print("user before commit:", user_john)
        session.commit()
        print("user after commit:", user_john)

    users = [
        User(
            username="bob",
            email="bob@example.com",
            full_name="Bob White",
        ),
        User(
            username="alice",
        ),
    ]
    with Session(engine) as session, session.begin():
        session.add_all(users)


def create_users_and_posts(
    session: Session,
):
    user_john = User(
        username="john",
        email="john@example.com",
    )
    user_bob = User(
        username="bob",
        email="bob@example.com",
        full_name="Bob White",
    )
    user_alice = User(
        username="alice",
    )
    users = [
        user_john,
        user_bob,
        user_alice,
    ]
    session.add_all(users)
    # это не часто используется
    # тут мы получаем айдишники, но ещё не сохраняем всё
    session.flush()

    for count, user in enumerate(users):
        if not count:
            continue

        posts = [
            Post(
                title=f"post-{num:02d} by {user.username} ({user.id})",
                # user=user,
                user_id=user.id,
            )
            for num in range(1, count + 1)
        ]
        session.add_all(posts)

    session.commit()


def create_tags(session: Session, *tags_names: str) -> list[Tag]:
    tags = [Tag(name=name) for name in tags_names]
    session.add_all(tags)
    session.commit()
    return tags


def initial_creation():
    # print(Base.metadata.tables)
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    # insert_values()
    create_users()

    tags = [
        "SQLAlchemy",
        "tutorial",
        "Python",
        "async",
        "REST",
        "backend",
        "containers",
        "observability",
        "typing",
        "web",
        "API",
        "database",
        "best practices",
        "deep dive",
        "migrations",
        "metrics",
    ]

    with Session(engine) as session:
        # create_users_and_posts(session)
        create_tags(session, "PyCharm", "VS Code", "Django", "FastAPI")
        create_tags(session, *tags)


def show_posts_with_authors(session: Session):
    # statement = select(Post).order_by(Post.id)
    statement = (
        select(Post)
        .options(
            joinedload(Post.user),
        )
        .order_by(Post.id)
    )
    posts = session.scalars(statement).all()
    for post in posts:
        print("-", post, "by", post.user)


def show_users_with_posts(session: Session):
    statement = (
        select(User)
        # .where(func.length(User.username) > 3)
        .options(
            selectinload(User.posts),
        ).order_by(User.id)
    )
    users = session.scalars(statement).all()
    for user in users:
        print(user, "and posts:")
        if not user.posts:
            print("=== no posts yet === ")
            continue
        for post in user.posts:
            print("  •", post)


def create_posts_with_tags_for_users(
    session: Session,
    users: Sequence[User],
):
    users_cycle = cycle(users)

    titles = [
        "How to get started with SQLAlchemy. Tutorial 1",
        "Deep dive into Python typing",
        "Async patterns in web apps",
        "Designing RESTful APIs",
        "Designing Async RESTful APIs",
        "Optimizing database queries",
        "Testing strategies for backend services. Tutorial.",
        "Deploying with containers",
        "Deploying best practices",
        "Security best practices",
        "Working with migrations",
        "Observability and metrics",
        "Scaling background jobs",
        "Data modeling patterns",
    ]
    tags = session.scalars(select(Tag)).all()

    for title in titles:
        post = Post(
            title=title,
            slug=slugify(title),
            user=next(users_cycle),
        )
        session.add(post)

        title_lower = title.lower()
        for tag in tags:
            if tag.name.lower() in title_lower:
                post.tags.append(tag)

    session.commit()


def show_posts_with_tags(session: Session):
    posts = session.scalars(
        select(Post)
        .order_by(Post.id)
        .options(
            selectinload(Post.tags),
        )
    ).all()

    for post in posts:
        print("+", post)
        if not post.tags:
            print("  -- no tags yet")
            continue
        print("  tags:")
        for tag in post.tags:
            print("  •", tag.name)


def main():
    """"""
    print(Base.metadata.tables)
    initial_creation()
    with Session(engine) as session:

        users = session.scalars(select(User)).all()
        create_posts_with_tags_for_users(session, users)

        show_posts_with_authors(session)
        show_users_with_posts(session)
        show_posts_with_tags(session)


if __name__ == "__main__":
    main()
