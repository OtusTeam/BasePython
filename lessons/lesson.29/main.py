from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload, joinedload

from models import (
    Base,
    User,
    engine,
    session_factory,
    Post,
)


def insert_values(session: Session):
    bob = User(
        username="bob",
        email="bob@example.com",
    )
    kyle = User(
        username="kyle",
    )
    alice = User(
        username="alice",
        full_name="Alice White",
    )
    session.add(bob)
    session.add(kyle)
    session.add(alice)
    session.commit()

    post_1 = Post(
        title="foo",
        body="bar",
        # user_id=bob.id,
        user=bob,
    )
    post_2 = Post(
        title="fizz",
        body="buzz",
        # user_id=bob.id,
        user=bob,
    )
    post_3 = Post(
        title="lala",
        body="bubub",
        # user_id=alice.id,
        user=alice,
    )
    session.add(post_1)
    session.add(post_2)
    session.add(post_3)
    session.commit()


def show_users_with_posts(session: Session):
    stmt = (
        select(User)
        .options(
            selectinload(User.posts),
        )
        .order_by(User.id)
    )
    users = session.scalars(stmt).all()
    for user in users:
        print(user.id, user.username)
        print("with posts:")
        for post in user.posts:
            print(" -", post.title, post.body)


def show_posts_with_users(session: Session):
    stmt = (
        select(Post)
        .options(
            joinedload(Post.user, innerjoin=True),
        )
        .order_by(Post.id)
    )
    posts = session.scalars(stmt).all()
    for post in posts:
        print("Post:", post.id, post.title, post.body)
        print(" by", post.user.id, post.user.username)


def show_posts_from_registered_users(session: Session):
    stmt = (
        select(Post)
        .join(Post.user)
        # .join(
        #     User,
        #     Post.user_id == User.id,
        # )
        .options(
            joinedload(
                Post.user,
                innerjoin=True,
            ),
        )
        .where(
            User.email.isnot(None),
        )
        .order_by(Post.id)
    )
    print(stmt)
    posts = session.scalars(stmt).all()
    for post in posts:
        print("Post:", post.id, post.title, post.body)
        print(" by", post.user.id, post.user.username)


def main():
    with session_factory() as session:
        insert_values(session)
        show_users_with_posts(session)
        show_posts_with_users(session)
        show_posts_from_registered_users(session)


if __name__ == "__main__":
    main()
