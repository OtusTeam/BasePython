from itertools import cycle
from random import randint

from sqlalchemy import select, Sequence, not_
from sqlalchemy.orm import (
    Session as SessionType,
    joinedload,
    selectinload,
    with_loader_criteria,
    load_only,
    subqueryload,
)

from models import (
    Base,
    engine,
    Session,
    User,
    Post,
    Tag,
)


def insert_one(
    session: SessionType,
):
    user = User(
        username="bob",
        email="bob@example.com",
        full_name="Bob White",
    )
    session.add(user)
    print("user before commit:", user)
    session.commit()
    print("user after commit:", user)


def insert_many(
    session: SessionType,
) -> None:
    alice = User(
        username="alice",
        full_name="Alice White",
    )
    john = User(
        username="john",
        email="john@abc.qwe",
    )
    kate = User(
        username="kate",
        full_name="Kate Brown",
        email="kate@ya.ru",
    )
    kyle = User(
        username="kyle",
        full_name="",
    )

    users = [
        alice,
        john,
        kate,
        kyle,
    ]
    session.add_all(users)
    session.commit()


def create_users() -> None:
    with Session() as session:
        insert_one(session)
        insert_many(session)


def select_users(
    session: SessionType,
) -> Sequence[User]:
    statement = select(User).order_by(User.id)
    return session.scalars(statement).all()


def select_tags(
    session: SessionType,
) -> list[Tag]:
    statement = select(Tag)
    return list(session.scalars(statement).all())


def select_users_with_emails(
    session: SessionType,
) -> list[User]:
    statement = (
        select(User)
        .where(
            User.email.is_not(None),
        )
        .order_by(User.id)
    )
    return list(session.scalars(statement).all())


def select_users_with_emails_not_end_with(
    session: SessionType, ends_with: str = "@invalid.mail"
) -> list[int]:
    statement = (
        select(User.id)
        .where(
            not_(
                User.email.endswith(ends_with),
            ),
        )
        .order_by(User.id)
    )
    return list(session.scalars(statement).all())


def create_posts_for_user(
    session: SessionType,
    user: User,
) -> list[Post]:
    posts = [
        Post(
            title=f"Post #{idx} by {user.username}",
            user=user,
        )
        for idx in range(1, randint(3, 5))
    ]
    session.add_all(posts)
    session.commit()
    for post in posts:
        print("post:", post)
    return posts


def create_posts_for_users_with_emails():
    with Session() as session:
        users = select_users_with_emails(session)
        for user in users:
            print("user", user)
            create_posts_for_user(
                session,
                user=user,
            )


def select_posts(
    session: SessionType,
) -> list[Post]:
    statement = select(Post).order_by(Post.id)
    return list(session.scalars(statement).all())


def select_posts_with_users(
    session: SessionType,
) -> list[Post]:
    statement = (
        select(Post)
        .options(
            joinedload(Post.user),
        )
        .order_by(Post.id)
    )
    return list(session.scalars(statement).all())


def select_users_with_posts(
    session: SessionType,
) -> list[User]:

    statement = (
        select(User)
        .options(
            selectinload(User.posts),
        )
        .order_by(User.id)
    )
    return list(session.scalars(statement).all())


def select_users_by_post_title_match(
    session: SessionType,
    match_text: str,
) -> list[User]:
    post_filter = Post.title.ilike(f"%{match_text}%")
    statement = (
        select(User)
        .join(User.posts)
        .where(
            post_filter,
        )
        .options(
            # вот так плюс не иметь в кэше все подтянутые объекты
            # потому что если в сессии будут все релейшншипы, алхимия их покажет
            selectinload(User.posts.and_(post_filter)),
        )
        .order_by(User.id)
    )
    return list(session.scalars(statement).all())


def create_tags(
    session: SessionType,
) -> list[Tag]:
    tag_names = [
        ("python", "Posts about Python"),
        ("sqlalchemy", "ORM-related posts"),
        ("web", "Web development"),
        ("tutorial", "How-to and tutorials"),
        ("ops", "DevOps and deployment"),
        ("data", "Data-related topics"),
    ]

    tags = [Tag(name=name, description=description) for name, description in tag_names]
    session.add_all(tags)

    session.commit()
    print("created tags:", tags)
    return tags


def create_posts_with_tags(
    session: SessionType,
) -> list[Post]:
    tag_sets = [
        ["python", "sqlalchemy", "tutorial"],
        ["python", "web", "tutorial"],
        ["web", "ops", "data", "python"],
        ["sqlalchemy", "data", "python"],
        ["ops", "web", "tutorial"],
        ["data", "python", "sqlalchemy"],
        ["web", "tutorial", "ops"],
    ]

    all_tags = select_tags(session)
    tag_name_to_tag = {tag.name: tag for tag in all_tags}

    some_users = select_users_with_emails_not_end_with(session)
    user_ids = cycle(some_users)
    posts = []
    for tag_set in tag_sets:
        tags_text = " | ".join(tag_set)
        user_id = next(user_ids)
        post = Post(
            title=f"Post by user #{user_id} ({tags_text})",
            user_id=user_id,
        )
        for tag_name in tag_set:
            post.tags.append(tag_name_to_tag[tag_name])

        posts.append(post)

    session.add_all(posts)
    session.commit()

    print("created posts:", posts)
    return posts


def get_posts_with_tags(session: SessionType) -> list[Post]:
    statement = (
        select(Post)
        .options(
            selectinload(Post.tags),
            # subqueryload(Post.tags),
        )
        .order_by(Post.id)
    )
    return list(session.scalars(statement).all())


def get_users_with_posts_matching_tag(
    session: SessionType,
    tag_name: str,
) -> list[User]:
    tag_filter = Tag.name == tag_name
    statement = (
        select(User)
        .join(User.posts)
        .join(Post.tags)
        .where(tag_filter)
        .options(
            selectinload(
                User.posts.and_(
                    Post.tags.and_(tag_filter),
                ),
            ).selectinload(Post.tags),
        )
        .order_by(User.id)
    )
    return list(session.scalars(statement).unique().all())


def main() -> None:
    # create_users()
    # create_posts_for_users_with_emails()

    with Session() as session:
        # create_tags(session)
        # create_posts_with_tags(session)

        # posts = get_posts_with_tags(session)
        # for post in posts:
        #     print("-", post)
        #     if not post.tags:
        #         print(" ***no tags")
        #         continue
        #     for tag in post.tags:
        #         print(" *", tag)

        users = get_users_with_posts_matching_tag(session, "python")
        for user in users:
            print("•", user)
            for post in user.posts:
                print(" -", post)
                for tag in post.tags:
                    print("  **", tag)


if __name__ == "__main__":
    main()
