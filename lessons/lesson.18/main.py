from functools import wraps
from pprint import pprint

from sqlalchemy.orm import joinedload

from blog_project.models import User, Author, Article, Tag
from blog_project.models.database import Session


def with_session(func):
    @wraps(func)
    def wrapper():
        session = Session()
        func(session)
        session.close()

    return wrapper


def query_authors():
    session = Session()

    author = session.query(Author).first()
    print(author)
    print("Author user:", author.user)

    user = session.query(User).get(author.user_id)
    print(user)
    print("User author:", user.author)

    session.close()


def load_joined():
    session = Session()

    query = session.query(User).options(joinedload(User.author))
    users_w_authors = query.all()
    for user in users_w_authors:
        print("user:", user)
        print("user's author:", user.author)

    session.close()


def load_joined2():
    session = Session()

    query = session.query(Author).options(joinedload(Author.user))
    authors_w_users = query.all()
    for author in authors_w_users:
        print("author", author)
        print("author's user", author.user)

    author_1 = query.get(1)
    print("A1", author_1)

    session.close()


@with_session
def load_joined_many(session):
    q_author_with_articles = session.query(Author).options(joinedload(Author.articles))
    author_with_articles = q_author_with_articles.all()

    for author in author_with_articles:
        print("author", author)
        print("author's articles:")
        for article in author.articles:
            print("-", article)


@with_session
def load_joined_many_joins(session):
    q_users_w_authors_with_articles = (
        session
            .query(User)
            .options(
            joinedload(User.author)
                .joinedload(Author.articles)
        )
    )
    users_w_authors_with_articles = q_users_w_authors_with_articles.all()

    for user in users_w_authors_with_articles:
        print("user", user)
        if not user.author:
            print("no author")
            continue
        print("user's author", user.author)
        print("author's articles:")
        for article in user.author.articles:
            print("-", article)


@with_session
def load_query_joined(session):
    q_john_articles = (
        session
            .query(Article)
            .join(
            Author,
            Author.id == Article.author_id,
        )
            .filter(Author.name.ilike("john%"))
    )

    articles = q_john_articles.all()

    for article in articles:
        print("-", article)


@with_session
def load_query_joined_many(session):
    q_users_flask_aricles = (
        session
            .query(User)
            .join(
            Author,
            Author.user_id == User.id,
        )
            .join(
            Article,
            Article.author_id == Author.id,
        )
            .filter(
            Article.title.ilike("%flask%"),
        )
    )

    users = q_users_flask_aricles.all()

    print("users with flask articles:")
    for user in users:
        print(user)


@with_session
def create_items(session):
    user_nick = User(username="nick")
    session.add(user_nick)

    author_nick = Author(name="Nick Gray", user=user_nick, bio="I like Docker!")
    session.add(author_nick)

    article_1 = Article(
        title="Docker intro",
        body="Hello..",
        author=author_nick,
    )
    session.add(article_1)

    article_2 = Article(
        title="docker-compose intro",
        body="Hello again..",
        author=author_nick,
    )
    session.add(article_2)

    session.commit()

    print("user", user_nick)
    print("author", author_nick)
    print("articles")
    pprint(author_nick.articles)

    article_3 = Article(
        title="PyCharm intro",
        body="lalala..",
    )
    author_nick.articles.append(article_3)

    session.commit()
    print("articles")
    pprint(author_nick.articles)


def assign_tags_by_title_contains(session, tag: Tag, text: str):
    q_articles = (
        session
            .query(Article)
            .filter(Article.title.ilike(f"%{text}%"))
    )
    articles = q_articles.all()
    print(f"articles for text {text!r}:")
    pprint(articles)
    for article in articles:
        article.tags.append(tag)

    return articles


@with_session
def create_tags(session):
    tag_docker = Tag(name="docker")
    tag_python = Tag(name="python")
    tag_pycharm = Tag(name="pycharm")
    tag_dataclasses = Tag(name="dataclasses")
    tag_intro = Tag(name="intro")

    tags = [
        tag_docker,
        tag_python,
        tag_pycharm,
        tag_dataclasses,
        tag_intro,
    ]
    session.add_all(tags)

    session.commit()
    print("Created tags:")
    pprint(tags)

    docker_articles = assign_tags_by_title_contains(session, tag_docker, "docker")
    intro_articles = assign_tags_by_title_contains(session, tag_intro, "intro")
    dataclasses_articles = assign_tags_by_title_contains(session, tag_dataclasses, "dataclasses")
    pycharm_articles = assign_tags_by_title_contains(session, tag_pycharm, "pycharm")
    python_articles = assign_tags_by_title_contains(session, tag_python, "python")

    session.commit()
    pprint(docker_articles)
    pprint(intro_articles)
    pprint(dataclasses_articles)
    pprint(pycharm_articles)
    pprint(python_articles)


@with_session
def fetch_with_tags(session):
    # q_articles = (
    #     session
    #         .query(Article)
    #         .filter(Article.title.ilike("%docker%"))
    # )
    # articles = q_articles.all()
    # print("fetched articles:")
    # pprint(articles)

    q_articles = (
        session
            .query(Article)
            .filter(Article.title.ilike("%docker%"))
            .options(
            joinedload(Article.tags)
        )
    )
    articles = q_articles.all()
    print("fetched articles with tags:")
    pprint(articles)


@with_session
def fetch_authors_by_tags(session):
    q_users_python_articles = (
        session
            .query(User)
            .join(Author, User.author)
            .join(Article, Author.articles)
            .join(Tag, Article.tags)
            .filter(
                Tag.name == "python",
            )
    )

    users = q_users_python_articles.all()
    print("users with python articles")
    pprint(users)


def main():
    create_items()
    create_tags()
    fetch_with_tags()
    fetch_authors_by_tags()


if __name__ == '__main__':
    main()
