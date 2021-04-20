from sqlalchemy.orm import joinedload

from blog_project.models import (
    Session,
    User,
    Post,
    Tag,
)


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

    admin: User = session.query(User).filter_by(username="admin").one()
    print("admin:", admin)
    print("admin posts before:", admin.posts)

    post_flask = Post(title="Flask lesson", user=admin)
    post_django = Post(title="Django lesson", user_id=admin.id)

    session.add(post_flask)
    session.add(post_django)
    session.commit()

    print("post flask", post_flask)
    print("post django", post_django)

    print("admin posts after:", admin.posts)

    session.close()


def create_tags():
    tags = Session.query(Tag).all()
    print("tags:", tags)

    tag_news = Tag(name="news")
    tag_django = Tag(name="django")
    tag_flask = Tag(name="flask")

    Session.add(tag_news)
    Session.add(tag_flask)
    Session.add(tag_django)

    Session.commit()

    tags = Session.query(Tag).all()
    print("tags:", tags)

    Session.close()


def assign_tags_to_posts():

    tag_news = Session.query(Tag).filter_by(name="news").one()
    tag_django = Session.query(Tag).filter_by(name="django").one()
    tag_flask = Session.query(Tag).filter_by(name="flask").one()

    print(tag_news, tag_django, tag_flask)

    post_django: Post = Session.query(Post).filter(Post.title.ilike("%django%")).first()
    post_flask: Post = Session.query(Post).filter(Post.title.ilike("%flask%")).first()

    print(post_django)
    print(post_flask)

    post_django.tags.append(tag_news)
    post_django.tags.append(tag_django)

    post_flask.tags.append(tag_news)
    post_flask.tags.append(tag_flask)

    Session.commit()

    print(post_django)
    print(post_flask)

    Session.close()


def load_and_remove_tags():
    post_flask: Post = Session.query(
        Post,
    ).filter(
        Post.title.ilike("%flask%"),
    ).options(
        joinedload(Post.tags),
    ).first()

    print("***** post_flask", post_flask)

    for tag in post_flask.tags:
        if tag.name == "news":
            post_flask.tags.remove(tag)
            break

    Session.commit()

    print("***** post_flask", post_flask)

    Session.close()


def main():
    create_users()
    create_posts()
    create_tags()
    assign_tags_to_posts()
    load_and_remove_tags()


if __name__ == "__main__":
    main()
