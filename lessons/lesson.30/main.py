from collections.abc import Sequence
from itertools import cycle

from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session, selectinload, joinedload, subqueryload

from models import (
    Base,
    User,
    engine,
    session_factory,
    Post,
    Tag,
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


def fetch_users(session: Session) -> list[User]:
    stmt = select(User).order_by(User.id)
    users = session.scalars(stmt).all()
    return list(users)


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
            name=name,
            display_name=display_name,
        )
        for name, display_name in tags_slugs_create
    ]
    print("prepared tags:", tags)
    session.add_all(tags)
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

    tag_name_to_tag = {tag.name: tag for tag in all_tags}

    for post in all_posts:
        post_title = post.title.lower()
        for title_word in post_title.split():
            tag = tag_name_to_tag.get(title_word.strip())
            if not tag:
                continue
            if tag not in post.tags:
                post.tags.append(tag)

    session.commit()


def show_posts_with_tags(session: Session) -> None:
    stmt = (
        select(Post)
        .where(
            or_(
                Post.title.ilike("%lesson%"),
                Post.title.ilike("%intro%"),
            )
        )
        .options(
            selectinload(Post.tags),
        )
    )
    posts = session.scalars(stmt).all()
    for post in posts:
        print(post)
        print(" *", *[tag.name for tag in post.tags])


def show_posts_with_tags_and_authors(session: Session) -> None:
    stmt = (
        select(Post)
        .where(
            or_(
                Post.title.ilike("%lesson%"),
                Post.title.ilike("%intro%"),
            )
        )
        .options(
            selectinload(Post.tags),
            joinedload(Post.user, innerjoin=True),
        )
    )
    posts = session.scalars(stmt).all()
    for post in posts:
        print(post, "by", post.user.username)
        print(" *", *[tag.name for tag in post.tags])


def show_users_with_posts_with_tags(session: Session) -> None:
    stmt = (
        select(User)
        .where(func.length(User.username) > 3)
        .options(
            # selectinload(User.posts).selectinload(Post.tags),
            subqueryload(User.posts).subqueryload(Post.tags),
        )
    )
    users = session.scalars(stmt).all()
    for user in users:
        print(user.username, user.full_name)
        for post in user.posts:
            print(" Post:", post)
            tags_names = [tag.name for tag in post.tags]
            if tags_names:
                print("  *", *tags_names)


def main():
    with session_factory() as session:
        # insert_values(session)
        # show_users_with_posts(session)
        # show_posts_with_users(session)
        # show_posts_from_registered_users(session)
        # create_tags(session)
        # create_posts_for_users(session)
        # auto_assign_new_tags_to_posts(session)
        # show_posts_with_tags(session)
        # show_posts_with_tags_and_authors(session)
        show_users_with_posts_with_tags(session)


if __name__ == "__main__":
    main()
