from models import Session, User, Author, Post, Tag

from sqlalchemy import or_, and_, func
from sqlalchemy.orm import Session as SessionType, joinedload, selectinload, aliased


def create_user(session: SessionType, username: str, is_staff=False) -> User:
    user = User(username=username, is_staff=is_staff)
    session.add(user)
    session.commit()
    return user

def find_user(session: SessionType, username: str) -> User:
    user = session.query(User).filter_by(username=username).one_or_none()
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


def create_tags(session: SessionType, *tags_names: str) -> list[Tag]:
    tags = [
        Tag(name=name)
        for name in tags_names
    ]
    session.add_all(tags)
    session.commit()
    print("created tags", tags)
    return tags


def fetch_tags(session: SessionType) -> list[Tag]:
    tags = session.query(Tag).order_by(Tag.id).all()
    print("fetched tags", tags)
    return tags


def auto_assign_tags_to_posts(session: SessionType) -> None:
    posts = session.query(Post).options(selectinload(Post.tags)).all()
    tags = session.query(Tag).all()

    for post in posts:
        post_title = post.title.lower()
        for tag in tags:
            if tag.name.lower() in post_title and tag not in post.tags:
                post.tags.append(tag)

    session.commit()


def show_posts_with_tags(session: SessionType) -> list[Post]:
    posts = session.query(Post).options(selectinload(Post.tags)).order_by(Post.id).all()

    for post in posts:
        print("--", post)
        print(post.tags)

    return posts


def find_users_by_tag_name(session: SessionType, tag_name: str) -> list[User]:
    users = (
        session.query(User)
        .join(User.author)
        .join(Author.posts)
        .join(Post.tags)
        .filter(
            func.lower(Tag.name) == tag_name.lower(),
        )
    ).all()
    print("users for tag", tag_name, users)
    return users


def find_posts_by_tags_names(session: SessionType, *tags_names: str) -> list[Post]:
    posts = (
        session.query(Post)
        .join(Post.tags)
        # .join(Tag, Post.tags)
        .filter(
            func.lower(Tag.name).in_(tags_names),
            # Tag.name.in_(tags_names),
        )
        .options(
            joinedload(Post.author),
            joinedload(Post.tags),
        )
        .order_by(Tag.name)
    ).all()
    print("posts for tags", tags_names)
    for post in posts:
        print("---", post)
        print("- author", post.author)
        print("* tags", post.tags)
    return posts


def find_posts_by_two_tags(session: SessionType, tag1: str, tag2: str) -> list[Post]:

    table_tags_1 = aliased(Tag, name="table_tags_1")
    table_tags_2 = aliased(Tag, name="table_tags_2")

    posts = (
        session.query(Post)
        .join(table_tags_1, Post.tags)
        .join(table_tags_2, Post.tags)
        .filter(
            func.lower(table_tags_1.name) == tag1,
            func.lower(table_tags_2.name) == tag2,
        )
        .options(
            joinedload(Post.author),
            joinedload(Post.tags),
        )
        .all()
    )
    print("posts for all tags", tag1, tag1)
    for post in posts:
        print("---", post)
        print("- author", post.author)
        print("* tags", post.tags)
    return posts


def find_posts_by_all_tags(session: SessionType, *tags_names: str) -> list[Post]:
    posts_q = session.query(Post)
    tags_names = list(set(tags_names))
    filters = []
    for name in tags_names:
        tbl = aliased(Tag, name=f"table_tags_search_{name}")
        posts_q = posts_q.join(tbl, Post.tags)
        filters.append(func.lower(tbl.name) == name.lower())

    posts = (
        posts_q
        .filter(
            *filters,
        )
        .options(
            joinedload(Post.author),
            joinedload(Post.tags),
        )
        .all()
    )
    print("posts for all tags", tags_names)
    for post in posts:
        print("---", post)
        print("- author", post.author)
        print("* tags", post.tags)
    return posts


def main():
    session: SessionType = Session()
    john = create_user(session, "john")
    author = create_author(session, john, "John Smith")
    print(john)
    print(author)

    sam = create_user(session, "sam")
    nick = create_user(session, "nick")
    bob = create_user(session, "bob")

    sam = find_user(session, "sam")
    nick = find_user(session, "nick")
    author_sam = create_author(session, sam, "Sam Grey")
    author_nick = create_author(session, nick, "Nick Brown")
    author_bob = create_author(session, bob, "Bob Black")
    show_users(session)
    show_users_with_authors(session)
    show_authors_with_users(session)
    author_bob = find_author_by_user_username(session, "bob")
    author_john = find_author_by_user_username(session, "john")

    create_posts(session, author_john, "PyCharm News", "Python News")
    create_posts(session, author_john, "Golang Lesson")
    create_posts(session, author_bob, "Lesson SQL", "Lesson PG")
    create_posts(session, author_sam, "Python Django Lesson", "Python Flask Lesson")
    get_posts_with_authors_and_users(session)
    get_posts_with_authors_and_users_by_username(session, "bob")
    get_posts_filtered(session, "l", "bob")
    create_tags(session, "python", "pycharm", "sql", "pg", "news", "lesson")
    create_tags(session, "golang", "django", "flask")
    fetch_tags(session)
    auto_assign_tags_to_posts(session)
    show_posts_with_tags(session)
    find_users_by_tag_name(session, "python")
    find_users_by_tag_name(session, "sql")
    find_posts_by_tags_names(session, "sql", "python")
    find_posts_by_two_tags(session, "python", "lesson")
    find_posts_by_all_tags(session, "python", "lesson", "flask")

    session.close()


if __name__ == "__main__":
    main()
