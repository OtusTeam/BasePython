import logging
from typing import Optional, List

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session as SessionType, joinedload, selectinload

from models import User, Author, Post, Tag
from models.base import Base, Session

log = logging.getLogger(__name__)


def create_user(session: SessionType, username: str) -> User:
    user = User(username=username)

    print("create user", user)

    session.add(user)
    session.commit()

    print("created user", user)

    return user


def find_user_by_username(session: SessionType, username: str) -> Optional[User]:
    user = session.query(User).filter_by(username=username).one_or_none()
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


def create_tags(session: SessionType, *tags_names: str):
    tags = []
    for tag_name in tags_names:
        tag = Tag(name=tag_name)
        session.add(tag)
        tags.append(tag)

    session.commit()

    print("created tags", tags)


def fetch_all_tags(session: SessionType) -> list[Tag]:
    tags = session.query(Tag).all()
    print("tags:", tags)
    return tags


def assign_tags_to_posts(session: SessionType):
    tags = fetch_all_tags(session)
    # TODO: join tags
    posts: list[Post] = session.query(Post).all()

    tag_python = next(filter(lambda t: t.name == "python", tags), None)

    for post in posts:
        for tag in tags:
            if tag.name in post.title.lower():
                post.tags.append(tag)
        if tag_python and tag_python not in post.tags:
            post.tags.append(tag_python)

    session.commit()


def fetch_posts_with_tags(session: SessionType) -> list[Post]:
    posts: list[Post] = (
        session.query(Post)
        .options(joinedload(Post.tags))
    )
    for post in posts:
        print("post", post.id, post.title)
        print("-- tags", post.tags)

    return posts


def fetch_posts_with_tags2(session: SessionType) -> list[Post]:
    posts: list[Post] = (
        session.query(Post)
        .options(selectinload(Post.tags))
    )
    for post in posts:
        print("post", post.id, post.title)
        print("-- tags", post.tags)

    return posts


def fetch_tags_with_posts(session: SessionType) -> list[Tag]:
    tags: list[Tag] = session.query(Tag).options(joinedload(Tag.posts)).all()

    for tag in tags:
        print("tag", tag)
        print("-- tag posts")
        for post in tag.posts:
            print("... ", post.id, post.title)

    return tags


def assign_and_delete_tag(session: SessionType, tag_name: str):

    tag: Tag = session.query(Tag).filter_by(name=tag_name).one_or_none()
    if not tag:
        tag = Tag(name=tag_name)
        # session.add(tag)
        # session.commit()
        # session.refresh(tag)

    post: Post = session.query(Post).options(joinedload(Post.tags)).first()
    if not post:
        raise ValueError("post not found")

    print("post to update")
    print("post", post.id, post.title)
    print("post tags:", post.tags)

    post.tags.append(tag)

    session.commit()
    print("added tag to post, now it's")
    print("post", post.id, post.title)
    print("post tags:", post.tags)

    print("remove tag")
    post.tags.remove(tag)
    session.commit()

    print("post", post.id, post.title)
    print("post tags:", post.tags)


def find_user_by_author_post_tag(session: SessionType, tag_name: str) -> list[User]:
    users: list[User] = (
        session
        .query(User)
        .join(User.author)
        .join(Author.posts)
        .join(Post.tags)
        .filter(Tag.name == tag_name)
        .options(
            joinedload(User.author)
            .joinedload(Author.posts)
            .joinedload(Post.tags)
        )
        .all()
    )

    for user in users:
        print("user", user)
        print("author", user.author)
        print("author posts:")
        for post in user.author.posts:
            print("- ", post.id, post.title)
            print("-  tags", post.tags)

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
    # # posts = create_posts_for_author(session, author, ["Django Intro", "Flask Lesson"])
    #
    # try:
    #     find_user_with_author_and_posts(session, "jack")
    # except NoResultFound:
    #     log.info("no user jack")
    # find_user_with_author_and_posts(session, "john")
    # find_user_with_author_and_posts(session, "sam")

    # find_matching_username(session, "joh")
    # find_matching_username(session, "johna")
    # find_matching_username(session, "a")

    # user_john = find_user_by_username(session, "john")
    # author_john = create_author_for_user(session, user_john, "John S.")
    # user_john = fetch_user_with_author_by_username(session, "john")
    # create_posts_for_author(session, user_john.author, ["Django Lesson", "SQLAlchemy Lesson", "Python News"])

    # posts = create_posts_for_author()
    # for post in posts:
    #     post.title


    # TAGS!!

    # create_tags(session, "python", "news", "django", "flask", "sqlalchemy")
    # fetch_all_tags(session)
    # assign_tags_to_posts(session)
    # fetch_posts_with_tags(session)
    # fetch_posts_with_tags2(session)
    # fetch_tags_with_posts(session)

    # assign_and_delete_tag(session, "qwerty")
    assign_and_delete_tag(session, "foobar")
    # find_user_by_author_post_tag(session, "django")
    # find_user_by_author_post_tag(session, "news")

    session.close()


if __name__ == "__main__":
    main()
