# id id1 id2
# id post_id tag_id
# id (post_id tag_id)
# (post_id tag_id)
# id post_id tag_id creator_id


from sqlalchemy import Table, Column, Integer, ForeignKey

from blog_project.models import Base


posts_tags_table = Table(
    "posts_tags_association_table",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), nullable=False),
    Column("tag_id", Integer, ForeignKey("tags.id"), nullable=False),
)
