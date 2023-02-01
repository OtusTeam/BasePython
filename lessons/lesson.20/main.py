from models import Base, Session, User, Author, Post

from sqlalchemy import or_, and_
from sqlalchemy.orm import Session as SessionType, joinedload


def create_user(session: SessionType, username: str, is_staff=False) -> User:
    user = User(username=username, is_staff=is_staff)
    session.add(user)
    session.commit()
    return user


def create_author(session: SessionType, user: User, name: str) -> Author:
    author = Author(name=name, user=user)
    session.add(author)
    session.commit()
    return author


def get_all_users(session: SessionType) -> list[User]:
    users = session.query(User).all()
    return users


def show_users(session: SessionType):
    users = get_all_users(session)
    for user in users:
        print(user)


def show_users_with_authors(session: SessionType):
    users = session.query(User).options(joinedload(User.author)).all()
    for user in users:
        print(user, user.author)


def show_authors_with_users(session: SessionType):
    authors = session.query(Author).options(joinedload(Author.user)).all()
    for author in authors:
        print(author, author.user)


def find_author_by_user_username(session: SessionType, username: str) -> Author:
    author = (
        session.query(Author)
        .join(
            Author.user,
            # User,
            # Author.user_id == User.id,
        )
        .filter(
            User.username == username,
        )
        .options(
            joinedload(Author.user),
            # ).one_or_none()
        )
        .one()
    )
    return author


def create_posts(session: SessionType, author: Author, *titles: str) -> list[Post]:
    posts = [Post(author=author, title=title) for title in titles]
    session.add_all(posts)
    session.commit()
    return posts


def get_posts_with_authors_and_users(session: SessionType):
    posts = (
        session.query(Post)
        .options(
            joinedload(Post.author).joinedload(Author.user),
        )
        .all()
    )
    for post in posts:
        print("-----")
        print(post)
        print("*", post.author)
        print("+++", post.author.user)


def get_posts_with_authors_and_users_by_username(session: SessionType, username: str) -> list[Post]:
    posts = (
        session.query(Post)
        .join(Post.author)
        .join(Author.user)
        .filter(
            User.username == username,
        )
        .options(
            joinedload(Post.author).joinedload(Author.user),
        )
        .all()
    )
    for post in posts:
        print("-----")
        print(post)
        print("*", post.author)
        print("+++", post.author.user)


def get_posts_filtered(session: SessionType, post_name_contains: str, username: str) -> list[Post]:
    posts = (
        session.query(Post)
        .join(Post.author)
        .join(Author.user)
        .filter(
            or_(
                Post.title.ilike(f"%{post_name_contains}%"),
                and_(
                    User.is_staff.is_(False),
                    User.username == username,
                )
            ),
        )
        .options(
            joinedload(Post.author).joinedload(Author.user),
        )
        .all()
    )
    for post in posts:
        print("-----")
        print(post)
        print("*", post.author)
        print("+++", post.author.user)


def main():
    session: SessionType = Session()
    john = create_user(session, "john")
    author = create_author(session, john, "John Smith")
    print(john)
    print(author)

    sam = create_user(session, "sam")
    nick = create_user(session, "nick")
    bob = create_user(session, "bob")
    author_bob = create_author(session, bob, "Bob Black")
    show_users(session)
    show_users_with_authors(session)
    show_authors_with_users(session)
    author_bob = find_author_by_user_username(session, "bob")
    author_john = find_author_by_user_username(session, "john")

    create_posts(session, author_john, "L1", "L2")
    create_posts(session, author_bob, "Lesson SQL", "Lesson PG")
    get_posts_with_authors_and_users(session)
    get_posts_with_authors_and_users_by_username(session, "bob")
    get_posts_filtered(session, "l", "bob")
    session.close()


if __name__ == "__main__":
    # Base.metadata.drop_all()
    # Base.metadata.create_all()
    # print(Base.metadata.tables)
    main()
