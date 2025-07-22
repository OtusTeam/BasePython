import logging
from collections.abc import Sequence, Iterable
from itertools import cycle

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, joinedload, selectinload, subqueryload

import config
from models import Base, User, Datacenter, Profile, Article

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
)

LOG_DEFAULT_FORMAT = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)

log = logging.getLogger(__name__)


def create_datacenter(
    session: Session,
    name: str,
) -> Datacenter:
    dc = Datacenter(name=name)
    session.add(dc)
    session.commit()
    log.info("Created datacenter %s", dc)
    return dc


def create_users(
    session: Session,
    *usernames: str,
    dcs: Iterable[Datacenter],
) -> Sequence[User]:
    users = [
        User(
            username=username,
            dc=dc,
        )
        for (username, dc) in zip(usernames, dcs)
    ]

    log.info("Creating users: %s", users)
    session.add_all(users)
    session.commit()
    log.info("Created %d users", len(users))
    return users


def create_profile(
    session: Session,
    user: User,
) -> Profile:
    profile = Profile(
        about=f"{user.username}'s profile",
        user_id=user.id,
    )
    session.add(profile)
    session.commit()
    log.info("Created profile: %s", profile)
    return profile


def create_articles(
    session: Session,
    user: User,
    *titles: str,
) -> Sequence[Article]:
    articles = [
        Article(
            title=title,
            user_id=user.id,
        )
        for title in titles
    ]
    session.add_all(articles)
    session.commit()
    log.info("Created %d articles", len(articles))
    return articles


def create_entities(
    session: Session,
) -> None:
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    dc1 = create_datacenter(session, "dc1")
    dc2 = create_datacenter(session, "dc2")
    users: Sequence[User] = create_users(
        session,
        "admin",
        "bob",
        "alice",
        "kyle",
        "jack",
        "kate",
        dcs=cycle([dc1, dc2]),
    )
    for user in users:
        create_profile(session, user)

    for count, user in enumerate(users):
        if not count:
            continue
        titles = [f"title - {idx} - {user.username}" for idx in range(1, count + 1)]
        create_articles(session, user, *titles)


def get_users_with_relationships(session: Session) -> Sequence[User]:
    statement = (
        # get all users
        select(User)
        # also load profiles in the same query
        .options(
            # join profile in the same query
            joinedload(User.profile),
            # join all articles in the next query
            selectinload(User.articles),
            # joinedload(User.articles),
            # subqueryload(User.articles),
            # joinedload(User.dc),
            selectinload(User.dc),
        )
        # sort users by id
        .order_by(User.id)
    )
    # return session.scalars(statement).unique().all()
    return session.scalars(statement).all()


def get_articles_with_relationships(session: Session) -> Sequence[Article]:
    statement = (
        # get all articles
        select(Article)
        # load authors in the same query
        .options(
            joinedload(Article.user).joinedload(User.profile),
        )
        # order by user id
        .order_by(
            # сортируем сначала по юзеру
            Article.user_id,
            # а в рамках юзера сортируем по названию
            Article.title,
        )
    )
    return session.scalars(statement).all()


def demo_get_users_with_relations(
    session: Session,
) -> None:
    users = get_users_with_relationships(session)
    for user in users:
        print("+", user, user.dc)
        print("\t| Profile:", user.profile)
        if not user.articles:
            print()
            continue
        print("Articles:")
        for article in user.articles:
            print("\t*", article)
        print()


def demo_get_articles_with_relations(
    session: Session,
) -> None:
    articles = get_articles_with_relationships(session)
    for article in articles:
        print("+", article)
        print("\tAuthor:", article.user, article.user.profile)


def main():
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_DEFAULT_FORMAT,
    )
    with Session(engine) as session:
        # create_entities(session)
        demo_get_users_with_relations(session)
        # demo_get_articles_with_relations(session)


if __name__ == "__main__":
    main()
