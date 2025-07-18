from sqlalchemy import select, exists, func
from sqlalchemy.orm import Session, selectinload, joinedload

from models import Base, engine, User, Post, Tag


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


def create_tag(
    session: Session,
    name: str,
) -> Tag:
    tag = Tag(name=name)
    print("new tag:", tag)
    session.add(tag)
    print("committing...")
    session.commit()
    print("created a new tag:", tag)
    return tag


def create_tags(
    session: Session,
    *names: str,
) -> list[Tag]:
    tags = [Tag(name=name) for name in names]
    print("new tags:", tags)
    session.add_all(tags)
    print("committing...")
    session.commit()
    print("created new tags:", tags)
    return tags


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


def get_posts_with_all(
    session: Session,
) -> list[Post]:
    statement = (
        select(Post)
        .options(
            joinedload(Post.user),
            selectinload(Post.tags),
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


def demo_create_users(
    session: Session,
):
    create_user(
        session,
        name="Bob",
        username="bob",
    )
    create_user(
        session,
        name="Alice",
        username="alice",
        email="alice@example.com",
    )

    create_users(
        session,
        ("Jack Black", "jack"),
        ("Kyle White", "kyle"),
        ("Nick Grey", "nick"),
    )


def demo_create_posts(
    session: Session,
):
    bob: User = find_user(session, "bob")
    create_posts(
        session,
        bob,
        "Python Intro",
        "SQLAlchemy Intro",
        "Postgres tutorial",
    )
    alice = find_user(session, "alice")
    create_posts(
        session,
        alice,
        "JS Intro",
        "drizzle orm intro",
    )
    kyle = find_user(session=session, username="kyle")
    create_posts(session, kyle, "PyCharm Intro")
    users = get_users_with_posts(session)
    for user in users:
        print("==", user)
        print("** posts **")
        for post in user.posts:
            print("-", post.id, post.title)
        print()


def demo_fetch_with_relationships(
    session: Session,
):
    posts = get_posts_with_all(session)
    for post in posts:
        print("+", post.id, post.title)
        print("author:", post.user)
        print(" * Post tags:", post.tags)
        print()

    authors_intro = get_users_by_post_title_match(
        session,
        "intro",
    )
    print("Intro authors:")
    for user in authors_intro:
        print("==", user)


def get_posts_with_tags(
    session: Session,
) -> list[Post]:
    statement = select(Post).options(
        selectinload(Post.tags),
    )
    return list(session.scalars(statement).all())


def get_all_tags(
    session: Session,
):
    statement = select(Tag)
    return list(session.scalars(statement).all())


def auto_associate_posts_with_tags(
    session: Session,
):
    posts = get_posts_with_tags(session)
    tags = get_all_tags(session)
    tags_map = {tag.name.lower(): tag for tag in tags}
    for post in posts:
        post_title = post.title.lower()
        for word in post_title.split():
            if word.lower() not in tags_map:
                new_tag = create_tag(session, word)
                tags_map[word.lower()] = new_tag
            tag = tags_map[word.lower()]
            if tag not in post.tags:
                post.tags.append(tag)
                print("Added tag", tag, "to post", post)

    session.commit()


def fetch_posts_has_tag(
    session: Session,
    tag_name: str,
) -> list[Post]:
    statement = (
        select(Post)
        .join(
            Post.tags,
        )
        .where(
            func.lower(Tag.name) == tag_name.lower(),
        )
        .options(
            selectinload(Post.tags),
        )
        .order_by(Post.title)
    )

    return list(session.scalars(statement).all())


def main():
    with Session(engine) as session:
        # example_sql(session)
        # demo_create_users(session)
        # demo_create_posts(session)
        # demo_fetch_with_relationships(session)

        # create_tags(
        #     session,
        #     "python",
        #     "js",
        #     "Postgres",
        # )
        # auto_associate_posts_with_tags(session)
        # demo_fetch_with_relationships(session)

        posts = fetch_posts_has_tag(session, "intro")
        for post in posts:
            print("+", post.id, post.title)
            print(" * Post tags:", post.tags)
            print()


if __name__ == "__main__":
    main()
