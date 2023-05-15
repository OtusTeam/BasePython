from datetime import datetime
from typing import Iterable

from sqlalchemy import (
    create_engine,
    func,
    or_,
)

from sqlalchemy.orm import (
    aliased,
    Session,
    joinedload,
    selectinload,
)

from models import User, Author, Post, Tag

import config

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
)


def create_user(session: Session, username: str) -> User:
    user = User(username=username)
    print("user", user)
    session.add(user)
    session.commit()
    print("saved user", user)
    return user


# def create_author(session: Session, name: str, user_id: int) -> Author:
def create_author(session: Session, name: str, user: User) -> Author:
    author = Author(
        name=name,
        user_id=user.id,
        # user=user,
    )
    session.add(author)
    session.commit()
    print("created author", author)

    return author


def show_users_with_authors(session: Session):
    # N+1 Problem
    users = (
        # get all users
        session.query(User)
        # extra options
        .options(
            # join all "to-one" relations (User -> Author)
            joinedload(User.author)
        )
        # get all
        .all()
    )

    for user in users:
        print(user, user.author)


def show_users_only_with_authors(session: Session):
    # N+1 Problem
    users = (
        # get all users
        session.query(User)
        # for filtering
        # .join(User.author)
        # extra options
        .options(
            # join all "to-one" relations (User -> Author)
            joinedload(User.author, innerjoin=True)
        )
        # add "where" to SQL
        # .filter(
        #     Author.user_id.isnot(None),
        # )
        # get all
        .all()
    )

    for user in users:
        print(user, user.author)


def show_authors_with_users(session: Session):
    authors = (
        # get all authors
        session.query(Author)
        # extra
        .options(
            # join "to-one" users
            joinedload(Author.user)
        )
        # get all objects
        .all()
    )

    for author in authors:
        print(author, author.user)


def update_users_emails_by_username(session: Session, domain: str, *filters):
    # result = (
    #     session.query(
    #         User.id,
    #         User.username,
    #         func.length(User.username),
    #         func.length(User.username) == 4,
    #     )
    #     .filter(
    #         func.length(User.username) == 4,
    #     )
    #     .all()
    # )
    # for row in result:
    #     print(row)
    query = session.query(User).filter(*filters)
    query.update(
        {
            User.email: User.username + domain,
            # "email": "",
        },
        synchronize_session=False,
    )
    session.commit()


def find_authors_by_user_email_domain(session: Session, email_domain: str):
    authors = (
        # get author objects
        session.query(Author)
        # join users
        .join(Author.user).filter(User.email.endswith(email_domain))
        # .join(
        #     User,
        #     Author.user_id == User.id,
        # )
        .options(joinedload(Author.user))
        # all of them
        .all()
    )
    for author in authors:
        print(author, author.user)


def find_author_by_user_username(session: Session, username: str):
    return (
        session.query(Author)
        # явное присоединение
        # explicit join
        .join(Author.user)
        # find by username
        .filter(User.username == username)
        # or error
        .one()
    )


def create_posts(
    session: Session,
    author: Author,
    *titles: str,
) -> list[Post]:
    posts = [
        Post(
            title=title,
            author_id=author.id,
        )
        for title in titles
    ]
    session.add_all(posts)
    session.commit()
    print("posts:", posts)
    return posts


def show_users_with_author_and_posts(session: Session):
    users = (
        # get users
        session.query(User)
        # join all related objects
        # .options(joinedload(User.author).joinedload(Author.posts))
        # joinedload - "to one"
        # selectinload - "to many"
        .options(joinedload(User.author).selectinload(Author.posts))
        # sort
        .order_by(User.id)
        # get all of them
        .all()
    )

    for user in users:
        print("- user", user)
        if not user.author:
            continue
        print("++ author", user.author)
        print("=== posts:")
        for post in user.author.posts:
            print("=", post)


def show_authors_with_users_and_posts(session: Session):
    authors = (
        # all authors
        session.query(Author)
        # join related objects
        .options(
            # "to one"
            joinedload(Author.user),
            # "to many"
            selectinload(Author.posts),
        )
        # sort
        .order_by(Author.id)
        # fetch all
        .all()
    )

    for author in authors:
        print("+", author)
        print("++", author.user)

        print("=== posts:")
        for post in author.posts:
            print("=", post)


def create_tags(session: Session, *names: str) -> list[Tag]:
    tags = [
        Tag(name=name)
        for name in names
    ]
    session.add_all(tags)
    session.commit()
    print(tags)

    return tags


def find_tags(session: Session, *names: str) -> list[Tag]:
    tags = session.query(Tag).filter(
        func.lower(Tag.name).in_(names)
    ).all()
    print("found tags", tags)

    return tags


def create_post_with_tags(
    session: Session,
    author: Author,
    title: str,
    tags: Iterable[Tag],
) -> Post:
    post = Post(
        title=title,
        # author=author
        author_id=author.id,
        tags=tags,
    )
    session.add(post)
    session.commit()

    print(post)
    print(post.tags)

    return post


def auto_associate_tags_with_posts(session: Session):
    tags: Iterable[Tag] = session.query(Tag).all()
    posts: Iterable[Post] = session.query(Post).options(
        selectinload(Post.tags)
    ).all()

    for post in posts:
        title = post.title.lower()
        for tag in tags:
            if tag.name.lower() in title and tag not in post.tags:
                post.tags.append(tag)

    session.commit()


def find_posts_for_any_of_tags(session: Session, *tags_names: str) -> Iterable[Post]:
    posts: Iterable[Post] = (
        session.query(Post)
        .join(Post.tags)
        .filter(
            func.lower(Tag.name).in_(tags_names),
        )
        .options(
            joinedload(Post.author),
            selectinload(Post.tags),
        )
        .order_by(Post.title)
    )

    for post in posts:
        print("---")
        print("post", post)
        print("author:", post.author)
        print("tags:", post.tags)

    return posts


def find_posts_for_two_tags(session: Session, tag1: str, tag2: str) -> Iterable[Post]:
    table_tags1 = aliased(Tag, name="table_tags1")
    table_tags2 = aliased(Tag, name="table_tags2")
    # table_tags3 = aliased(Tag, name="table_tags2")
    posts = (
        session.query(Post)
        .join(table_tags1, Post.tags)
        .join(table_tags2, Post.tags)
        # .join(table_tags3, Post.tags)
        .filter(
            func.lower(table_tags1.name) == tag1,
            func.lower(table_tags2.name) == tag2,
            # func.lower(table_tags3.name) == tag3,
        )
        .options(selectinload(Post.tags))
        .order_by(Post.id)
        .all()
    )

    print("posts for both tags", tag1, tag2)

    for post in posts:
        print("---")
        print("post", post)
        print("tags:", post.tags)

    return posts


def find_posts_for_all_of_tags(session: Session, *tags: str) -> Iterable[Post]:
    posts_q = session.query(Post)

    tags_names = list(set(map(str.lower, tags)))
    filters = []

    for tag_name in tags_names:
        table = aliased(Tag, name=f"table_tags_{tag_name}")
        posts_q = posts_q.join(table, Post.tags)
        filters.append(
            func.lower(table.name) == tag_name,
        )

    posts = (
        posts_q
        .filter(*filters)
        .options(selectinload(Post.tags))
        .order_by(Post.id)
        .all()
    )

    print("posts for tags", tags)

    for post in posts:
        print("---")
        print("post", post)
        print("tags:", post.tags)

    return posts


def find_posts_between_dates(session: Session, after_dt: datetime, before_dt: datetime) -> Iterable[Post]:
    posts = session.query(Post).filter(
        Post.created_at >= after_dt,
        Post.created_at <= before_dt,
    ).order_by(Post.created_at).all()

    for post in posts:
        print(post.title, post.created_at)

    return posts


def find_posts_by_title(session: Session, *texts: str) -> Iterable[Post]:
    posts = (
        session.query(Post)
        .filter(
            or_(
                *(
                    func.lower(Post.title).contains(text.lower())
                    for text in texts
                )
            )
        )
        .order_by(Post.id)
        .all()
    )

    print(posts)

    return posts


# def find_tags(session: Session, *tag_names: str) -> Iterable[Tag]:
#     return session.query(Tag).filter(func.lower(Tag.name).in_(tag_names))


def add_tags_to_posts(session: Session, posts: Iterable[Post], tags: Iterable[Tag]):
    for post in posts:
        for tag in tags:
            if tag not in post.tags:
                post.tags.append(tag)

    session.commit()


def main():
    with Session(engine) as session:
        john = create_user(session, username="john")
        sam = create_user(session, username="sam")
        author_john = create_author(session, "John Smith", user=john)
        author_sam = create_author(session, "Sam White", user=sam)
        kate = create_user(session, username="kate")
        alice = create_user(session, username="alice")
        show_users_with_authors(session)
        show_authors_with_users(session)
        show_users_only_with_authors(session)
        update_users_emails_by_username(session, "@google.com")
        update_users_emails_by_username(
            session,
            "@yahoo.com",
            (func.length(User.username) == 4),
        )
        find_authors_by_user_email_domain(session, "@yahoo.com")
        author_john = find_author_by_user_username(session, "john")
        create_posts(session, author_john, "PyCharm News", "Python Tutorial")
        author_sam = find_author_by_user_username(session, "sam")
        create_posts(session, author_sam, "Postgres news", "MySQL Tutorial")
        show_users_with_author_and_posts(session)
        show_authors_with_users_and_posts(session)
        create_tags(session, "Python", "news", "lesson", "PyCharm")
        create_tags(session, "MySQL", "tutorial")
        create_tags(session, "database")
        posts = find_posts_by_title(session, "mysql", "postgres")
        tags = find_tags(session, "database")
        add_tags_to_posts(session, posts, tags)
        create_post_with_tags(session, author_john, "New Python Update", tags)
        auto_associate_tags_with_posts(session)
        find_posts_for_any_of_tags(session, "tutorial", "mysql", "database")
        find_posts_for_any_of_tags(session, "qwerty")
        find_posts_for_any_of_tags(session, "pycharm", "news")
        find_posts_for_two_tags(session, "pycharm", "news")
        find_posts_for_all_of_tags(session, "tutorial", "mysql", "database")
        find_posts_for_all_of_tags(session, "tutorial")
        find_posts_for_all_of_tags(session, "database")
        find_posts_between_dates(
            session,
            after_dt=datetime(2023, 5, 15, 17, 10),
            before_dt=datetime(2023, 5, 15, 17, 20),
        )


if __name__ == "__main__":
    main()
