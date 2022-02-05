from functools import wraps

from sqlalchemy import and_, not_, or_
from sqlalchemy.orm import joinedload, selectinload, aliased

from blog_project.models.database import Base, Session
from blog_project.models import User, Author, Post, Tag


def with_session(func):

    @wraps(func)
    def wrapper(*args):
        session = Session()
        func(session, *args)
        session.close()

    return wrapper


@with_session
def create_user(session, username: str):
    user = User(username=username, is_staff=False)
    print("create", user)
    session.add(user)
    session.commit()
    print("saved user")
    print("user:", user)


@with_session
def create_author_for_user(session, username: str, author_name: str):
    user: User = session.query(User).filter_by(username=username).one()
    author = Author(
        name=author_name,
        # user_id=3,
        user=user,
    )

    print("create author for user:", author, user)

    session.add(author)
    session.commit()

    print("created author for user:", author)

    print("user on author:", author.user)
    print("author on user:", user.author)


@with_session
def create_posts_for_user(session, username: str, *posts_titles: str):
    author: Author = (
        session
        .query(Author)
        .join(User)
        .filter(User.username == username)
        .one()
    )
    print(author)

    for title in posts_titles:
        post = Post(
            title=title,
            author=author,
        )
        print("post:", post)

        session.add(post)

    session.commit()


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


@with_session
def create_tags(session, *names: str):
    tags = [
        Tag(name=name)
        for name in names
    ]
    print(tags)

    session.add_all(tags)
    session.commit()


@with_session
def create_posts_tags_associations(session):
    q_tags = session.query(Tag)
    tag_python: Tag = q_tags.filter_by(name="python").one()
    other_tags: list[Tag] = q_tags.filter(Tag.id != tag_python.id).all()
    # tag_news: Tag = q_tags.filter_by(name="news").one()
    # tag_django: Tag = q_tags.filter_by(name="django").one()
    # tag_flask: Tag = q_tags.filter_by(name="flask").one()

    posts: list[Post] = session.query(Post).all()

    for post in posts:
        post.tags.append(tag_python)

        for tag in other_tags:
            if tag.name in post.title.lower():
                post.tags.append(tag)

    session.commit()


@with_session
def fetch_posts_with_tags(session):
    posts: list[Post] = session.query(Post).options(joinedload(Post.tags)).all()
    for post in posts:
        print("post:", post)
        print("--tags:", post.tags)


@with_session
def fetch_posts_with_all_data(session):
    posts: list[Post] = (
        session
        .query(Post)
        .options(
            joinedload(Post.tags),
            joinedload(Post.author).joinedload(Author.user),
        )
        .all()
    )
    for post in posts:
        print("post:", post)
        print("*Authored by:", post.author.name, "with username", post.author.user.username)
        print("--tags:", post.tags)


@with_session
def fetch_posts_with_all_data_by_tags(session, *tags: str):
    # required_tags = session.query(Tag).filter(Tag.name.in_(tags))
    # subquery_required_tags = required_tags.subquery()
    posts: list[Post] = (
        session
        .query(Post)
        .join(Tag, Post.tags)
        .filter(
            Tag.name.in_(tags)
        )
        .options(
            joinedload(Post.tags),
            joinedload(Post.author).joinedload(Author.user),
        )
        .all()
    )
    print("posts with tags", tags)
    for post in posts:
        print("post:", post)
        print("*Authored by:", post.author.name, "with username", post.author.user.username)
        print("--tags:", post.tags)


@with_session
def fetch_posts_with_all_data_by_selected_tags(session, tag_1: str, tag_2: str):
    tbl_tags_1 = aliased(Tag, name="tbl_tags_1")
    tbl_tags_2 = aliased(Tag, name="tbl_tags_2")

    posts: list[Post] = (
        session
        .query(Post)
        .join(tbl_tags_1, Post.tags)
        .join(tbl_tags_2, Post.tags)
        .filter(
            tbl_tags_1.name == tag_1,
            tbl_tags_2.name == tag_2,
        )
        .options(
            joinedload(Post.tags),
            joinedload(Post.author).joinedload(Author.user),
        )
        .all()
    )
    # print("posts with tags", tags)
    for post in posts:
        print("post:", post)
        print("*Authored by:", post.author.name, "with username", post.author.user.username)
        print("--tags:", post.tags)


@with_session
def fetch_posts_with_all_data_by_all_tags(session, *tags: str):
    """

    SELECT blog_posts.id             AS blog_posts_id,
           blog_posts.created_at     AS blog_posts_created_at,
           blog_posts.title          AS blog_posts_title,
           blog_posts.body           AS blog_posts_body,
           blog_posts.status         AS blog_posts_status,
           blog_posts.author_id      AS blog_posts_author_id,
           blog_users_1.id           AS blog_users_1_id,
           blog_users_1.created_at   AS blog_users_1_created_at,
           blog_users_1.username     AS blog_users_1_username,
           blog_users_1.is_staff     AS blog_users_1_is_staff,
           blog_authors_1.id         AS blog_authors_1_id,
           blog_authors_1.created_at AS blog_authors_1_created_at,
           blog_authors_1.name       AS blog_authors_1_name,
           blog_authors_1.user_id    AS blog_authors_1_user_id,
           blog_tags_1.id            AS blog_tags_1_id,
           blog_tags_1.name          AS blog_tags_1_name
    FROM blog_posts
             JOIN posts_tags_association AS posts_tags_association_1 ON blog_posts.id = posts_tags_association_1.post_id
             JOIN blog_tags AS tbl_tags_0 ON tbl_tags_0.id = posts_tags_association_1.tag_id
             JOIN posts_tags_association AS posts_tags_association_2 ON blog_posts.id = posts_tags_association_2.post_id
             JOIN blog_tags AS tbl_tags_1 ON tbl_tags_1.id = posts_tags_association_2.tag_id
             LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_authors_1.id = blog_posts.author_id
             LEFT OUTER JOIN blog_users AS blog_users_1 ON blog_users_1.id = blog_authors_1.user_id
             LEFT OUTER JOIN (posts_tags_association AS posts_tags_association_3 JOIN blog_tags AS blog_tags_1 ON blog_tags_1.id = posts_tags_association_3.tag_id)
                             ON blog_posts.id = posts_tags_association_3.post_id
    WHERE tbl_tags_0.name = 'django'
      AND tbl_tags_1.name = 'python';

    :param session:
    :param tags:
    :return:
    """
    filters = []
    q_posts = session.query(Post)

    for index, tag in enumerate(tags):
        tbl_tags = aliased(Tag, name=f"tbl_tags_{index}")
        # q_posts is immutable, replace it!
        q_posts = q_posts.join(tbl_tags, Post.tags)
        filters.append(tbl_tags.name == tag)

    posts: list[Post] = (
        q_posts
        .filter(*filters)
        .options(
            joinedload(Post.tags),
            joinedload(Post.author).joinedload(Author.user),
        )
        .all()
    )

    print("posts with tags", tags)
    for post in posts:
        print("post:", post)
        print("*Authored by:", post.author.name, "with username", post.author.user.username)
        print("--tags:", post.tags)


def prepare_db_data():
    """
    :return:
    """
    # print("User mro", User.mro())
    # Base.metadata.create_all()  # NEVER!

    create_user("sam")
    create_user("john")
    create_author_for_user("sam", "Samuel White")
    create_author_for_user("john", "John Black")
    create_posts_for_user("john", "Lesson Django", "Lesson Flask")
    create_posts_for_user("sam", "Python News", "Lesson PyCharm")

    fetch_post_with_all_data()
    fetch_authors_with_lesson_posts_with_all_data()
    promote_user_sam()
    check_username_exists("sam")
    check_username_exists("admin")
    check_username_exists("john")
    create_tags("news", "python", "django", "flask")
    create_posts_tags_associations()
    fetch_posts_with_tags()
    fetch_posts_with_all_data()
    fetch_posts_with_all_data_by_tags("news", "flask")
    fetch_posts_with_all_data_by_all_tags("news", "python")
    fetch_posts_with_all_data_by_selected_tags("news", "python")
    fetch_posts_with_all_data_by_all_tags("news", "python")
    fetch_posts_with_all_data_by_all_tags("django", "python")


def main():
    prepare_db_data()


if __name__ == '__main__':
    main()
