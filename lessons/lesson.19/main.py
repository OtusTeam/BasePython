import sys

from sqlalchemy.orm import joinedload

from models.base import Session
from models import User, Author, Post, Tag


def create_tag(session, name):
    tag = Tag(name=name)
    session.add(tag)
    session.commit()


def create_post(session, username, title):
    user = session.query(User).filter_by(username=username).one_or_none()
    if user:
        author = session.query(Author).filter_by(user=user).one_or_none()
        if author:
            post = Post(title=title, author_id=author.id)
            session.add(post)
            session.commit()
            print("Создано успешно")
    else:
        print("Нет или пользователя или он не автор")


def all_posts(session):
    items = session.query(Post).all()
    for item in items:
        print(item)


def create_author(session, username):
    user = session.query(User).filter_by(username=username).one_or_none()
    if user:
        author = Author(user_id=user.id)
        session.add(author)
        session.commit()
    else:
        print("Такого пользователя нет")


def all_authors(session):
    items = session.query(Author).all()
    for item in items:
        print(item)
        print(item.posts)


def all_users_with_author_data(session):
    items = session.query(User).all()
    for item in items:
        print("user", item)
        print("author", item.author)


def registration(session, username):
    user = User(username=username)
    session.add(user)
    session.commit()


def all_users(session):
    items = session.query(User).all()
    for item in items:
        print(item)


def exit(session):
    session.close()
    sys.exit(0)


def hello(session, name):
    print("Hello,", name)


def link_tag(session, post_title, tag_name):
    post = session.query(Post).filter_by(title=post_title).one_or_none()
    if not post:
        print("Такого поста нету")
        return
    tag = session.query(Tag).filter_by(name=tag_name).one_or_none()
    if not tag:
        tag = Tag(name=tag_name)
        session.add(tag)
        session.commit()
    # Добавить тэг к посту
    post.tags.append(tag)
    session.commit()


# 1 - *
def authors_posts(session):
    # Взять авторов вместе с постами
    authors = session.query(Author).all()
    for author in authors:
        print(f"-------------->{author.user.username}<-------------")
        for post in author.posts:
            print(f"post: {post.title}")
        print("-----------------------------------------------------")


def authors_posts_opt(session):
    # Взять авторов вместе с постами
    authors = session.query(Author).options(joinedload(Author.posts)).all()
    for author in authors:
        print(f"-------------->{author.created_at}<-------------")
        for post in author.posts:
            print(f"post: {post.title}")
        print("-----------------------------------------------------")


# * - *
def posts_tags(session):
    posts = session.query(Post).all()
    for post in posts:
        print(f"-------------->{post.title}<-------------")
        for tag in post.tags:
            print(f"tag: {tag.name}")
        print("-----------------------------------------------------")


def posts_tags_opt(session):
    posts = session.query(Post).options(joinedload(Post.tags)).all()
    for post in posts:
        print(f"-------------->{post.title}<-------------")
        for tag in post.tags:
            print(f"tag: {tag.name}")
        print("-----------------------------------------------------")


def all_blog_data(session):
    users = session.query(User).all()
    for user in users:
        print(f"---------->{user.username}<-------------")
        if user.author:
            print(f"{user.username} is author")
            for post in user.author.posts:
                print(f"post: {post.title}")
                for tag in post.tags:
                    print(f"tag: {tag.name}")

        print("---------------------------------")


def all_blog_data_opt(session):
    users = (
        session.query(User)
        .options(joinedload(User.author).joinedload(Author.posts).joinedload(Post.tags))
        .all()
    )
    for user in users:
        print(f"---------->{user.username}<-------------")
        if user.author:
            print(f"{user.username} is author")
            for post in user.author.posts:
                print(f"post: {post.title}")
                for tag in post.tags:
                    print(f"tag: {tag.name}")

        print("---------------------------------")


actions = {
    "exit": exit,
    "hello": hello,
    "registration": registration,
    "all_users": all_users,
    "all_authors": all_authors,
    "alwd": all_users_with_author_data,
    "create_author": create_author,
    "create_post": create_post,
    "all_posts": all_posts,
    "create_tag": create_tag,
    "link_tag": link_tag,
    "authors_posts": authors_posts,
    "posts_tags": posts_tags,
    "all_blog_data": all_blog_data,
    "authors_posts_opt": authors_posts_opt,
    "posts_tags_opt": posts_tags_opt,
    "all_blog_data_opt": all_blog_data_opt,
}


def main():
    session = Session()

    while True:
        input_str = input("->")
        action_name, *params = input_str.split()
        action = actions[action_name]
        action(session, *params)


if __name__ == "__main__":
    main()
