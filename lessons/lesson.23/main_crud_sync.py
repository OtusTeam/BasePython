from typing import Sequence

from sqlalchemy import select
from sqlalchemy import and_
from sqlalchemy import func
from sqlalchemy import update
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session, joinedload, selectinload

from config import engine
from models import Base
from models import Post
from models import User


def create_user(
    session: Session,
    username: str,
    email: str | None = None,
) -> User:
    user = User(
        username=username,
        email=email,
    )
    print(user)
    session.add(user)
    session.commit()
    print("saved user")
    print("user details:", user)
    return user


def create_users(
    session: Session,
    *usernames: str,
) -> list[User]:
    users = [User(username=username) for username in usernames]
    session.add_all(users)
    session.commit()
    print("saved users:", users)
    return users


def get_user_by_id(
    session: Session,
    user_id: int,
) -> User | None:
    """
    From cache

    :param session:
    :param user_id:
    :return:
    """
    user = session.get(User, user_id)
    print(user)
    # if user is None:
    #     raise ...
    return user


def find_user_by_id(
    session: Session,
    user_id: int,
) -> User | None:
    stmt = select(User).where(User.id == user_id)
    # result: Result = session.execute(stmt)
    # user = result.scalar_one_or_none()
    user = session.scalar(stmt)
    if user is None:
        print("no user by id", user_id)
    else:
        print("found user", user)

    return user


def find_user_by_username(
    session: Session,
    username: str,
) -> User | None:
    # stmt = select(User).where(User.username == username)
    stmt = select(User).where(User.username.ilike(username))
    # stmt = select(User).where(func.lower(User.username) == func.lower(username))
    # result: Result = session.execute(stmt)
    # user = result.scalar_one_or_none()
    user = session.scalar(stmt)
    if user is None:
        print("no user by username", username)
    else:
        print("found user", user)

    return user


def demo_update_users(session: Session):
    fltr_u_w_o = User.username.ilike("%o%")
    stmt_users_w_o = select(User).where(fltr_u_w_o)
    users_w_o = session.scalars(stmt_users_w_o).all()
    print(users_w_o)
    upd_stmt = (
        update(User)
        .where(fltr_u_w_o)
        .values(
            {
                User.email: func.concat(User.username, "@ya.ru"),
                # User.email: "abc",
            }
        )
    )
    session.execute(upd_stmt)
    session.commit()
    users_w_o = session.scalars(stmt_users_w_o).all()
    print(users_w_o)


def find_users(
    session: Session,
) -> Sequence[User]:
    stmt = (
        select(User)
        .where(
            # or_(
            and_(
                User.email.isnot(None),
                User.username.ilike("%n%"),
            ),
        )
        .order_by(User.id)
    )
    users = session.scalars(stmt).all()
    print(users)
    return users


def create_post(
    session: Session,
    user_id: int,
    title: str,
) -> Post:
    post = Post(
        title=title,
        user_id=user_id,
    )
    session.add(post)
    session.commit()
    print(post)
    return post


def show_posts_with_authors(session: Session):
    # stmt = select(Post).where(Post.id == 1).order_by(Post.id)
    # stmt = select(Post).order_by(Post.id)

    # stmt = select(Post.id, Post.title)
    # stmt = select(Post.id, )
    # result: Result = session.execute(stmt)
    # # items = result.scalars().all()
    # items = result.scalars().all()
    # post = result.one_or_none()
    # post = result.one()
    # post = result.scalar_one()
    # post = result.scalar_one_or_none()
    # print(post)
    # return
    # items = result.all()
    # print(items)
    # # for (item,) in items:
    # for item in items:
    #     print("item:", item)
    #     print("- item.id:", item.id)
    #     print("- item.title:", item.title)

    stmt = (
        select(Post)
        .join(Post.user)
        # .where(User.email.isnot(None))
        .where(User.email.is_(None))
        # .options(joinedload(Post.user))
        .options(selectinload(Post.user))
        .order_by(Post.id)
    )

    for post in session.scalars(stmt).all():  # type: Post
        print("-", post, "by", post.user.username, post.user.email)


def show_users_with_posts(session: Session):
    stmt = (
        select(User)
        # .where(User.id <= 2)
        .options(selectinload(User.posts))
        .order_by(User.id)
    )
    for user in session.scalars(stmt).all():  # type: User
        print(user)
        for post in user.posts:  # type: Post
            print("-", post)


def show_filtered_users_with_posts(session: Session):
    stmt = (
        select(User)
        .join(User.posts)
        # .join(
        #     Post,
        #     Post.user_id == User.id,
        # )
        # .where(Post.title.ilike("Post by%"))
        # .where(Post.title.ilike("Another%"))
        # .where()
        .group_by(User.id)
        .having(func.count(Post.id) >= 2)
        .options(selectinload(User.posts))
        # .options(joinedload(User.posts))
        .order_by(User.id)
    )
    for user in session.scalars(stmt).unique().all():  # type: User
        print(user)
        for post in user.posts:  # type: Post
            print("-", post)


def show_count_posts(session: Session):
    stmt = select(func.count(Post.id))
    print("posts count:", session.scalar(stmt))


def main():
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    with Session(engine) as session:
        john = create_user(session, "john")
        sam = create_user(session, "sam")
        bob = create_user(session, "bob")

        post1_by_john = create_post(session, user_id=john.id, title="Post by John")
        post2_by_john = create_post(session, user_id=john.id, title="Another post by John")
        post_by_sam = create_post(session, user_id=sam.id, title="Post by Sam")
        show_posts_with_authors(session)
        show_users_with_posts(session)
        show_posts_with_authors(session)
        show_filtered_users_with_posts(session)
        show_count_posts(session)


        # bob = create_user(session, "bob")
        # nick = create_user(session, "nick")

        # create_users(session, "sam", "bob", "nick")
        # get_user_by_id(session, 1)
        # get_user_by_id(session, 2)
        # get_user_by_id(session, 1)
        # find_user_by_id(session, 1)
        # find_user_by_id(session, 2)
        # find_user_by_id(session, 5)
        # find_user_by_username(session, "qwerty")
        # find_user_by_username(session, "bob")
        # find_user_by_username(session, "Nick")
        # find_user(session)
        # demo_update_users(session)
        # find_users(session)


if __name__ == "__main__":
    main()
