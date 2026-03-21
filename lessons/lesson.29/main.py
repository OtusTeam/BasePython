from collections.abc import Sequence
from itertools import cycle

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload, selectinload

from models import Base, engine, User, session_factory, Post, Tag


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


def show_posts_with_tags(session: Session) -> None:
    stmt = (
        select(Post)
        .options(
            selectinload(Post.tags),
        )
        .order_by(Post.title)
    )
    posts: Sequence[Post] = session.scalars(stmt).all()

    for post in posts:
        print("-", post)
        print(" • tags:", post.tags)


def create_posts_with_names_for_all_users(
    session: Session,
    posts_titles: list[str],
) -> None:
    users = fetch_users(session)

    posts = []
    for post_title, user in zip(posts_titles, cycle(users)):
        posts.append(
            Post(
                title=post_title,
                content=f"content for user {user.id} - title {post_title}",
                user=user,
            )
        )

    session.add_all(posts)
    session.commit()
    print("posts:")
    print(posts)


def get_tags(session: Session) -> list[Tag]:

    stmt = select(Tag).order_by(Tag.name)

    tags = session.scalars(stmt).all()
    return list(tags)


def create_tags(
    session: Session,
    tag_names: list[str],
) -> None:
    stmt = select(Tag.name).order_by(Tag.name)
    res_tags_names = session.scalars(stmt).all()
    tags_names = {tag_name.lower() for tag_name in res_tags_names}

    seen = set()
    tags = []  #
    for name in tag_names:
        name_lower = name.lower()
        if name_lower not in tags_names and name_lower not in seen:
            tags.append(Tag(name=name))
            seen.add(name_lower)

    session.add_all(tags)
    session.commit()

    stmt = (
        select(Tag)
        .where(
            Tag.name.in_(tag_names),
        )
        .order_by(Tag.name)
    )
    new_tags = session.scalars(stmt).all()
    print("tags:", new_tags)


def auto_bind_tags_to_posts(
    session: Session,
) -> None:
    stmt = select(Tag)
    all_tags = session.scalars(stmt).all()
    tag_name_to_tag = {tag.name.lower(): tag for tag in all_tags}

    stmt = select(Post).options(
        selectinload(Post.tags),
    )
    all_posts: Sequence[Post] = session.scalars(stmt).all()

    for post in all_posts:
        post_title = post.title.lower().strip()
        for part in post_title.split():
            tag = tag_name_to_tag.get(part.strip())
            if not tag:
                continue
            if tag not in post.tags:
                post.tags.append(tag)

    session.commit()


posts_names = [
    "Python FastAPI Intro",
    "Python Django Intro",
    "Go Intro",
    "JS Intro",
    "Python lesson",
    "Go lesson",
    "Python news",
]

tags_names_create = [
    #
    tag_name.strip()
    for post_name in posts_names
    for tag_name in post_name.split()
]


def main():
    # print(Base.metadata.tables)
    # Base.metadata.create_all(bind=engine)
    # insert_users()

    with session_factory() as session:
        # create_posts_for_all_users(session)
        # show_posts_with_authors(session)
        # show_users_and_their_posts(session)
        # show_filtered_users_and_their_posts(session)
        show_posts_with_tags(session)

        # create_posts_with_names_for_all_users(
        #     session,
        #     posts_names,
        # )
        # create_tags(session, tags_names_create)
        # auto_bind_tags_to_posts(session)


if __name__ == "__main__":
    main()
