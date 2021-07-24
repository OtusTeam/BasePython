from functools import wraps
from pprint import pprint

from sqlalchemy.orm import joinedload

from models import User, Author, Article
from models.database import Base, Session


def with_session(func):
    @wraps(func)
    def wrapper():
        session = Session()
        func(session)
        session.close()

    return wrapper


def create_tables():
    Base.metadata.create_all()
    print("Created tables")


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

    author_nick = Author(name="Nick Gray", user=user_nick)
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


def main():
    create_tables()
    create_items()

    query_authors()
    load_joined()
    load_joined2()
    load_joined_many()
    load_joined_many_joins()
    load_query_joined()
    load_query_joined_many()


if __name__ == '__main__':
    main()
