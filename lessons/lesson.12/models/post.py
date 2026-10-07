__all__ = ("Post",)

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
from uuid import UUID

from models.posts_tags_association import PostsTagsAssociation

if TYPE_CHECKING:
    from models import User, Tag


@dataclass
class Post:
    id: UUID
    title: str
    body: str

    users: list[User] = field(default_factory=list)

    def add_user(self, user: User):
        if not user in self.users:
            self.users.append(user)

    @property
    def tags(self) -> list[Tag]:
        assoc = PostsTagsAssociation()
        return assoc.get_tags_for_post(self.id)
