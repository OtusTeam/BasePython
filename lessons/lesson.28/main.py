from datetime import datetime
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session as SessionType, joinedload, selectinload

from models.db import Session
from models import Base, User, Post, UserStatus


def create_users() -> None:
    bob = User(
        username="bob",
        email="bob@example.com",
        created_at=datetime.utcnow(),
    )
    alice = User(
        username="alice",
        email="alice@example.com",
    )
    john = User(
        username="john",
        full_name="John Smith",
    )
    with Session() as session:
        session.add(bob)
        print("bob", bob.id, "'created at' before commit", bob.created_at)
        session.commit()
        print("bob", bob.id, "'created at' after commit", bob.created_at)

        session.add(alice)
        session.add(john)
        session.commit()


def get_user_by_username(
    session: SessionType,
    username: str,
) -> User:
    statement = select(User).where(User.username == username)
    result = session.execute(statement)
    return result.scalar_one()


def create_post(
    session: SessionType,
    title: str,
    body: str,
    user_id: int,
) -> None:
    post = Post(
        title=title,
        body=body,
        user_id=user_id,
    )
    session.add(post)
    session.commit()


def create_posts(
    session: SessionType,
    *titles: str,
    user: User,
) -> list[Post]:
    posts = [
        Post(
            title=title,
            user=user,
        )
        for title in titles
    ]
    session.add_all(posts)
    session.commit()
    return posts


def get_users_with_posts(
    session: SessionType,
) -> Sequence[User]:
    statement = (
        select(User)
        # .join(Post)
        # .join(User.posts)
        .join(
            User.posts,
            isouter=False,
        )
        # .join(
        #     Post,
        #     Post.user_id == User.id,
        # )
        .options(
            # joinedload(User.posts),
            selectinload(User.posts),
        ).order_by(User.id)
    )
    # result = session.execute(statement)
    # return result.scalars().all()
    # return session.scalars(statement).all()
    return session.scalars(statement).unique().all()


def get_posts_with_author(
    session: SessionType,
) -> Sequence[Post]:
    statement = (
        select(Post)
        .options(
            joinedload(Post.user),
            # selectinload(Post.user),
        )
        .order_by(Post.id)
    )
    return session.scalars(statement).all()


def create_statuses(
    session: SessionType,
) -> None:
    status_active = UserStatus(
        name="active",
        description="User is active",
    )
    status_prospect = UserStatus(
        name="prospect",
        description="User is prospect",
    )

    session.add(status_active)
    session.add(status_prospect)
    session.commit()


def main() -> None:
    print(Base.metadata.tables)
    print(repr(User.__table__))
    create_users()
    with Session() as session:
        create_statuses(session)
        bob = get_user_by_username(session, "bob")
        create_post(
            session=session,
            title="Post Title",
            body="Post Body",
            user_id=bob.id,
        )
        john = get_user_by_username(session, "john")
        create_posts(
            session,
            "Green Post",
            "Red Post",
            "Black Post",
            user=john,
        )
        users_w_posts = get_users_with_posts(session)
        for user in users_w_posts:
            print("@", user)
            if not user.posts:
                print("- no posts for user", user.username)
                continue
            for post in user.posts:
                print("+", post)

        print()
        print()
        print()

        posts_w_author = get_posts_with_author(session)
        for post in posts_w_author:
            print("+", post)
            print("@", post.user)


if __name__ == "__main__":
    main()
