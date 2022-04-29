import logging
from typing import Optional, List

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session as SessionType, joinedload

from models import User, Author, Post
from models.base import Base, Session

log = logging.getLogger(__name__)


def create_user(session: SessionType, username: str) -> User:

    user = User(username=username)

    print("create user", user)

    session.add(user)
    session.commit()

    print("created user", user)

    return user


def create_author_for_user(
    session: SessionType, user: User, author_name: str
) -> Author:

    author = Author(name=author_name, user=user)
    # author = Author(name=author_name, user_id=user.id)
    print("create author", author)

    session.add(author)
    session.commit()

    print("created author", author)

    return author


def fetch_author_by_id(session: SessionType, author_id: int) -> Author:
    author: Author = session.get(Author, author_id, options=(joinedload(Author.user),))

    print(author)
    print(author.user)

    return author


def fetch_user_with_author_by_username(session: SessionType, username: str) -> User:
    user: User = (
        session.query(User)
        .filter_by(username=username)
        .options(
            joinedload(User.author),
        )
        .one()
    )

    print(user)
    print(user.author)

    return user


def find_user_by_author_name(session: SessionType, author_name: str) -> Optional[User]:
    user = (
        session.query(User)
        .join(Author)
        # .join(Author, isouter=True)
        # .join(Author, isinner=True)
        # .join(Author, Author.user_id == User.id)
        .filter(Author.name == author_name)
        .options(joinedload(User.author))
        # .options(joinedload(User.author, innerjoin=True))
        .first()
    )

    print("found user", user)
    if user:
        print("user's author:", user.author)

    return user


def create_posts_for_author(
    session: SessionType, author: Author, titles: List[str]
) -> List[Post]:

    posts = []

    for title in titles:
        post = Post(
            title=title,
            author=author,
            # author_id=author.id,
        )
        print("create post", title, post)
        session.add(post)
        posts.append(post)

    session.commit()

    print("created posts")
    return posts


def find_user_with_author_and_posts(session: SessionType, username: str):

    user = (
        session.query(User)
        .filter(User.username == username)
        # .filter_by(username=username)
        .options(
            # joinedload(User.profile),
            # joinedload(User.author),
            joinedload(User.author).joinedload(Author.posts),
        )
        .one()
    )

    print(user)
    if user.author:
        print(user.author)
        for post in user.author.posts:
            print(post)


def find_matching_username(session: SessionType, username_part: str) -> List[User]:
    users: List[User] = (
        session
        .query(User)
        .filter(
            User.username.ilike(f"%{username_part}%")
        )
        .all()
    )
    print(users)
    return users


def main():
    session: SessionType = Session()

    # user_john = create_user(session, "john")
    # user_sam = create_user(session, "sam")
    # user_johnathan = create_user(session, "johnathan")
    # author_sam = create_author_for_user(session, user_sam, "Samuel")
    #
    # author = fetch_author_by_id(session, 1)
    #
    # fetch_user_with_author_by_username(session, "sam")
    # fetch_user_with_author_by_username(session, "john")
    # find_user_by_author_name(session, "John")
    # user_sam: User = find_user_by_author_name(session, "Samuel")
    #
    # posts = create_posts_for_author(session, author, ["Django Intro", "Flask Lesson"])
    # posts = create_posts_for_author(session, author, ["Django Intro", "Flask Lesson"])
    #
    # try:
    #     find_user_with_author_and_posts(session, "jack")
    # except NoResultFound:
    #     log.info("no user jack")
    # find_user_with_author_and_posts(session, "john")
    # find_user_with_author_and_posts(session, "sam")

    find_matching_username(session, "joh")
    find_matching_username(session, "johna")
    find_matching_username(session, "a")

    # posts = create_posts_for_author()
    # for post in posts:
    #     post.title

    session.close()


if __name__ == "__main__":
    main()
