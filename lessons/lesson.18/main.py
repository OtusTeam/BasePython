import random
from sqlalchemy.orm import joinedload

from models import (
    User,
    Session,
    Tag,
    Post,
    Author,
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


# Создать тэги (посмотреть)
def create_tags(session):
    names = ['python', 'java', 'js']
    for name in names:
        existing_tag = session.query(Tag).filter_by(name=name).one_or_none()
        if not existing_tag:
            tag = Tag(name=name)
            session.add(tag)


def create_posts_by_username(session, username, names):
    ext = session.query(User).filter_by(username=username).one_or_none()
    if not ext:
        user = User(username=username)
        session.add(user)

        ext = session.query(Author).filter_by(user_id=user.id).one_or_none()
        if not ext:
            author = Author(user_id=user.id)
            session.add(author)
            for name in names:
                ext = session.query(Post).filter_by(author_id=author.id, title=name).one_or_none()
                if not ext:
                    post = Post(author_id=author.id, title=name)
                    session.add(post)


def create_posts(session):
    create_posts_by_username(session, 'leo', ['Django', 'Web', 'Javascript'])
    create_posts_by_username(session, 'max', ['Asp', 'Spring', 'Vue.js'])

# Создать посты
# Связать посты с тегами (посмотреть в базу)

def link_to_tags(session):
    posts = session.query(Post).all()
    tags = session.query(Tag).all()

    for post in posts:
        random_tags = random.sample(tags, len(tags) - 1)
        for tag in random_tags:
            if tag not in post.tags:
                post.tags.append(tag)
            else:
                print('Такой тэг уже есть')

# Вывести посты с тегами + оптимизация
def get_posts_with_tags(session):
    posts = session.query(Post).all()
    print('-----------start---------------------------')
    for post in posts:
        print(f'---------------->{post.title}<----------------')
        for tag in post.tags:
            print(f'------){tag.name}(---------')
    print('---------------------------------------------------')

def get_posts_with_tags_opt(session):
    posts = session.query(Post).options(joinedload(Post.tags)).all()
    print('-----------start---------------------------')
    for post in posts:
        print(f'---------------->{post.title}<----------------')
        for tag in post.tags:
            print(f'------){tag.name}(---------')
    print('---------------------------------------------------')

def get_users_by_tag(tag):
    print('users^--------')
    for post in tag.posts:
        author = post.author
        user = author.user
        print(user)
    print('end users^')

    # Вывести всё + оптимизация
def get_all_data(session):
    print('-------start---------')
    users = session.query(User).all()
    for user in users:
        print(f'user-{user.username}')
        author = user.author
        print('user is Author')
        for post in author.posts:
            print(f'post-{post.title}')
            for tag in post.tags:
                print(f'tag-{tag.name}')
                # get_users_by_tag(tag)
    print('end')

def get_all_data_opt(session):
    print('-------start---------')

    users = session.query(User).options(
        joinedload(User.author).
        joinedload(Author.posts).
        joinedload(Post.tags)
    ).all()

    for user in users:
        print(f'user-{user.username}')
        author = user.author
        print('user is Author')
        for post in author.posts:
            print(f'post-{post.title}')
            for tag in post.tags:
                print(f'tag-{tag.name}')
                # get_users_by_tag(tag)
    print('end')




def main():
    # Base.metadata.drop_all()
    # Base.metadata.create_all()

    session = Session()
    # create_users(session)
    # create_authors(session)
    # create_posts(session)
    # get_users(session)
    # get_users_with_authors(session)
    # get_authors_with_users(session)
    # get_authors_with_posts(session)
    # get_authors_with_posts_joined(session)
    #create_tags(session)

    #create_posts(session)

    # link_to_tags(session)

    session.commit()

    # get_posts_with_tags_opt(session)
    get_all_data_opt(session)

    session.close()


if __name__ == "__main__":
    main()
