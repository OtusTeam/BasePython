from sqlalchemy import (
    select,
    func,
)

from sqlalchemy.orm import (
    Session,
    joinedload,
    selectinload,
)

from models import (
    Base,
    engine,
    User,
    Article,
)


def create_users(
    session: Session,
):
    bob = User(
        username="bob",
        email="bob@example.com",
    )
    alice = User(
        username="alice",
    )
    john = User(
        username="john",
        full_name="John Smith",
    )
    session.add(bob)
    session.commit()

    session.add(alice)
    session.add(john)

    session.commit()


def fetch_user_by_username(
    session: Session,
    username: str,
) -> User:
    stmt = select(User).where(User.username == username)
    return session.execute(stmt).scalar_one()


def create_article(
    session: Session,
    user: User,
    title: str,
    body: str,
) -> None:
    article = Article(
        title=title,
        body=body,
        author_id=user.id,
    )
    session.add(article)
    session.commit()


def create_articles_for_users(
    session: Session,
):
    bob = fetch_user_by_username(
        session=session,
        username="bob",
    )
    alice = fetch_user_by_username(
        session=session,
        username="alice",
    )
    create_article(
        session,
        bob,
        "The Future of Technology",
        "In this article, we explore the advancements in technology that are shaping our future. From AI to quantum computing, the possibilities are endless.",
    )
    create_article(
        session,
        alice,
        "Healthy Living: Tips and Tricks",
        "This publication provides practical tips for maintaining a healthy lifestyle, including diet, exercise, and mental well-being.",
    )
    create_article(
        session,
        alice,
        "Traveling the World: A Guide",
        "A comprehensive guide to traveling the world, covering the best destinations, travel tips, and cultural experiences.",
    )


def fetch_all_articles(
    session: Session,
) -> list[Article]:
    stmt = select(Article).order_by(Article.id)
    return list(session.scalars(stmt))


def fetch_articles_with_authors(
    session: Session,
) -> list[Article]:
    stmt = (
        select(Article)
        .order_by(Article.id)
        .options(
            joinedload(Article.author),
        )
    )
    return list(session.scalars(stmt))


def fetch_users_with_articles(
    session: Session,
) -> list[User]:
    stmt = (
        select(User)
        # .where(func.length(User.username) < 5)
        .order_by(User.id).options(
            selectinload(User.articles),
        )
    )
    return list(session.scalars(stmt))


def show_articles_with_authors(
    session: Session,
):
    articles = fetch_articles_with_authors(session)
    for article in articles:
        print(
            article.id,
            "-",
            article.title,
            "@",
            article.author,
            # repr(article.author),
            article.author.email,
        )


def main():
    print(Base.metadata.tables)
    Base.metadata.create_all(bind=engine)
    with Session(engine) as session:
        # create_users(session)
        # fail = fetch_user_by_username(
        #     session=session,
        #     username="fail",
        # )
        # create_articles_for_users(session)
        # articles = fetch_all_articles(session)
        # show_articles_with_authors(session)
        # show_articles_with_authors(session)
        users = fetch_users_with_articles(session)
        for user in users:
            print("Articles", user.id, user.username, user.email)
            for article in user.articles:
                print(" +", article.id, article.title)
            print("---")


if __name__ == "__main__":
    main()
