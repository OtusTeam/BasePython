from sqlalchemy.orm import joinedload

from models import Session, User, Post, Tag


def create_users():
    session = Session()

    username = "admin"
    admin = User(username=username, is_staff=True)
    print(admin)

    guest = User(username="guest")
    print(guest)

    session.add(admin)
    session.add(guest)
    session.commit()
    print(admin)
    print(guest)

    session.close()


def create_posts():
    session = Session()

    guest: User = session.query(User).filter_by(username="guest").one()
    print("guest posts before:", guest.posts)

    post1 = Post(title="Flask lesson", user_id=guest.id)
    post2 = Post(title="Django lesson", user=guest)

    session.add(post1)
    session.add(post2)
    session.commit()

    print(post1)
    print(post2)
    print("guest posts after:", guest.posts)

    session.close()


def create_tags():
    session = Session()

    tag1 = Tag(name="flask")
    tag2 = Tag(name="django")
    tag3 = Tag(name="news")

    session.add(tag1)
    session.add(tag2)
    session.add(tag3)
    session.commit()

    print(tag1, tag2, tag3)

    session.close()


def connect_tags_with_posts():
    session = Session()

    # tags = session.query(Tag).all()
    # print(tags)

    q_tags = session.query(Tag)
    tag_flask: Tag = q_tags.filter_by(name="flask").one()
    tag_django: Tag = q_tags.filter_by(name="django").one()
    tag_news: Tag = q_tags.filter_by(name="news").one()

    print(tag_flask, tag_django, tag_news)

    q_posts = session.query(Post)
    post_django: Post = q_posts.filter(Post.title.ilike("django%")).first()
    post_flask: Post = q_posts.filter(Post.title.ilike("flask%")).first()

    print(post_django, post_flask)

    print("post_django.tags", post_django.tags)
    print("tag_flask.posts", tag_flask.posts)
    print("tag_django.posts", tag_django.posts)

    post_django.tags.append(tag_django)
    post_django.tags.append(tag_news)

    tag_flask.posts.append(post_flask)
    tag_news.posts.append(post_flask)

    session.commit()

    print("post_django.tags", post_django.tags)
    print("post_flask.tags", post_flask.tags)
    print("tag_flask.posts", tag_flask.posts)
    print("tag_django.posts", tag_django.posts)
    print("tag_news.posts", tag_news.posts)

    session.close()


def remove_tag():
    session = Session()

    post_django: Post = session.query(
        Post,
    ).filter(
        Post.title.ilike("django%")
    ).options(
        joinedload(Post.tags)
    ).first()

    print("post django:", post_django, post_django.tags)
    # tag_news: Tag = session.query(Tag).filter_by(name="news").one()

    for tag in post_django.tags:
        if tag.name == "news":
            post_django.tags.remove(tag)
            break

    session.commit()

    session.close()


if __name__ == "__main__":
    create_users()
    create_posts()
    create_tags()
    connect_tags_with_posts()
    remove_tag()
