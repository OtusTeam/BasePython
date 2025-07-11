from sqlalchemy import select, exists
from sqlalchemy.orm import Session, selectinload, joinedload

from models import Base, engine, User, Post


def create_user(
    session: Session,
    name: str,
    username: str,
    email: str | None = None,
) -> User:
    user = User(
        name=name,
        username=username,
        email=email,
    )
    print("new user:", user)
    session.add(user)
    print("committing...")
    session.commit()
    print("created a new user:", user)
    return user


def create_users(
    session: Session,
    *names_and_usernames: tuple[str, str],
) -> list[User]:
    users = [
        User(name=name, username=username) for name, username in names_and_usernames
    ]
    print("new users:", users)
    session.add_all(users)
    print("committing...")
    session.commit()
    print("created new users:", users)
    return users


def create_posts(
    session: Session,
    user,
    *titles: str,
) -> list[Post]:
    posts = [Post(title=title, user_id=user.id) for title in titles]
    print("new posts:", posts)
    session.add_all(posts)
    print("committing...")
    session.commit()
    print("created new posts:", posts)
    return posts


def find_user(
    session: Session,
    username: str,
) -> User:
    statement = select(User).where(
        User.username == username,
    )
    # return session.scalar(statement)
    result = session.execute(statement)
    return result.scalar_one()


def get_users_with_posts(
    session: Session,
) -> list[User]:
    statement = (
        select(User)
        .options(
            selectinload(User.posts),
        )
        .order_by(User.id)
    )

    return list(session.scalars(statement).all())


def get_posts_with_authors(
    session: Session,
) -> list[Post]:
    statement = (
        select(Post)
        .options(
            joinedload(Post.user),
        )
        .order_by(Post.title)
    )
    return list(session.scalars(statement).all())


def get_users_by_post_title_match(
    session: Session,
    title_match: str,
) -> list[User]:
    # statement = (
    #     select(User)
    #     .join(Post)
    #     # .join(Post, Post.user_id == User.id)
    #     .where(
    #         Post.title.ilike(f"%{title_match}%"),
    #     )
    #     .order_by(User.id)
    # )
    # return list(session.scalars(statement).unique().all())

    statement = (
        select(User)
        .where(
            exists(1).where(
                Post.user_id == User.id,
                Post.title.ilike(f"%{title_match}%"),
            )
        )
        .order_by(User.id)
    )
    return list(session.scalars(statement).all())


def main():
    # print(Base.metadata.tables)
    # Base.metadata.create_all(bind=engine)
    # return
    with Session(engine) as session:
        # example_sql(session)
        # create_user(
        #     session,
        #     name="Bob",
        #     username="bob",
        # )
        # create_user(
        #     session,
        #     name="Alice",
        #     username="alice",
        #     email="alice@example.com",
        # )

        # create_users(
        #     session,
        #     ("Jack Black", "jack"),
        #     ("Kyle White", "kyle"),
        #     ("Nick Grey", "nick"),
        # )

        # bob: User = find_user(session, "bob")
        # create_posts(
        #     session,
        #     bob,
        #     "Python Intro",
        #     "SQLAlchemy Intro",
        #     "Postgres tutorial",
        # )
        # alice = find_user(session, "alice")
        # create_posts(
        #     session,
        #     alice,
        #     "JS Intro",
        #     "drizzle orm intro",
        # )
        # kyle = find_user(session=session, username="kyle")
        # create_posts(session, kyle, "PyCharm Introduction")
        # users = get_users_with_posts(session)
        # for user in users:
        #     print("==", user)
        #     print("** posts **")
        #     for post in user.posts:
        #         print("-", post.id, post.title)
        #     print()

        # posts = get_posts_with_authors(session)
        # for post in posts:
        #     print("+", post.id, post.title)
        #     print("author:", post.user)
        #     print()

        authors_intro = get_users_by_post_title_match(
            session,
            "intro",
        )
        print("Intro authors:")
        for user in authors_intro:
            print("==", user)


if __name__ == "__main__":
    main()
