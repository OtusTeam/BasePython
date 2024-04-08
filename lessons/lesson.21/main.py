from typing import Sequence

from sqlalchemy import (
    select,
    update,
    func,
)
from sqlalchemy import text
from sqlalchemy.orm import (
    Session,
    joinedload,
    selectinload,
)

from models import (
    Base,
    User,
    Post,
)
from models.db import engine


def create_tables():
    Base.metadata.create_all(bind=engine)


def example_calc(session: Session):
    result = session.execute(select(1))

    # print(result.all())
    # print(result.one())
    print(result.scalar())

    # SELECT 1 + 2;
    result = session.execute(select(text("1 + 2")))
    print(result.scalar())


def create_user(
    session: Session,
    username: str,
    email: str | None = None,
) -> User:
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    print("created user:", user)
    return user


def create_post(
    session: Session,
    title: str,
    user_id: int,
) -> Post:
    post = Post(title=title, user_id=user_id)
    session.add(post)
    session.commit()
    print("created post:", post)
    return post


def create_users(
    session: Session,
    *usernames: str,
) -> list[User]:
    users = [
        User(username=username)
        for username in usernames
    ]
    session.add_all(users)
    print("prepared users:", users)
    session.commit()

    print("created users:", users)
    return users


def create_posts(
    session: Session,
    *titles: str,
    user_id: int,
) -> list[Post]:
    posts = [
        Post(title=title, user_id=user_id)
        for title in titles
    ]
    session.add_all(posts)
    session.commit()
    print("created posts:", posts)
    return posts


def fetch_all_users(session: Session) -> list[User]:
    stmt = select(User).order_by(User.id)
    users = session.scalars(stmt).all()
    # result = session.execute(stmt)
    # users = result.scalars().all()
    users_list = list(users)
    for user in users_list:
        print(user)
    return users_list


def fetch_user_by_id(session: Session, user_id: int) -> User | None:
    # stmt = select(User).where(User.id == user_id)
    # user = session.scalar(stmt)
    user = session.get(User, user_id)
    print("user:", user)
    return user


def fetch_user_by_username(session: Session, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    user = session.scalar(stmt)
    print("user:", user)
    return user


def update_users_emails(
    session: Session,
    username_len: int,
    email_domain: str,
):
    stmt = update(User).where(
        User.email.is_(None),
        func.length(User.username) > username_len,
    ).values(
        {
            User.email: func.concat(func.lower(User.username), email_domain.lower()),
            # User.username: "aqwe"
        }
    )
    session.execute(stmt)
    # print(result.all())
    session.commit()


def fetch_users_for_domain(session: Session, domain: str) -> list[User]:
    stmt = select(User).where(
        User.email.ilike(f"%{domain.lower()}")
    )
    users = session.scalars(stmt).all()
    print(f"users for domain {domain}:", users)
    return users


def fetch_posts_for_user_id(
    session: Session,
    user_id: int,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .where(Post.user_id == user_id)
        .order_by(Post.id)
    )
    posts = session.scalars(stmt)
    return posts.all()


def fetch_users_with_posts(
    session: Session,
) -> Sequence[User]:
    stmt = (
        select(User)
        # .where(func.length(User.username) > 3)
        .options(
            # joinedload(User.posts),
            selectinload(User.posts),
        )
        .order_by(User.id)
    )
    users = session.scalars(stmt)
    # return users.unique().all()
    return users.all()


def fetch_authors_with_posts(
    session: Session,
) -> Sequence[User]:
    """
    Left join to get only users with posts
    """
    stmt = (
        select(User)
        .join(
            User.posts,
        )
        # .join(
        #     Post,
        #     # Post.user_id == User.id,
        # )
        # .join(
        #     Post,
        #     Post.user_id == User.id,
        # )
        .options(
            joinedload(User.posts)
        )
        .order_by(User.id)
    )
    users = session.scalars(stmt)
    return users.unique().all()


def fetch_posts_with_authors(
    session: Session,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .options(
            # joinedload(Post.author),
            selectinload(Post.author),
        )
        .order_by(Post.id)
    )
    posts = session.scalars(stmt)
    return posts.all()


def demo(session: Session):
    # user_john = create_user(session, "john")
    # user_sam = create_user(session, "sam")
    # user_nick = create_user(session, "nick")
    #
    # create_post(session, "Intro Lesson", user_id=user_john.id)
    # create_posts(
    #     session,
    #     "SQL Introduction",
    #     "MySQL Lesson",
    #     "Postgres Lesson",
    #     user_id=user_sam.id,
    # )
    # 1
    # for user_id in (0, 1, 2, 10):
    #     posts = fetch_posts_for_user_id(session, user_id)
    #     if not posts:
    #         print("no posts for user id", user_id)
    #         continue
    #     print("++user id posts", user_id)
    #     for post in posts:
    #         print("-", post)
    # 2
    users_with_posts = fetch_users_with_posts(session)
    for user in users_with_posts:
        print("++ posts for user", user)
        for post in user.posts:
            print("-", post)

    # # 3
    # authors_with_posts = fetch_authors_with_posts(session)
    # for user in authors_with_posts:
    #     print("++ posts for author", user)
    #     for post in user.posts:
    #         print("-", post)

    # 4
    posts_with_authors = fetch_posts_with_authors(session)
    for post in posts_with_authors:
        print("post", (post.id, post.title), "author:", post.author)


def main():
    # Base.metadata.drop_all(bind=engine)
    create_tables()

    with Session(engine) as session:
        demo(session)


if __name__ == "__main__":
    main()
