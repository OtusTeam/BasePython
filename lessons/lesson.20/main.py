from models import Base, engine
from models import User, Post, Tag
# from models.tag import Tag
# from models.user import User

from sqlalchemy import select, text, literal, insert, func

from sqlalchemy.orm import Session, joinedload, selectinload, noload
from sqlalchemy.engine.cursor import CursorResult


def create_user(
    session: Session,
    username: str,
    email: str | None = None,
) -> User:
    user = User(username=username, email=email)

    session.add(user)
    session.commit()

    print(user)
    return user


def get_user_by_id(session: Session, user_id: int) -> User | None:
    user = session.get(User, user_id)
    print("user by id", user_id, "value:", user)
    return user


def create_post(session: Session, post_title: str, user: User) -> Post:
    post = Post(
        title=post_title,
        user_id=user.id,
        # user=user,
    )

    session.add(post)
    session.commit()

    print("created post", post)

    return post


def show_user_with_posts(session: Session, user_id: int) -> User | None:
    user: User | None = session.get(User, user_id)
    if user is None:
        print("user not found")
        return

    print()
    print("************* user", user.username)
    for post in user.posts:
        print("post", post.id, post.title)

    print()
    return user


def show_users_with_posts(
    session: Session,
    only_with_posts: bool = False,
) -> list[User]:
    query = (
        select(User)
        .options(
            joinedload(User.posts, innerjoin=only_with_posts)
        )
        .order_by(User.id)
    )
    print(query.compile())

    users: list[User] = (
        session
        .query(User)
        .options(
            joinedload(User.posts, innerjoin=only_with_posts)
        )
        .order_by(User.id)
        .all()
    )

    for user in users:

        print()
        print("************* user", user.username)
        for post in user.posts:
            print("post", post.id, post.title)

        print()

    return users


def show_posts_with_users(session: Session) -> list[Post]:
    posts = (
        session
        .query(Post)
        # .options(joinedload(Post.user, innerjoin=True))
        .options(joinedload(Post.user))
        .order_by(Post.id)
        .all()
    )

    for post in posts:
        print()
        print("*" * 10, post.id, post.title, post.user)
        print(post.body_len)

    return posts


def show_posts_with_title_len_no_more(
    session: Session,
    max_title_len: int,
) -> list[Post]:
    posts = (
        session
        .query(Post)
        .filter(
            func.length(Post.title) <= max_title_len,
        )
        .order_by(Post.id)
        .all()
    )

    for post in posts:
        print("post", post.id, len(post.title), post.title)

    return posts


def get_user_by_email_domain(session: Session, domain: str) -> list[User]:
    users = (
        session
        .query(User)
        .filter(User.email.ilike(f"%{domain}"))
        .order_by(User.id)
        .all()
    )
    print("users with email domain", domain, users)
    return users


def show_posts_with_users_on_domain(session: Session, domain: str) -> list[Post]:
    posts = (
        session
        .query(Post)
        .join(Post.user)
        # .join(
        #     User,
        #     Post.user_id == User.id,
        # )
        .filter(
            User.email.ilike(f"%@{domain}")
        )
        .options(joinedload(Post.user))
        .order_by(Post.id)
        .all()
    )

    for post in posts:
        print()
        print("*" * 10, post.id, post.title, post.user)

    return posts


def show_raw(session: Session):
    # sql_stmt = "SELECT * FROM users ORDER BY id;"
    sql_stmt = """
    SELECT users.id             AS users_id,
           users.username       AS users_username,
           users.email          AS users_email,
           users.is_staff       AS users_is_staff,
           users.created_at     AS users_created_at,
           posts_1.id           AS posts_1_id,
           posts_1.title        AS posts_1_title,
           posts_1.body         AS posts_1_body,
           posts_1.published_at AS posts_1_published_at,
           posts_1.user_id      AS posts_1_user_id
    FROM users
        JOIN posts AS posts_1 ON users.id = posts_1.user_id
    ORDER BY users.id;
    """
    result: CursorResult = session.execute(sql_stmt)
    for row in result.all():
        print(row.users_username, row.posts_1_title)

    stmt = select(literal("42").label("num"))
    result: CursorResult = session.execute(stmt)
    row = result.one()
    print(row)
    print(row.num)
    # row = result.scalar_one()
    # print(row)


def create_tags(session: Session, *tags_names: str) -> list[Tag]:
    tags = [
        Tag(name=tag_name)
        for tag_name in tags_names
    ]
    session.add_all(tags)
    session.commit()

    print("tags:", tags)
    return tags


def show_posts_with_tags(
    session: Session,
) -> None:
    query = (
        select(Post)
        .order_by(Post.id)
        # .options(noload(Post.tags))
        .options(selectinload(Post.tags))
    )
    print(query.compile())

    posts: list[Post] = (
        session
        .query(Post)
        .order_by(Post.id)
        # .options(noload(Post.tags))
        .options(selectinload(Post.tags))
        .all()
    )
    for post in posts:
        print(" --- post", post.id, post.title)
        print("post tags:", post.tags)


def auto_associate_tags_with_posts(
    session: Session,
    commit=True,
) -> None:
    posts: list[Post] = (
        session
        .query(Post)
        .order_by(Post.id)
        .options(selectinload(Post.tags))
        .all()
    )
    tags: list[Tag] = (
        session
        .query(Tag)
        .order_by(Tag.id)
        .all()
    )

    for post in posts:
        title = post.title.lower()
        for tag in tags:
            if tag.name.lower() in title and tag not in post.tags:
                post.tags.append(tag)

    if commit:
        session.commit()


def show_posts_with_any_of_tags(session: Session, *tags_names: str) -> list[Post]:
    posts: list[Post] = (
        session
        .query(Post)
        .join(Post.tags)
        .filter(
            func.lower(Tag.name).in_(tags_names),
        )
        .options(
            joinedload(Post.user),
            selectinload(Post.tags),
        )
        .order_by(Post.id)
        .all()
    )

    for post in posts:
        print("----")
        print("post", post.id, post.title)
        print("author:", post.user)
        print("tags:", post.tags)

    return posts


def show_users_using_tags(session: Session, *tags_names: str) -> list[User]:
    users: list[User] = (
        session
        .query(User)
        .join(User.posts)
        .join(Post.tags)
        .filter(
            func.lower(Tag.name).in_(tags_names),
        )
        .order_by(User.id)
        .all()
    )

    for user in users:
        print("----")
        print("author:", user)

    return users


def show_users_using_tags_with_posts_and_tags(
    session: Session,
    *tags_names: str,
) -> list[User]:
    users: list[User] = (
        session
        .query(User)
        .join(User.posts)
        .join(Post.tags)
        .filter(
            func.lower(Tag.name).in_(tags_names),
        )
        .options(
            joinedload(
                User.posts
            ).selectinload(
                Post.tags
            )
        )
        .order_by(User.id)
        .all()
    )

    for user in users:
        print("----")
        print("author:", user)
        print("--posts--")
        for post in user.posts:
            print("post", post.id, post.title)
            print("tags:", post.tags)

    return users


def run_queries():
    with Session(engine) as session:
        # show_raw(session)

        # user_john = create_user(session, username="john", email="john@example.com")
        # user_sam = create_user(session, username="sam", email="sam@yahoo.com")
        # user_nick = create_user(session, username="nick", email="nick@example.com")
        # user_kate = create_user(session, username="kate", email="kate@yahoo.com")
        #
        # create_post(session, "Post by John", user=user_john)
        # create_post(session, "SQL Lesson", user=user_john)
        #
        # create_post(session, "Post by Sam", user=user_sam)
        # create_post(session, "PyCharm lesson", user=user_sam)
        # create_post(session, "VS Code lesson", user=user_sam)
        #
        # create_post(session, "CSS lesson", user=user_kate)
        # create_post(session, "JS lesson", user=user_kate)

        # show_user_with_posts(session, user_john.id)
        # show_user_with_posts(session, user_sam.id)
        # show_users_with_posts(session)
        # show_users_with_posts(session, only_with_posts=True)
        # show_posts_with_users(session)
        # show_posts_with_title_len_no_more(session, 11)
        # show_posts_with_users_on_domain(session, "yahoo.com")
        # show_posts_with_users_on_domain(session, "example.com")

        # create_tags(session, "news", "python", "PyCharm", "VS Code", "JS")
        # create_tags(session, "SQL")

        # show_posts_with_tags(session)
        # auto_associate_tags_with_posts(session)

        # show_posts_with_any_of_tags(session, "python", "js")
        # show_users_using_tags(session, "python", "js")
        show_users_using_tags_with_posts_and_tags(session, "python", "js")


def main():
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    run_queries()


if __name__ == '__main__':
    main()
