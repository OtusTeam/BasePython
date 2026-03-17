from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload, selectinload, subqueryload

from models import Base, engine, User, session_factory, Post


def insert_users() -> None:
    user_john = User(
        username="john",
        email="john@example.com",
        full_name="Johnathan",
    )

    with session_factory() as session:
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
    with session_factory() as session, session.begin():
        session.add_all(users)


def insert_posts(
    session: Session,
    user: User,
    posts_titles: list[str],
) -> None:
    posts = [
        Post(
            title=title,
            content=f"content for user {user.id} - title {title}",
            # user_id=user.id,
            user=user,
        )
        for title in posts_titles
    ]
    session.add_all(posts)
    session.commit()
    print(posts)


def fetch_users(
    session: Session,
) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    users = session.scalars(stmt)
    return users.all()


def create_posts_for_all_users(session: Session) -> None:
    users = fetch_users(session)
    for idx, user in enumerate(users, start=1):
        insert_posts(
            session,
            user,
            [
                # просто какой-то заголовок
                f"title-user-{user.username}-{i}"
                for i in range(1, idx + 1)
            ],
        )


def show_posts_with_authors(session: Session) -> None:
    stmt = (
        select(Post)
        .options(
            joinedload(Post.user),
            # subqueryload(Post.user),
        )
        .order_by(
            Post.title,
            Post.id.asc(),
        )
    )
    posts: Sequence[Post] = session.scalars(stmt).all()

    for post in posts:
        print("-", post)
        print(" • author:", post.user)


def show_users_and_their_posts(session: Session) -> None:
    stmt = (
        select(User)
        .where(
            User.email.is_not(None),
        )
        .options(
            selectinload(User.posts),
        )
        .order_by(
            User.username,
        )
    )
    users: Sequence[User] = session.scalars(stmt).all()

    for user in users:
        print("+", user)
        if not user.posts:
            print(" [no posts]")
            continue
        for post in user.posts:
            print(" -", post)


def show_filtered_users_and_their_posts(session: Session) -> None:
    stmt = (
        select(User)
        .join(
            User.posts,
        )
        .where(
            Post.title.like("%-2"),
        )
        .options(
            selectinload(User.posts),
        )
        .order_by(
            User.username,
        )
    )
    users: Sequence[User] = session.scalars(stmt).all()

    for user in users:
        print("+", user)
        if not user.posts:
            print(" [no posts]")
            continue
        for post in user.posts:
            print(" -", post)


def main():
    # print(Base.metadata.tables)
    # Base.metadata.create_all(bind=engine)
    # insert_users()

    with session_factory() as session:
        # create_posts_for_all_users(session)
        # show_posts_with_authors(session)
        # show_users_and_their_posts(session)
        show_filtered_users_and_their_posts(session)


if __name__ == "__main__":
    main()
