from collections.abc import Sequence

from sqlalchemy import desc
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import selectinload

from models import engine, Base, User, Post


def create_tables():
    # Base.metadata.drop_all(bind=engine)
    print("Creating tables...", Base.metadata.tables)
    Base.metadata.create_all(bind=engine)


def create_user(
    session: Session,
    username: str,
    email: str | None = None,
) -> User:
    user = User(username=username, email=email)
    session.add(user)

    session.commit()

    print("user created:", user)
    return user


def create_post(
    session: Session,
    title: str,
    user_id: int,
) -> Post:
    post = Post(title=title, user_id=user_id)
    # post.author = user
    session.add(post)
    session.commit()
    print("post created:", post)
    return post


def create_users(
    session: Session,
    *usernames: str,
) -> Sequence[User]:
    users = [
        User(username=username)
        for username in usernames
    ]
    session.add_all(users)
    print("prepared users:", users)

    session.commit()

    print("saved users:", users)
    return users


def create_posts(
    session: Session,
    *titles: str,
    user_id: int,
) -> Sequence[Post]:
    posts = [
        Post(title=title, user_id=user_id)
        for title in titles
    ]
    session.add_all(posts)
    print("prepared posts:", posts)
    session.commit()
    print("saved posts:", posts)
    return posts


def fetch_all_users(session: Session) -> Sequence[User]:
    # stmt = select(User).order_by(User.id)
    stmt = select(User).order_by(desc(User.username))
    # result = session.execute(stmt)
    # users = result.scalars().all()
    users = session.scalars(stmt).all()
    print("users:", users)
    return users


def fetch_users_with_posts(
    session: Session,
) -> Sequence[User]:
    stmt = (
        select(User)
        .options(
            # joinedload(User.posts),
            selectinload(User.posts),
        )
        .order_by(User.id)
    )

    print("load users w/ posts:")
    # users = session.scalars(stmt).unique().all()
    users = session.scalars(stmt).all()
    for user in users:
        print("+", user)
        for post in user.posts:
            print("  -", post)

    return users


def fetch_all_posts(session: Session) -> Sequence[Post]:
    stmt = select(Post).order_by(Post.id)
    # result = session.execute(stmt)
    # posts = result.scalars().all()
    posts = session.scalars(stmt).all()
    print("posts:", posts)
    return posts


def fetch_all_posts_with_authors(
    session: Session,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .options(
            joinedload(Post.author),
        )
        .order_by(Post.id)
    )
    posts = session.scalars(stmt).all()
    print("posts:", posts)

    for post in posts:
        print("+", post)
        print("= author:", post.author)

    return posts


def fetch_user_by_username(session: Session, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    # result = session.execute(stmt)
    # user = result.scalars().one_or_none()
    user: User | None = session.scalars(stmt).one_or_none()
    print("user for username", repr(username), "result:", user)
    return user


SQL = """
UPDATE users 
SET email=concat(
    lower(users.username), 
    '@ya.ru'::VARCHAR
)
WHERE users.email IS NULL 
    AND length(users.username) < 5::INTEGER;
"""


def set_emails_for_null_email_users_with_username_limit(
    session: Session,
    username_size_limit: int,
    domain: str,
):
    """

    :param session:
    :param username_size_limit:
    :param domain: example: '@ya.ru'
    :return:
    """

    new_email = (
        func.concat(
            func.lower(User.username),
            domain.lower(),
        )
    )
    stmt = (
        update(User)
        .where(
            # empty email
            User.email.is_(None),
            # username len limit
            func.length(User.username) < username_size_limit,
        )
        .values(
            {
                User.email: new_email,
            }
        )
    )

    session.execute(stmt)
    session.commit()


def select_top_users_with_posts_sorted(
    session: Session,
) -> None:
    users_w_posts_count_stmt = (
        select(User, func.count(Post.id).label('posts_count'))
        .join(User.posts, isouter=True)
        .group_by(User.id)
        .order_by(func.count(Post.id).desc(), User.username)
    )
    result = session.execute(users_w_posts_count_stmt).all()
    for user, posts_count in result:
        print("+ user", user.id, user.username, "w/", posts_count, "posts")


def main():
    # create_tables()
    with Session(engine) as session:
        # create_user(session, username="admin", email="admin@admin.com")
        # john = create_user(session, username="john", email=None)
        # post_pg = create_post(
        #     session=session,
        #     title="PostgreSQL news",
        #     user_id=john.id,
        # )
        # print("post pg:", post_pg)
        # create_users(session, "nick", "bob", "alice")
        # sam = create_user(session, username="sam", email=None)
        # create_posts(
        #     session,
        #     "MySQL Intro",
        #     "MariaDB Lesson",
        #     user_id=sam.id,
        # )

        # fetch_all_users(session)
        # fetch_users_with_posts(session)

        # posts = fetch_all_posts(session)
        # fetch_all_posts_with_authors(session)
        #
        # for post in posts:
        #     print("+", post)
        #     print("= author:", post.author)

        # fetch_user_by_username(session, "bob")
        # fetch_user_by_username(session, "jack")
        # set_emails_for_null_email_users_with_username_limit(
        #     session,
        #     username_size_limit=5,
        #     domain="@ya.ru",
        # )

        select_top_users_with_posts_sorted(session)

        # запрашиваем посты авторов, у кого юзернейм длиной более 3 символов
        # stmt = (
        #     select(Post)
        #     # .join(User)
        #     # .join(User, Post.user_id == User.id)
        #     .join(Post.author)
        #     .where(func.length(User.username) > 3)
        #     .options(
        #         # joinedload(Post.author),
        #         selectinload(Post.author),
        #     )
        #     .order_by(Post.id)
        # )
        #
        # posts = session.scalars(stmt).all()
        # print(posts)


if __name__ == "__main__":
    main()
