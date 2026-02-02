import asyncio
import random

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from models import async_session, Post, Tag, User


async def get_all_users(
    session: AsyncSession,
) -> list[User]:
    stmt = select(User).order_by(User.id)
    result = await session.scalars(stmt)
    return list(result.all())


async def get_all_tags(
    session: AsyncSession,
) -> list[Tag]:
    stmt = select(Tag).order_by(Tag.name)
    result = await session.scalars(stmt)
    tags = result.all()
    return list(tags)


async def create_users(
    session: AsyncSession,
) -> list[User]:
    usernames = [
        "john",
        "bob",
        "kyle",
        "alice",
        "kate",
    ]
    users = [
        User(
            username=username,
            email=f"{username}@email.com",
            full_name=f"Full Name {username} - {idx}",
        )
        for idx, username in enumerate(usernames, start=1)
    ]
    session.add_all(users)
    print("all users before commit:", users)
    await session.commit()
    await session.refresh(users[0])
    print("all users after commit:", users)
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


async def create_tags(
    session: AsyncSession,
) -> list[Tag]:
    tags_names = set()
    for _, tags in titles_with_tags:
        tags_names.update(tags)

    tags = [Tag(name=name) for name in tags_names]
    session.add_all(tags)
    await session.commit()

    return tags


async def create_posts(
    session: AsyncSession,
) -> list[Post]:
    users: list[User] = await get_all_users(session)
    tags: list[Tag] = await get_all_tags(session)
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
    await session.commit()
    return posts


async def create_values():
    async with async_session() as session:
        await create_users(session)
        await create_tags(session)
        await create_posts(session)


async def show_posts_with_authors(
    session: AsyncSession,
):
    stmt = (
        select(Post)
        .options(
            # к одному всегда joinedload
            joinedload(Post.user),
        )
        .order_by(Post.id)
    )
    result = await session.scalars(stmt)
    posts = result.all()

    for post in posts:
        print("-", post)
        print("  by", post.user)


async def show_posts_with_authors_and_tags(
    session: AsyncSession,
):
    stmt = (
        select(Post)
        .options(
            # к одному всегда joinedload
            joinedload(Post.user),
            selectinload(Post.tags),
        )
        .order_by(Post.id)
    )
    result = await session.scalars(stmt)
    posts = result.all()

    for post in posts:
        print("-", post)
        print("  by", post.user)
        print(" •", [tag.name for tag in post.tags])


async def show_users_with_posts(
    session: AsyncSession,
):
    stmt = (
        select(User)
        .options(
            # для "ко многим" всегда selectinload
            selectinload(User.posts),
        )
        .order_by(User.id)
    )
    result = await session.scalars(stmt)
    users = result.all()
    for user in users:
        print(user)
        for post in user.posts:
            print("-", post)


async def show_users_with_posts_with_tags(
    session: AsyncSession,
):
    stmt = (
        select(User)
        .options(
            # для "ко многим" всегда selectinload
            selectinload(User.posts).selectinload(Post.tags),
        )
        .order_by(User.id)
    )
    result = await session.scalars(stmt)
    users = result.all()
    for user in users:
        print(user)
        for post in user.posts:
            print("-", post)
            print(" •", [tag.name for tag in post.tags])


async def update_post_text(
    session: AsyncSession,
    contains_text: str,
    new_text: str,
) -> None:
    stmt = select(Post).where(Post.text.contains(contains_text))
    result = await session.execute(stmt)
    post: Post = result.scalar_one()
    print("post before update:", post, post.created_at, post.updated_at)
    post.text = f"{new_text} - {random.randint(1, 10)}"
    await session.commit()
    print("post after update:", post, post.created_at, post.updated_at)
    await session.refresh(
        post,
        # (
        #     "created_at",
        #     "updated_at",
        # ),
    )
    print("post after refresh:", post, post.created_at, post.updated_at)


async def fetch_values():
    async with async_session() as session:
        await show_posts_with_authors(session)
        await show_users_with_posts(session)
        await show_users_with_posts_with_tags(session)
        await show_posts_with_authors_and_tags(session)


async def main() -> None:
    # await create_values()
    await fetch_values()
    async with async_session() as session:
        await update_post_text(
            session,
            contains_text="foobar",
            new_text="very new text foobar",
        )


if __name__ == "__main__":
    asyncio.run(main())
