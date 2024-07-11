from collections.abc import Sequence

from sqlalchemy import desc
from sqlalchemy import distinct
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.orm import aliased
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import selectinload

from models import (
    engine,
    Base,
    User,
    Post,
    Tag,
)


def create_tables():
    # Base.metadata.drop_all(bind=engine)
    print("Creating tables...", Base.metadata.tables)
    Base.metadata.create_all(bind=engine)


def create_user(
    session: Session,
    username: str,
    email: str | None = None,
) -> User:
    user = User(username=username, email=email)
    session.add(user)

    session.commit()

    print("user created:", user)
    return user


def create_post(
    session: Session,
    title: str,
    user_id: int,
) -> Post:
    post = Post(title=title, user_id=user_id)
    # post.author = user
    session.add(post)
    session.commit()
    print("post created:", post)
    return post


def create_users(
    session: Session,
    *usernames: str,
) -> Sequence[User]:
    users = [
        User(username=username)
        for username in usernames
    ]
    session.add_all(users)
    print("prepared users:", users)

    session.commit()

    print("saved users:", users)
    return users


def create_posts(
    session: Session,
    *titles: str,
    user_id: int,
) -> Sequence[Post]:
    posts = [
        Post(title=title, user_id=user_id)
        for title in titles
    ]
    session.add_all(posts)
    print("prepared posts:", posts)
    session.commit()
    print("saved posts:", posts)
    return posts


def create_tags(
    session: Session,
    *names: str,
) -> Sequence[Tag]:
    tags = [
        Tag(name=name)
        for name in names
    ]
    session.add_all(tags)
    print("prepared tags:", tags)
    session.commit()
    print("saved tags:", tags)
    return tags


def fetch_all_users(session: Session) -> Sequence[User]:
    # stmt = select(User).order_by(User.id)
    stmt = select(User).order_by(desc(User.username))
    # result = session.execute(stmt)
    # users = result.scalars().all()
    users = session.scalars(stmt).all()
    print("users:", users)
    return users


def fetch_users_with_posts(
    session: Session,
) -> Sequence[User]:
    stmt = (
        select(User)
        .options(
            # joinedload(User.posts),
            selectinload(User.posts),
        )
        .order_by(User.id)
    )

    print("load users w/ posts:")
    # users = session.scalars(stmt).unique().all()
    users = session.scalars(stmt).all()
    for user in users:
        print("+", user)
        for post in user.posts:
            print("  -", post)

    return users


def fetch_all_posts(session: Session) -> Sequence[Post]:
    stmt = select(Post).order_by(Post.id)
    # result = session.execute(stmt)
    # posts = result.scalars().all()
    posts = session.scalars(stmt).all()
    print("posts:", posts)
    return posts


def fetch_all_tags(session: Session) -> Sequence[Tag]:
    stmt = select(Tag).order_by(Tag.id)
    tags = session.scalars(stmt).all()
    print("tags:", tags)
    return tags


def fetch_all_tags_with_posts(session: Session) -> Sequence[Tag]:
    stmt = (
        select(Tag)
        .options(
            selectinload(Tag.posts),
        )
        .order_by(Tag.id)
    )
    tags = session.scalars(stmt).all()
    return tags


def fetch_all_posts_with_authors(
    session: Session,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .options(
            joinedload(Post.author),
        )
        .order_by(Post.id)
    )
    posts = session.scalars(stmt).all()
    print("posts:", posts)

    for post in posts:
        print("+", post)
        print("= author:", post.author)

    return posts


def fetch_all_posts_with_tags(
    session: Session,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .options(
            selectinload(Post.tags),
        )
        .order_by(Post.id)
    )
    posts = session.scalars(stmt).all()
    return posts


def fetch_all_posts_with_tags_where_tag_is_present(
    session: Session,
    tag_name: str,
) -> Sequence[Post]:
    stmt = (
        select(Post)
        .join(Post.tags)
        .where(func.lower(Tag.name) == tag_name.lower())
        .options(
            selectinload(Post.tags),
        )
        .order_by(Post.id)
    )
    posts = session.scalars(stmt).all()
    return posts


def fetch_user_by_username(session: Session, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    # result = session.execute(stmt)
    # user = result.scalars().one_or_none()
    user: User | None = session.scalars(stmt).one_or_none()
    print("user for username", repr(username), "result:", user)
    return user


SQL = """
UPDATE users 
SET email=concat(
    lower(users.username), 
    '@ya.ru'::VARCHAR
)
WHERE users.email IS NULL 
    AND length(users.username) < 5::INTEGER;
"""


def set_emails_for_null_email_users_with_username_limit(
    session: Session,
    username_size_limit: int,
    domain: str,
):
    """

    :param session:
    :param username_size_limit:
    :param domain: example: '@ya.ru'
    :return:
    """

    new_email = (
        func.concat(
            func.lower(User.username),
            domain.lower(),
        )
    )
    stmt = (
        update(User)
        .where(
            # empty email
            User.email.is_(None),
            # username len limit
            func.length(User.username) < username_size_limit,
        )
        .values(
            {
                User.email: new_email,
            }
        )
    )

    session.execute(stmt)
    session.commit()


"""
SQL:
SELECT ('a', 'b');

python:
result all: [('a', 'b'),]
result first: ('a', 'b')

SQL:
SELECT (42);

python 
result all: [(42, ),]
result first: (42, )

result all: [(42, ), (7, ), ]

python scalars
result scalars all: [42, 7,]
result scalar first: 42


SELECT ( {tag.id, tag.name} )

python
result all: [ (Tag(id=1, name='...'), ), (Tag(id=2, name='...'), ), ]
result scalars all: [ Tag(id=1, name='...'), Tag(id=2, name='...'), ]
result first: ( Tag(id=1, name='...'), )
result scalar first: Tag(id=1, name='...')


SELECT ( {user.id, user.username}, count )
group by ...

python
result all [ (User(...), count, ), (User(...), count, ) ]
result first (User(...), count, )
"""


def select_top_users_with_posts_sorted(
    session: Session,
) -> None:
    users_w_posts_count_stmt = (
        select(User, func.count(Post.id).label('posts_count'))
        .join(User.posts, isouter=True)
        .group_by(User.id)
        .order_by(func.count(Post.id).desc(), User.username)
    )
    result = session.execute(users_w_posts_count_stmt).all()
    for user, posts_count in result:
        print("+ user", user.id, user.username, "w/", posts_count, "posts")


def create_tags_based_on_posts_titles(
    session: Session,
) -> Sequence[Tag]:
    posts = fetch_all_posts(session)
    known_tags = fetch_all_tags(session)
    known_tags_names: set[str] = {tag.name.lower() for tag in known_tags}

    new_tags_names: set[str] = set()
    for post in posts:
        parts = post.title.lower().strip().split()
        new_tags_names.update(parts)

    new_tags_names.difference_update(known_tags_names)
    tags = create_tags(session, *new_tags_names)
    return tags


def auto_associate_tags_with_posts(session: Session) -> None:
    posts = fetch_all_posts_with_tags(session)
    tags = fetch_all_tags(session)

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
            func.lower(Tag.name) == tag_name.lower()
        )
        .order_by(User.id)
    )
    users = session.scalars(stmt).unique().all()
    print("users who used tag", repr(tag_name), "in posts:")
    for user in users:
        print("+", user)

    return users


def get_users_with_posts_with_tag_using_subquery(
    session: Session,
    tag_name: str,
) -> Sequence[User]:

    stmt_users_ids_for_posts_with_tag = (
        select(distinct(Post.user_id))
        .join(Post.tags)
        .where(
            func.lower(Tag.name) == tag_name.lower()
        )
    )
    # print(session.execute(stmt_users_ids_for_posts_with_tag).all())
    stmt = (
        select(User)
        .where(
            User.id.in_(
                stmt_users_ids_for_posts_with_tag.subquery(),
            )
        )
        .order_by(User.id)
    )
    users = session.scalars(stmt).all()
    print("users who used tag", repr(tag_name), "in posts:")
    for user in users:
        print("+", user)

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
            func.lower(table_tags1.name) == t1_name.lower(),
            func.lower(table_tags2.name) == t2_name.lower(),
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


def main():
    # create_tables()
    with Session(engine) as session:
        # create_user(session, username="admin", email="admin@admin.com")
        # bob = create_user(session, username="bob", email=None)
        # john = create_user(session, username="john", email=None)
        # post_pg = create_post(
        #     session=session,
        #     title="PostgreSQL news",
        #     user_id=john.id,
        # )
        # print("post pg:", post_pg)
        # create_users(session, "nick", "alice")
        # sam = create_user(session, username="sam", email=None)
        # create_posts(
        #     session,
        #     "MySQL Intro",
        #     "MariaDB SQL Lesson",
        #     user_id=sam.id,
        # )
        #
        # create_posts(
        #     session,
        #     "Python Intro",
        #     "Python Lesson",
        #     "Python decorators",
        #     user_id=bob.id,
        # )
        #
        #
        # create_users(session, "pete", "jenn", "marco")
        # create_users(session, "kyle", "james", "kate")
        #
        # fetch_all_users(session)
        # fetch_users_with_posts(session)

        # create_tags_based_on_posts_titles(session)
        # auto_associate_tags_with_posts(session)
        # posts = fetch_all_posts_with_tags(session)
        # posts = fetch_all_posts_with_tags_where_tag_is_present(session, tag_name="sql")
        #
        # for post in posts:
        #     print("+", post)
        #     for t in post.tags:
        #         print(" *", t.name)

        # tags_with_posts = fetch_all_tags_with_posts(session)
        # for tag in tags_with_posts:
        #     print("+", tag)
        #     for post in tag.posts:
        #         print(" | ", post.id, post.title)

        # get_users_with_posts_with_tag(session, "sql")
        # get_users_with_posts_with_tag_using_subquery(session, "sql")
        # posts = show_posts_with_one_of_tags(session, "sql", "Python")
        # posts = show_posts_with_two_tags(session, "lesson", "Python")
        posts = show_posts_with_all_tags(session, "postgres", "sql", "news")
        for post in posts:
            print("+", post)
            for t in post.tags:
                print(" *", t.name)

        # create_tags(session, "news", "postgres", "python", "sql", "lesson")

        # posts = fetch_all_posts(session)
        # fetch_all_posts_with_authors(session)
        #
        # for post in posts:
        #     print("+", post)
        #     print("= author:", post.author)


if __name__ == "__main__":
    main()
