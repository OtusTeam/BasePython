from sqlalchemy import (
    create_engine,
    func,
)

from sqlalchemy.orm import (
    Session,
    joinedload,
    selectinload,
)

from models import User, Author, Post

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


if __name__ == "__main__":
    main()
