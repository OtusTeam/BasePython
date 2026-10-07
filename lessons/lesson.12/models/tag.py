from dataclasses import dataclass
from typing import TYPE_CHECKING

from models.posts_tags_association import PostsTagsAssociation

if TYPE_CHECKING:
    from models import Post


@dataclass
class Tag:
    name: str

    @property
    def posts(self) -> list[Post]:
        assoc = PostsTagsAssociation()
        return assoc.get_posts_by_tag(self.name)
