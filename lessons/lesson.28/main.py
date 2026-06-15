from collections.abc import Sequence

from sqlalchemy import select, func
from sqlalchemy.orm import Session, selectinload, joinedload

from models import Base, engine, User, Post, session_factory


def insert_users(
    session: Session,
):
    john = User(
        username="john",
        email="john@example.com",
    )
    john.hello()
    print(john)

    session.add(john)
    session.commit()
    print("committed")
    print("new john:", john)

    bob = User(
        username="bob",
        email="bob@example.com",
        full_name="Bob Black",
    )
    alice = User(
        username="alice",
        full_name="Alice",
    )
    new_users = [bob, alice]
    session.add_all(new_users)
    session.commit()
    print("committed")
    print("new users:", new_users)


def get_user(
    session: Session,
    username: str,
) -> User:
    stmt = select(User).where(User.username == username)
    result = session.execute(stmt)
    return result.scalar_one()


def insert_posts(
    session: Session,
    user: User,
    *posts_titles: str,
):
    posts = [
        Post(
            title=title,
            user=user,
        )
        for title in posts_titles
    ]
    session.add_all(posts)
    session.commit()


def create_posts(session: Session):
    insert_posts(
        session,
        get_user(session, "bob"),
        "Hello World (by Bob)",
    )
    insert_posts(
        session,
        get_user(session, "alice"),
        "Python lessons",
        "SQlite lessons",
    )


def fetch_users(session: Session) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    return session.scalars(stmt).all()


def fetch_users_with_posts(session: Session) -> Sequence[User]:
    stmt = (
        select(User)
        # .where(User.email.isnot(None))
        # .where(func.length(User.username) > 3)
        .options(
            selectinload(User.posts),
        ).order_by(User.id)
    )
    return session.scalars(stmt).all()


def show_users(session: Session):
    # users = fetch_users(session)
    users = fetch_users_with_posts(session)
    for user in users:
        print("-", user)
        for post in user.posts:
            print(" ·", post)


def fetch_posts(session: Session) -> Sequence[Post]:
    stmt = select(Post).order_by(Post.id)
    return session.scalars(stmt).all()


def fetch_posts_with_user(session: Session) -> Sequence[Post]:
    stmt = (
        select(Post)
        .options(
            joinedload(Post.user),
        )
        .order_by(Post.id)
    )
    return session.scalars(stmt).all()


def show_posts(session: Session):
    # posts = fetch_posts(session)
    posts = fetch_posts_with_user(session)
    for post in posts:
        print("-", post)
        print("   by", post.user)


def main():
    # print("Tables:", Base.metadata.tables)

    with session_factory() as session:
        insert_users(session)
        create_posts(session)
        show_users(session)
        show_posts(session)


if __name__ == "__main__":
    main()
