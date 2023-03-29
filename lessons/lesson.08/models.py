from datetime import datetime
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    username: str
    email: str | None = None


class Author(BaseModel):
    id: int
    name: str
    user: User


class Post(BaseModel):
    title: str
    body: str = ""
    created_at: datetime = Field(default_factory=datetime.utcnow)
    # tags: list[str] = Field(default_factory=list)
    tags: list[str] = []


def main():
    user = User(id="1", username="john")
    print(user)
    user_dict = user.dict()
    user_dict["email"] = "john@e.c"
    print(user_dict)

    author = Author(
        id=b"123",
        name="John Smith",
        user=user_dict,
    )
    print(author)
    print(repr(author))
    print(repr(author.user))

    post = Post(
        title="Python news",
        created_at="2023-01-31T10:42:50",
    )
    post.tags.append("tag1")
    print(post)
    print(Post(title="qwe", tags=["abc", b"qwe", 346]))
    post_2 = Post(title="123")
    print(post_2)
    post_2.tags.append("tag2")
    print(post_2)
    print(id(post.tags))
    print(id(post_2.tags))


if __name__ == "__main__":
    main()


