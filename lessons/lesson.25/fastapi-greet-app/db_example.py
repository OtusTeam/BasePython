from typing import Sequence

from sqlalchemy import select, update
from sqlalchemy import and_
from sqlalchemy import func
from sqlalchemy import or_
from sqlalchemy.orm import Session, defer, aliased
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import selectinload

from models.db import engine
from models import User, Post, Tag


def create_user(
    session: Session,
    username: str,
    email: str | None = None,
) -> User:
    user = User(
        username=username,
        email=email,
    )
    session.add(user)
    session.commit()

    print("saved user")
    print("user info:", user)
    # session.refresh(user)

    return user


def create_users(
    session: Session,
    *usernames: str,
) -> list[User]:
    users = [
        # create new user
        User(username=username)
        # for each username
        for username in usernames
    ]
    session.add_all(users)
    session.commit()
    print("saved users:", users)
    return users


def get_user_by_primary_key(
    session: Session,
    pk: int,
) -> User | None:
    # user = session.get(User, pk)
    user = session.get(User, pk)
    # session.refresh(user)
    print("user for pk", pk, "result:", user)
    return user


def find_user_by_pk(
    session: Session,
    pk: int,
) -> User:
    stmt = select(User).where(
        User.id == pk,
        # User.id > 10,
    )
    # result = session.execute(stmt)
    # user = result.scalar()
    # user = session.scalar(stmt)
    result = session.execute(stmt)
    # user: User | None = result.scalar_one_or_none()
    # user: User = result.scalar_one()
    # user: User = result.scalars().first()
    user: User = result.scalar_one()
    print(user)
    return user


def find_user_by_username(
    session: Session,
    username: str,
) -> User | None:
    stmt = select(User).where(User.username == username)
    # user: User | None = session.scalar(stmt)
    user: User | None = session.scalars(stmt).one_or_none()
    print("user username", username, user)
    return user


def search_users(
    session: Session,
) -> Sequence[User]:
    no_email_and_a_in_username_condition = and_(
        User.email.isnot(None),
        User.username.ilike("%a%"),
    )
    stmt = (
        select(User)
        .where(
            or_(
                User.username.ilike("%e"),
                no_email_and_a_in_username_condition,
            )
        )
        .order_by(User.id)
    )
    users = session.scalars(stmt).all()

    for user in users:
        print(user)

    # print(list(users))
    return users


#


def create_posts(
    session: Session,
    user: User,
    *posts_titles: str,
) -> list[Post]:
    posts = [
        # create a new post for this user
        Post(title=title, user_id=user.id)
        # for each title in titles
        for title in posts_titles
    ]
    session.add_all(posts)
    session.commit()

    for post in posts:
        print(post)

    print(posts)

    return posts


def show_posts_with_authors(
    session: Session,
):
    # N + 1
    # 1 - запрос на все посты
    # N - количество постов, количество подгрузок пользователей
    # stmt = select(Post).order_by(Post.id)

    # это не тот `.join` !!
    stmt = (
        # fetch all posts
        select(Post)
        # extra params for ORM
        .options(
            # join all authors to posts in SQL, for use in ORM. one query
            # joinedload(Post.author),
            # extra SQL request, for use in ORM. second query
            selectinload(Post.author)
        )
        # sort
        .order_by(Post.id)
    )

    posts = session.scalars(stmt).all()
    for post in posts:  # type: Post
        print(post)
        print("+ author:", post.author)


def show_users_with_posts(session: Session):
    stmt = (
        # all users
        select(User)
        # extra ORM options
        .options(
            # 'to many' - only selectinload
            selectinload(User.posts)
        )
        # sort
        .order_by(User.id)
    )

    users = session.scalars(stmt).all()

    for user in users:  # type: User
        print(user)
        for post in user.posts:
            print("-", post)


def show_all_posts_count(session: Session):
    stmt = select(func.count(Post.id))
    print("posts count:", session.scalar(stmt))


def show_users_posts_counts(session: Session):
    stmt = (
        # query
        select(
            # full user
            User,
            # count
            func.count(Post.id).label("posts_count"),
        )
        .join(
            User.posts,
            isouter=True,
        )
        .group_by(User.id)
        # sort
        .order_by(User.id)
    )
    result = session.execute(stmt)
    for user, posts_count in result.all():
        print(posts_count, "posts by user", user)


def find_users_by_post_filter(session: Session):
    stmt = (
        select(User)
        .join(User.posts)
        # .where(
        #     Post.title.ilike("%intro%"),
        # )
        .group_by(User.id)
        .having(func.count(Post.id) > 1)
        .order_by(User.id)
    )
    users = session.scalars(stmt).all()
    for user in users:
        print(user)


def create_tags(
    session: Session,
    *tag_names: str,
) -> list[Tag]:
    tags = [
        # create a new post for this user
        Tag(name=name)
        # for each title in titles
        for name in tag_names
    ]
    session.add_all(tags)
    session.commit()

    print(tags)

    return tags


def auto_associate_posts_and_tags(
    session: Session,
):
    posts: Sequence[Post] = (
        #
        session.scalars(
            #
            select(Post)
            .options(
                selectinload(Post.tags),
            )
            .order_by(Post.id)
        ).all()
    )
    tags: Sequence[Tag] = (
        #
        session.scalars(
            #
            select(Tag).order_by(Tag.id)
        ).all()
    )
    for post in posts:
        title = post.title.lower()
        for tag in tags:
            if (
                # check if post title matches tag
                tag.name.lower() in title
                # and if tag is not already associated
                and tag not in post.tags
            ):
                post.tags.append(tag)

    session.commit()


def semi_manual_associate_posts_and_tags(
    session: Session,
):
    # tag_lesson = session.execute(
    #     select(Tag).where(Tag.name == "lesson"),
    # ).scalar_one()
    tag_code_editors = session.execute(
        select(Tag).where(Tag.name == "code-editors"),
    ).scalar_one()
    # tag_news = session.execute(
    #     select(Tag).where(Tag.name == "news"),
    # ).scalar_one()

    posts_editors = session.scalars(
        select(Post)
        .where(
            or_(
                Post.title.icontains("vs code"),
                Post.title.icontains("pycharm"),
            )
        )
        .options(selectinload(Post.tags))
    ).all()
    for post in posts_editors:
        post.tags.append(tag_code_editors)

    session.commit()


def show_posts_with_tags(session: Session):
    posts = session.scalars(
        select(Post)
        .options(
            selectinload(Post.tags),
            defer(Post.created_at),
            # defer(...  # from tag)
        )
        .order_by(Post.id)
    ).all()

    for post in posts:
        print("+ Post:")
        print(post.id, post.title)
        print("Tags:")
        for tag in post.tags:
            print("-", tag)


def show_tags_with_posts(session: Session):
    tags = session.scalars(
        select(Tag)
        .options(
            selectinload(Tag.posts),
        )
        .order_by(Tag.id)
    ).all()

    for tag in tags:
        print("+ Tag:", tag)
        for post in tag.posts:
            print("-", post.id, post.title)


def show_posts_which_have_tag(
    session: Session,
    tag_name: str,
):
    stmt = (
        select(Post)
        .join(Post.tags)
        .where(
            Tag.name == tag_name,
        )
    )
    posts = session.scalars(stmt).all()
    print("Next posts for tag", repr(tag_name))
    for post in posts:
        print("+ Post:", post.id, post.title)


def show_users_with_posts_with_this_tag(
    session: Session,
    tag_name: str,
):
    stmt = (
        select(User)
        .join(User.posts)
        .join(Post.tags)
        .where(
            Tag.name == tag_name,
        )
        .group_by(User)
    )
    print("users with posts by tag", repr(tag_name))
    # users = session.scalars(stmt).unique().all()
    users = session.scalars(stmt).all()
    for user in users:
        print(user)


def show_posts_which_have_one_of_tags(
    session: Session,
    *tag_names: str,
):
    stmt = (
        select(Post)
        .join(Post.tags)
        .where(
            or_(
                # unpack
                *(
                    # lower
                    func.lower(Tag.name) == tag_name.lower()
                    # for each one
                    for tag_name in tag_names
                )
            ),
        )
        .order_by(Post.id)
    )
    posts = session.scalars(stmt).unique().all()
    print("Next posts for tag", repr(tag_names))
    for post in posts:
        print("+ Post:", post.id, post.title)


def show_posts_which_have_two_tags(
    session: Session,
    tag_1: str,
    tag_2: str,
):
    table_tags_1 = aliased(Tag, name="table_tags_1")
    table_tags_2 = aliased(Tag, name="table_tags_2")
    stmt = (
        select(Post)
        .join(
            table_tags_1,
            Post.tags,
        )
        .join(
            table_tags_2,
            Post.tags,
        )
        .where(
            func.lower(table_tags_1.name) == tag_1.lower(),
            func.lower(table_tags_2.name) == tag_2.lower(),
        )
        .order_by(Post.id)
    )
    posts = session.scalars(stmt).unique().all()
    print("Next posts for tags", repr(tag_1), "and", repr(tag_2))
    for post in posts:
        print("+ Post:", post.id, post.title)


def show_posts_which_have_all_of_the_tags(
    session: Session,
    *tag_names: str,
):
    tags_names = list(set(map(str.lower, tag_names)))

    stmt = select(Post)
    filters = []
    for tag_name in tags_names:
        table = aliased(Tag, name=f"tags_{tag_name}")
        stmt = stmt.join(
            table,
            Post.tags,
        )
        filters.append(func.lower(table.name) == tag_name)

    stmt = stmt.where(
        *filters,
    ).order_by(Post.id)
    posts = session.scalars(stmt).unique().all()
    print("Next posts for tags", repr(tags_names))
    for post in posts:
        print("+ Post:", post.id, post.title)


def main():
    with Session(engine, expire_on_commit=True) as session:
        # create_user(session, "john")
        # create_user(session, "sam", "sam@example.com")
        #
        # create_users(
        #     session,
        #     "bob",
        #     "alice",
        #     "kate",
        #     "jack",
        # )
        #
        # get_user_by_primary_key(session, 0)
        # get_user_by_primary_key(session, 1)
        # get_user_by_primary_key(session, 3)
        # get_user_by_primary_key(session, 10)
        # find_user_by_pk(session, 1)
        # # find_user_by_pk(session, 0)
        # find_user_by_username(session, "bob")
        # find_user_by_username(session, "sam")
        # find_user_by_username(session, "qwerty")
        # search_users(session)
        #
        # user_john: User = find_user_by_username(session, "john")
        # user_sam: User = find_user_by_username(session, "sam")
        # john_posts: list[Post] = create_posts(
        #     session,
        #     user_john,
        #     "MySQL Lesson",
        #     "MS SQL Intro",
        #     "Postgres update review",
        # )
        # sam_posts: list[Post] = create_posts(
        #     session,
        #     user_sam,
        #     "PyCharm recent release details",
        #     "VS Code tips and tricks",
        # )
        # show_posts_with_authors(session)
        # show_users_with_posts(session)
        # show_all_posts_count(session)
        # show_users_posts_counts(session)
        # find_users_by_post_filter(session)
        #
        # create_tags(
        #     session,
        #     "MySQL",
        #     "MS SQL",
        #     "Postgres",
        #     "lesson",
        #     "code-editors",
        #     "news",
        # )
        # auto_associate_posts_and_tags(session)
        # semi_manual_associate_posts_and_tags(session)
        # show_posts_with_tags(session)
        # show_tags_with_posts(session)
        # show_posts_which_have_tag(session, "news")
        # show_users_with_posts_with_this_tag(session, "news")
        # show_posts_which_have_one_of_tags(
        #     session,
        #     "code-editors",
        #     "news",
        # )

        # show_posts_which_have_two_tags(
        #     session,
        #     "code-editors",
        #     "news",
        # )

        show_posts_which_have_all_of_the_tags(
            session,
            "code-editors",
            "news",
        )

        show_posts_which_have_all_of_the_tags(
            session,
            "MS SQL",
            "Postgres",
            "news",
        )


if __name__ == "__main__":
    main()
