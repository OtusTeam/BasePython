import random

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload, selectinload

from models import session_factory, Post, Tag, User


def get_all_users(session: Session) -> list[User]:
    stmt = select(User).order_by(User.id)
    users = session.scalars(stmt).all()
    return list(users)


def get_all_tags(session: Session) -> list[Tag]:
    stmt = select(Tag).order_by(Tag.name)
    tags = session.scalars(stmt).all()
    return list(tags)


def create_users(session: Session) -> list[User]:
    usernames = ["john", "bob", "kyle", "alice", "kate"]
    users = [
        User(
            username=username,
            email=f"{username}@email.com",
            full_name=f"Full Name {username} - {idx}",
        )
        for idx, username in enumerate(usernames, start=1)
    ]
    session.add_all(users)
    session.commit()
    return users


# Другие возможные теги
tag_django = "django"
tag_fastapi = "fastapi"
tag_flask = "flask"
tag_docker = "docker"
tag_pytest = "pytest"
tag_coroutines = "coroutines"

# Название постов и ассоциированные с ними уникальные теги
titles_with_tags = (
    (
        "Оптимизация производительности Django приложений и ускорение тестов",
        (
            tag_django,
            tag_pytest,
            "optimization",
        ),
    ),
    (
        "Flask vs FastAPI vs Django: сравнение подходов",
        (
            tag_flask,
            tag_fastapi,
            tag_django,
            tag_coroutines,
        ),
    ),
    (
        "Работа с асинхронностью в Django",
        (
            tag_coroutines,
            tag_django,
        ),
    ),
    (
        "Использование Docker для деплоя Flask приложения",
        (
            tag_docker,
            tag_flask,
            "deployment",
        ),
    ),
    (
        "Автоматическое тестирование FastAPI с pytest",
        (
            tag_fastapi,
            tag_pytest,
            "automation",
        ),
    ),
    (
        "Управление зависимостями в Python проектах",
        ("virtualenv",),
    ),
)


def create_tags(session: Session) -> list[Tag]:
    tags_names = set()
    for _, tags in titles_with_tags:
        tags_names.update(tags)

    tags = [Tag(name=name) for name in tags_names]
    session.add_all(tags)
    session.commit()

    return tags


def create_posts(session: Session) -> list[Post]:
    users = get_all_users(session)
    tags = get_all_tags(session)
    selected_users = random.sample(users, 3)
    available_posts_info = list(titles_with_tags)
    tags_map = {tag.name: tag for tag in tags}
    posts = []
    for idx, user in enumerate(selected_users, start=1):
        items = [available_posts_info.pop() for _ in range(idx)]

        for title, tag_names in items:
            post = Post(
                title=title,
                text=f"Контент поста {title!r}",
                user=user,
            )
            for tag_name in tag_names:
                tag = tags_map[tag_name]
                post.tags.append(tag)
            posts.append(post)

    session.add_all(posts)
    session.commit()
    return posts


def create_values():
    with session_factory() as session:
        create_users(session)
        create_tags(session)
        create_posts(session)


def show_posts_with_authors(session: Session):
    stmt = (
        select(Post)
        .options(
            # к одному всегда joinedload
            joinedload(Post.user),
        )
        .order_by(Post.id)
    )
    posts = session.scalars(stmt).all()

    for post in posts:
        print("-", post)
        print("  by", post.user)


def show_posts_with_authors_and_tags(session: Session):
    stmt = (
        select(Post)
        .options(
            # к одному всегда joinedload
            joinedload(Post.user),
            selectinload(Post.tags),
        )
        .order_by(Post.id)
    )
    posts = session.scalars(stmt).all()

    for post in posts:
        print("-", post)
        print("  by", post.user)
        print(" •", [tag.name for tag in post.tags])


def show_users_with_posts(session: Session):
    stmt = (
        select(User)
        .options(
            # для "ко многим" всегда selectinload
            selectinload(User.posts),
        )
        .order_by(User.id)
    )
    users = session.scalars(stmt).all()
    for user in users:
        print(user)
        for post in user.posts:
            print("-", post)


def show_users_with_posts_with_tags(session: Session):
    stmt = (
        select(User)
        .options(
            # для "ко многим" всегда selectinload
            selectinload(User.posts).selectinload(Post.tags),
        )
        .order_by(User.id)
    )
    users = session.scalars(stmt).all()
    for user in users:
        print(user)
        for post in user.posts:
            print("-", post)
            print(" •", [tag.name for tag in post.tags])


def fetch_values():
    with session_factory() as session:
        # show_posts_with_authors(session)
        # show_users_with_posts(session)
        # show_users_with_posts_with_tags(session)
        show_posts_with_authors_and_tags(session)


def main() -> None:
    # create_values()
    fetch_values()


if __name__ == "__main__":
    main()
