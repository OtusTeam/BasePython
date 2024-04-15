from typing import Sequence

from sqlalchemy import (
    select,
    update,
    func,
    distinct,
)
from sqlalchemy import text
from sqlalchemy.orm import (
    Session,
    joinedload,
    selectinload,
    aliased,
)

from models import (
    User,
    Post,
    Tag,
)
from models.db import engine


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


def fetch_all_posts(
    session: Session,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .order_by(Post.id)
    )
    posts = session.scalars(stmt)
    return posts.all()


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


def create_tags(
    session: Session,
    *tags_names: str,
) -> list[Tag]:
    tags = [
        Tag(name=tag_name)
        for tag_name in tags_names
    ]
    session.add_all(tags)
    session.commit()
    print(tags)
    return tags


def create_tags_for_posts_names(
    session: Session,
) -> Sequence[Tag]:
    posts = fetch_all_posts(session)
    tags_names = []
    for post in posts:
        parts = post.title.lower().strip().split()
        tags_names.extend(parts)

    tags = [
        Tag(name=name)
        for name in set(tags_names)
        if name
    ]
    session.add_all(tags)
    session.commit()
    print(tags)
    return tags


def fetch_all_tags_with_posts(
    session: Session,
) -> Sequence[Tag]:
    stmt = (
        select(Tag)
        .options(selectinload(Tag.posts))
        .order_by(Tag.id)
    )
    tags = session.scalars(stmt)
    return tags.all()


def fetch_all_posts_with_tags(
    session: Session,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .options(selectinload(Post.tags))
        .order_by(Post.id)
    )
    posts = session.scalars(stmt)
    return posts.all()


def auto_associate_tags_with_posts(session: Session):
    tags = fetch_all_tags_with_posts(session)
    posts = fetch_all_posts_with_tags(session)
    for post in posts:
        post_title = post.title.lower()
        for tag in tags:
            if tag in post.tags:
                continue
            if tag.name.lower() in post_title:
                post.tags.append(tag)

    session.commit()


def get_users_with_posts_with_tag(
    session: Session,
    tag_name: str,
) -> Sequence[User]:
    stmt = (
        select(User)
        .join(User.posts)
        .join(Post.tags)
        .where(
            func.lower(Tag.name) == tag_name.lower(),
        )
        .order_by(User.id)
    )
    result = session.scalars(stmt)
    users = result.unique().all()
    print("users who used tag", repr(tag_name), "in posts:")
    for user in users:
        print(user)

    return users


def get_users_with_posts_with_tag_using_subquery(
    session: Session,
    tag_name: str,
) -> Sequence[User]:
    stmt_user_id_from_posts_with_tag = (
        # select(Post.user_id)
        select(distinct(Post.user_id))
        .join(Post.tags)
        .where(
            func.lower(Tag.name) == tag_name.lower(),
        )
    )

    stmt = (
        select(User)
        .where(
            User.id.in_(
                stmt_user_id_from_posts_with_tag.subquery(),
            ),
        )
        .order_by(User.id)
    )
    result = session.scalars(stmt)
    users = result.all()
    print("users who used tag", repr(tag_name), "in posts:")
    for user in users:
        print(user)

    return users


def show_posts_with_one_of_tags(
    session: Session,
    *tags_names: str,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .join(Post.tags)
        .where(
            func.lower(Tag.name).in_([name.lower() for name in tags_names])
        )
        .options(
            selectinload(Post.tags)
        )
        .order_by(Post.id)
    )
    posts = session.scalars(stmt)
    return posts.unique().all()


def show_posts_with_two_tags(
    session: Session,
    t1_name: str,
    t2_name: str,
) -> Sequence[Post]:
    table_tags1 = aliased(Tag, name="table_tags1")
    table_tags2 = aliased(Tag, name="table_tags2")
    stmt = (
        select(Post)
        .join(
            table_tags1,
            Post.tags,
        )
        .join(
            table_tags2,
            Post.tags,
        )
        .where(
            func.lower(table_tags1.name) == t1_name,
            func.lower(table_tags2.name) == t2_name,
        )
        .options(
            selectinload(Post.tags)
        )
        .order_by(Post.id)
    )
    posts = session.scalars(stmt)
    return posts.unique().all()


def show_posts_with_all_tags(
    session: Session,
    *tags_names: str,
) -> Sequence[Post]:
    stmt = select(Post)
    tags_names = list(set(map(str.lower, tags_names)))
    filters = []
    for tag_name in tags_names:
        table_tags = aliased(Tag, name=f"table_tags_for_{tag_name}")
        stmt = stmt.join(
            table_tags,
            Post.tags,
        )
        filters.append(
            func.lower(table_tags.name) == tag_name
        )

    stmt = (
        stmt
        .where(
            *filters,
        )
        .options(
            selectinload(Post.tags)
        )
        .order_by(Post.id)
    )
    posts = session.scalars(stmt)
    return posts.unique().all()


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
    #     "Postgresql Lesson",
    #     user_id=user_sam.id,
    # )
    #
    # user_bob = create_user(session, "bob")
    # user_alice = create_user(session, "alice")
    #
    # create_posts(
    #     session,
    #     "SQL Transactions",
    #     "Transactions in MySQL",
    #     user_id=user_bob.id,
    # )
    #
    # create_tags(
    #     session,
    #     "news",
    #     "python",
    # )
    #
    # create_tags_for_posts_names(session)
    # auto_associate_tags_with_posts(session)

    # # 1
    # for user_id in (0, 1, 2, 10):
    #     posts = fetch_posts_for_user_id(session, user_id)
    #     if not posts:
    #         print("no posts for user id", user_id)
    #         continue
    #     print("++user id posts", user_id)
    #     for post in posts:
    #         print("-", post)
    # # 2
    # users_with_posts = fetch_users_with_posts(session)
    # for user in users_with_posts:
    #     print("++ posts for user", user)
    #     for post in user.posts:
    #         print("-", post)

    # # 3
    # authors_with_posts = fetch_authors_with_posts(session)
    # for user in authors_with_posts:
    #     print("++ posts for author", user)
    #     for post in user.posts:
    #         print("-", post)

    # # 4
    # posts_with_authors = fetch_posts_with_authors(session)
    # for post in posts_with_authors:
    #     print("post", (post.id, post.title), "author:", post.author)

    # posts_w_tags = fetch_all_posts_with_tags(session)
    # for post in posts_w_tags:
    #     print("P:", post)
    #     for tag in post.tags:
    #         print("-t", tag)
    #
    # tags_w_posts = fetch_all_tags_with_posts(session)
    # for tag in tags_w_posts:
    #     print("T:", tag)
    #     for post in tag.posts:
    #         print("-", post.id, post.title)

    # get_users_with_posts_with_tag(session, "sql")
    # get_users_with_posts_with_tag(session, "news")
    # get_users_with_posts_with_tag(session, "mysql")

    # get_users_with_posts_with_tag_using_subquery(session, "sql")
    # get_users_with_posts_with_tag_using_subquery(session, "news")
    # get_users_with_posts_with_tag_using_subquery(session, "mysql")

    # posts = show_posts_with_one_of_tags(
    #     session,
    #     "mysql",
    #     "sql",
    #     "news",
    # )
    posts = show_posts_with_all_tags(
        session,
        "mysql",
        "sql",
    )
    print("ready to show")
    for post in posts:
        print("P:", post)
        for tag in post.tags:
            print("-t", tag)

    posts = show_posts_with_all_tags(
        session,
        "mysql",
        "sql",
        "transactions",
    )
    print("ready to show")
    for post in posts:
        print("P:", post)
        for tag in post.tags:
            print("-t", tag)


def main():
    with Session(engine) as session:
        demo(session)


if __name__ == "__main__":
    main()
