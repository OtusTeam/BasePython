from pydantic import BaseModel


class User(BaseModel):
    username: str


class Author(BaseModel):
    full_name: str
    user: User
    bio: str

    posts: list["Post"] = []


class Post(BaseModel):
    title: str
    # body: str
    author: Author


def create_post_for_author(author: Author, title: str):
    post = Post(
        title=title,
        author=author,
    )
    author.posts.append(post)
    return post


def main():
    user = User(username="bob")
    author = Author(
        full_name="Bob White",
        user=user,
        bio="I love to write about Python",
    )

    post_a = create_post_for_author(
        author=author,
        title="Python intro",
    )
    post_b = create_post_for_author(
        author=author,
        title="Python tricks",
    )

    print(post_a)
    print(post_b)

    print(author)

    print(author.model_dump_json(indent=2, exclude={"posts"}))

    print(post_a.model_dump_json(indent=2, exclude={"author"}))
    print(post_b.model_dump_json(indent=2, exclude={"author"}))


if __name__ == "__main__":
    main()
