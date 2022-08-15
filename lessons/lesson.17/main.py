import sys
from models.base import Session, Base
from models import User, Author, Post


def create_post(session, username, title):
    user = session.query(User).filter_by(username=username).one_or_none()
    if user:
        author = session.query(Author).filter_by(user=user).one_or_none()
        if author:
            post = Post(title=title, author_id=author.id)
            session.add(post)
            session.commit()
            print('Создано успешно')
    else:
        print('Нет или пользователя или он не автор')


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
        print('Такого пользователя нет')


def all_authors(session):
    items = session.query(Author).all()
    for item in items:
        print(item)
        print(item.posts)


def all_users_with_author_data(session):
    items = session.query(User).all()
    for item in items:
        print('user', item)
        print('author', item.author)


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
    print('Hello,', name)


actions = {
    'exit': exit,
    'hello': hello,
    'registration': registration,
    'all_users': all_users,
    'all_authors': all_authors,
    'alwd': all_users_with_author_data,
    'create_author': create_author,
    'create_post': create_post,
    'all_posts': all_posts
}


def main():
    Base.metadata.create_all()
    session = Session()

    while True:
        input_str = input('->')
        action_name, *params = input_str.split()
        action = actions[action_name]
        action(session, *params)


if __name__ == '__main__':
    main()