from functools import wraps

from sqlalchemy.orm import joinedload, selectinload

from blog_project.models.database import Base, Session
from blog_project.models import User, Author, Post


def with_session(func):

    @wraps(func)
    def wrapper(*args):
        session = Session()
        func(session, *args)
        session.close()

    return wrapper


def create_user():
    session = Session()
    sam = User(username="sam", is_staff=False)
    print("create", sam)
    session.add(sam)
    session.commit()
    print("saved sam")
    print("sam:", sam)
    session.close()


def create_author_sam():
    session = Session()

    sam: User = session.query(User).filter_by(username="sam").one()
    author_sam = Author(
        name="Samuel White",
        # user_id=3,
        user=sam,
    )

    print("create author for sam:", author_sam, sam)

    session.add(author_sam)
    session.commit()

    print("created author for sam:", author_sam)

    print("user on author:", author_sam.user)
    print("author on user:", sam.author)

    session.close()


@with_session
def create_posts_for_john(session):
    author_john: Author = (
        session
        .query(Author)
        .join(User)
        .filter(User.username == "john")
        .one()
    )
    print(author_john)

    post_django = Post(
        title="Lesson Django",
        author=author_john,
    )
    print("post_django:", post_django)

    post_flask = Post(
        title="Lesson Flask",
        author=author_john,
    )
    print("post_flask:", post_flask)

    session.add(post_django)
    session.add(post_flask)

    session.commit()

    print("post_django:", post_django)
    print("post_flask:", post_flask)


@with_session
def fetch_post_with_all_data(session):
    # posts: list[Post] = session.query(Post).all()
    posts: list[Post] = (
        session
        .query(Post)
        .options(
            joinedload(Post.author)
            .joinedload(Author.user)
        )
        .all()
    )

    for post in posts:
        print("post:", post)
        print("post.author", post.author)
        print("post.author.user", post.author.user)


@with_session
def fetch_authors_with_lesson_posts_with_all_data(session):
    q_authors = (
        session
        .query(Author)
        .join(Post, Post.author_id == Author.id)
        .options(
            joinedload(Author.user),
            joinedload(Author.posts),
            # selectinload(Author.posts),
        )
        .filter(Post.title.ilike("lesson%"))
    )

    # print(q_authors)

    authors: list[Author] = q_authors.all()

    for author in authors:
        print("author:", author)
        print("author.user", author.user)
        print("author.posts", author.posts)


@with_session
def promote_user_sam(session):
    sam: User = session.query(User).filter_by(username="sam").one()
    print("sam before", sam)
    sam.is_staff = True

    session.commit()
    print("sam after", sam)


@with_session
def check_username_exists(session, username):
    sam_count = session.query(User).filter_by(username=username).count()
    result = bool(sam_count)
    print("Username", username, "exists?", result)
    return result


def main():
    print("User mro", User.mro())
    # Base.metadata.create_all()  # NEVER!

    # create_user()
    # create_author_sam()
    # create_posts_for_john()
    # fetch_post_with_all_data()
    # fetch_authors_with_lesson_posts_with_all_data()
    # promote_user_sam()
    check_username_exists("sam")
    check_username_exists("admin")
    check_username_exists("john")


if __name__ == '__main__':
    main()
