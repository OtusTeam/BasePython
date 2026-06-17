from collections.abc import Sequence
from itertools import cycle

from sqlalchemy import select, func
from sqlalchemy.orm import Session, selectinload, joinedload

from models import Base, engine, User, Post, session_factory, Tag


def insert_users(
    session: Session,
):
    john = User(
        username="john",
        email="john@example.com",
    )
    john.hello()
    print(john)

    session.add(john)
    session.commit()
    print("committed")
    print("new john:", john)

    bob = User(
        username="bob",
        email="bob@example.com",
        full_name="Bob Black",
    )
    alice = User(
        username="alice",
        full_name="Alice",
    )
    new_users = [bob, alice]
    session.add_all(new_users)
    session.commit()
    print("committed")
    print("new users:", new_users)


def get_user(
    session: Session,
    username: str,
) -> User:
    stmt = select(User).where(User.username == username)
    result = session.execute(stmt)
    return result.scalar_one()


def insert_posts(
    session: Session,
    user: User,
    *posts_titles: str,
):
    posts = [
        Post(
            title=title,
            user=user,
        )
        for title in posts_titles
    ]
    session.add_all(posts)
    session.commit()


def create_posts(session: Session):
    insert_posts(
        session,
        get_user(session, "bob"),
        "Hello World (by Bob)",
    )
    insert_posts(
        session,
        get_user(session, "alice"),
        "Python lessons",
        "SQlite lessons",
    )


def fetch_users(session: Session) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    return session.scalars(stmt).all()


def fetch_users_with_posts(session: Session) -> Sequence[User]:
    stmt = (
        select(User)
        # .where(User.email.isnot(None))
        # .where(func.length(User.username) > 3)
        .options(
            selectinload(User.posts),
        ).order_by(User.id)
    )
    return session.scalars(stmt).all()


def show_users(session: Session):
    # users = fetch_users(session)
    users = fetch_users_with_posts(session)
    for user in users:
        print("-", user)
        for post in user.posts:
            print(" ·", post)


def fetch_posts(session: Session) -> Sequence[Post]:
    stmt = select(Post).order_by(Post.id)
    return session.scalars(stmt).all()


def fetch_posts_with_user(session: Session) -> Sequence[Post]:
    stmt = (
        select(Post)
        .options(
            joinedload(Post.user),
        )
        .order_by(Post.id)
    )
    return session.scalars(stmt).all()


def show_posts(session: Session):
    # posts = fetch_posts(session)
    posts = fetch_posts_with_user(session)
    for post in posts:
        print("-", post)
        print("   by", post.user)


posts_titles = [
    "Python FastAPI Intro",
    "Python Django Intro",
    "Go Intro",
    "JS Intro",
    "Python lesson",
    "Go lesson",
    "Python news",
]

tags_slugs_create: set[tuple[str, str]] = {
    (tag_slug.strip().lower(), tag_slug.strip())
    for post_title in posts_titles
    for tag_slug in post_title.split()
}


def create_tags(session: Session) -> None:
    tags = [
        Tag(
            slug=tag_slug,
            display_name=tag_title,
        )
        for tag_slug, tag_title in tags_slugs_create
    ]
    session.add_all(tags)
    print("new tags:", tags)
    session.commit()
    print("saved tags:", tags)


def create_posts_for_users(session: Session) -> None:
    users = fetch_users(session)
    posts = [
        Post(
            title=post_title,
            user=user,
        )
        for post_title, user in zip(posts_titles, cycle(users))
    ]
    session.add_all(posts)
    session.commit()
    print("saved posts:", posts)


def auto_assign_new_tags_to_posts(session: Session) -> None:
    all_tags: Sequence[Tag] = session.scalars(select(Tag)).all()
    all_posts: Sequence[Post] = session.scalars(
        select(Post).options(
            selectinload(Post.tags),
        )
    ).all()

    tag_slug_to_tag = {tag.slug: tag for tag in all_tags}

    for post in all_posts:
        post_title = post.title.lower()
        for title_word in post_title.split():
            tag = tag_slug_to_tag.get(title_word.strip())
            if not tag:
                continue
            if tag not in post.tags:
                post.tags.append(tag)
                # print("adding tag", tag, "to post", post)

    session.commit()


def fetch_posts_with_tags(session: Session) -> Sequence[Post]:
    return session.scalars(
        select(Post).options(
            selectinload(Post.tags),
        )
    ).all()


def fetch_posts_with_tags_and_authors(session: Session) -> Sequence[Post]:
    return session.scalars(
        select(Post).options(
            selectinload(Post.tags),
            joinedload(Post.user),
        )
    ).all()


def fetch_users_with_posts_with_tags(session: Session) -> Sequence[User]:
    stmt = (
        select(User)
        .options(
            selectinload(
                User.posts,
            ).selectinload(
                Post.tags,
            ),
        )
        .where(
            func.length(User.username) > 3,
        )
        .order_by(
            User.username,
        )
    )
    return session.scalars(stmt).all()


def show_posts_with_tags(session: Session) -> None:
    posts = fetch_posts_with_tags(session)
    for post in posts:
        print("-", post)
        for tag in post.tags:
            print("  ª", tag)


def show_posts_with_tags_and_authors(session: Session) -> None:
    posts = fetch_posts_with_tags_and_authors(session)
    for post in posts:
        print("-", post, "by", post.user)
        for tag in post.tags:
            print("  ª", tag)


def show_users_with_posts_with_tags(session: Session) -> None:
    users = fetch_users_with_posts_with_tags(session)
    for user in users:
        print("-", user)
        for post in user.posts:
            print(" ·", post)
            for tag in post.tags:
                print("  ª", tag)


def fetch_users_with_posts_with_tags_by_post_title(
    session: Session,
    text_match: str,
) -> Sequence[User]:
    stmt = (
        select(User)
        .join(User.posts)
        .options(
            selectinload(
                User.posts,
            ).selectinload(
                Post.tags,
            ),
        )
        .where(
            func.length(User.username) > 3,
            Post.title.ilike(text_match),
        )
        .order_by(
            User.username,
        )
    )
    return session.scalars(stmt).unique().all()


def show_users_with_posts_with_tags_by_post_title(
    session: Session, text_part: str
) -> None:
    users = fetch_users_with_posts_with_tags_by_post_title(
        session,
        f"%{text_part.replace('%', '%%')}%",
    )
    for user in users:
        print("-", user)
        for post in user.posts:
            print(" ·", post)
            for tag in post.tags:
                print("  ª", tag)


def main():
    # print("Tables:", Base.metadata.tables)

    print(tags_slugs_create)
    with session_factory() as session:
        # insert_users(session)
        # create_posts(session)
        # show_users(session)
        # show_posts(session)
        # create_tags(session)
        # create_posts_for_users(session)
        # auto_assign_new_tags_to_posts(session)
        # show_posts_with_tags(session)
        # show_posts_with_tags_and_authors(session)
        # show_users_with_posts_with_tags(session)
        show_users_with_posts_with_tags_by_post_title(session, "Go")
        show_users_with_posts_with_tags_by_post_title(session, "Python")
        show_users_with_posts_with_tags_by_post_title(session, "news")


if __name__ == "__main__":
    main()
