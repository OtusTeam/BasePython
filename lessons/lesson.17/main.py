from sqlalchemy.orm import joinedload

from models import (
    User, Base, Session,
    # Author,
    # Post,
)


def create_user(session, username):
    user = User(username=username)

    session.add(user)

    print(user)
    session.commit()
    print(user)

    return user


def create_author(session, username, name):
    user = session.query(User).filter(User.username == username).one_or_none()
    if user:
        author = Author(user_id=user.id, name=name)
        session.add(author)
        session.commit()
        print(author)

        return author


def create_post(session, username, title, body):
    user = session.query(User).filter(User.username == username).one_or_none()
    if user:
        author = session.query(Author).filter(Author.user_id == user.id).one_or_none()
        if author:
            post = Post(author_id=author.id, title=title, body=body)
            session.add(post)
            session.commit()
            print(post)

            return post


def create_users(session):
    create_user(session, "john")
    create_user(session, "sam")
    user = create_user(session, "nick")
    # user.archived = True


def create_authors(session):
    create_author(session, 'john', 'john blogger')
    create_author(session, 'sam', 'sam user')


def create_posts(session):
    create_post(session, 'john', 'Hello, Python!', 'The Zen of Python')
    create_post(session, 'john', 'Simple code', 'print("hello, world!")')
    create_post(session, 'sam', 'Good morning )', 'Hello!')


def get_users(session):
    users = session.query(User).all()
    print('-' * 80)
    for el in users:
        print(el)
    print('-' * 80)
    return users


def get_users_with_authors(session):
    users = session.query(User).all()
    print('-' * 80)
    for el in users:
        print('user:', el)
        print('author:', el.author)
    print('-' * 80)
    return users


def get_authors_with_users(session):
    authors = session.query(Author).all()
    print('-' * 80)
    for el in authors:
        print('author:', el)
        # print('user:', el.user)
    print('-' * 80)
    return authors


def get_authors_with_posts(session):
    authors = session.query(Author).all()
    print('-' * 80)
    for el in authors:
        print('author:', el)
        print('posts:', el.posts)
    print('-' * 80)
    return authors


def get_authors_with_posts_joined(session):
    authors = (
        session.query(Author)
        # .join(Post)
        .options(joinedload(Author.posts))
        .all()
    )

    print('-' * 80)
    for el in authors:
        print('author:', el)
        print('posts:', el.posts)
    print('-' * 80)
    return authors


def main():
    # Base.metadata.drop_all()
    # Base.metadata.create_all()

    session = Session()
    create_users(session)
    # create_authors(session)
    # create_posts(session)
    get_users(session)
    # get_users_with_authors(session)
    # get_authors_with_users(session)
    # get_authors_with_posts(session)
    # get_authors_with_posts_joined(session)

    session.commit()

    session.close()


if __name__ == "__main__":
    main()
