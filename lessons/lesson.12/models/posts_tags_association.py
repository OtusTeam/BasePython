__all__ = ("PostsTagsAssociation",)
from dataclasses import dataclass
from typing import TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from models import Post, Tag


@dataclass
class PostsTagsAssociation:
    def get_posts_by_tag(self, tag_name: str) -> list[Post]:
        pass

    def get_tags_for_post(self, post_id: UUID) -> list[Tag]:
        pass
