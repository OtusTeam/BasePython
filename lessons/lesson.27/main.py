from random import randint

from sqlalchemy import select, Sequence
from sqlalchemy.orm import (
    Session as SessionType,
    joinedload,
    selectinload,
    with_loader_criteria,
)

from models import (
    Base,
    engine,
    Session,
    User,
    Post,
)


def insert_one(
    session: SessionType,
):
    user = User(
        username="bob",
        email="bob@example.com",
        full_name="Bob White",
    )
    session.add(user)
    print("user before commit:", user)
    session.commit()
    print("user after commit:", user)


def insert_many(
    session: SessionType,
) -> None:
    alice = User(
        username="alice",
        full_name="Alice White",
    )
    john = User(
        username="john",
        email="john@abc.qwe",
    )
    kate = User(
        username="kate",
        full_name="Kate Brown",
        email="kate@ya.ru",
    )
    kyle = User(
        username="kyle",
        full_name="",
    )

    users = [
        alice,
        john,
        kate,
        kyle,
    ]
    session.add_all(users)
    session.commit()


def create_users() -> None:
    with Session() as session:
        insert_one(session)
        insert_many(session)


def select_users(
    session: SessionType,
) -> Sequence[User]:
    statement = select(User).order_by(User.id)
    return session.scalars(statement).all()


def select_users_with_emails(
    session: SessionType,
) -> list[User]:
    statement = (
        select(User)
        .where(
            User.email.is_not(None),
        )
        .order_by(User.id)
    )
    return list(session.scalars(statement).all())


def create_posts_for_user(
    session: SessionType,
    user: User,
) -> list[Post]:
    posts = [
        Post(
            title=f"Post #{idx} by {user.username}",
            user=user,
        )
        for idx in range(1, randint(3, 5))
    ]
    session.add_all(posts)
    session.commit()
    for post in posts:
        print("post:", post)
    return posts


def create_posts_for_users_with_emails():
    with Session() as session:
        users = select_users_with_emails(session)
        for user in users:
            print("user", user)
            create_posts_for_user(
                session,
                user=user,
            )


def select_posts(
    session: SessionType,
) -> list[Post]:
    statement = select(Post).order_by(Post.id)
    return list(session.scalars(statement).all())


def select_posts_with_users(
    session: SessionType,
) -> list[Post]:
    statement = (
        select(Post)
        .options(
            joinedload(Post.user),
        )
        .order_by(Post.id)
    )
    return list(session.scalars(statement).all())


def select_users_with_posts(
    session: SessionType,
) -> list[User]:

    statement = (
        select(User)
        .options(
            selectinload(User.posts),
        )
        .order_by(User.id)
    )
    return list(session.scalars(statement).all())


def select_users_by_post_title_match(
    session: SessionType,
    match_text: str,
) -> list[User]:
    post_filter = Post.title.ilike(f"%{match_text}%")
    statement = (
        select(User)
        .join(User.posts)
        .where(
            post_filter,
        )
        .options(
            # вот так плюс не иметь в кэше все подтянутые объекты
            # потому что если в сессии будут все релейшншипы, алхимия их покажет
            selectinload(User.posts.and_(post_filter)),
        )
        .order_by(User.id)
    )
    return list(session.scalars(statement).all())


def main() -> None:
    print("tables:", Base.metadata.tables)
    Base.metadata.create_all(bind=engine)

    # create_users()
    # create_posts_for_users_with_emails()

    with Session() as session:
        # posts = select_posts_with_users(session)
        # for post in posts:
        #     print("-", post, post.user)
        #
        # users = select_users_with_posts(session)
        # for user in users:
        #     print("*", user)
        #     if not user.posts:
        #         print("[no posts]")
        #         continue
        #     for post in user.posts:
        #         print(" -", post)

        users = select_users_by_post_title_match(
            session,
            "#3",
        )
        for user in users:
            print("*", user)
            print("matching posts:")
            for post in user.posts:
                print(" -", post)


if __name__ == "__main__":
    main()
