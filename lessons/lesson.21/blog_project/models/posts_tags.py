from sqlalchemy import Table, Column, ForeignKey

from blog_project.models.database import Base


posts_tags_association_table = Table(
    "posts_tags_association",
    Base.metadata,
    Column("post_id", ForeignKey("blog_posts.id"), primary_key=True),
    Column("tag_id", ForeignKey("blog_tags.id"), primary_key=True),
)
