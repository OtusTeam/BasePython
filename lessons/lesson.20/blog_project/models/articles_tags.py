from sqlalchemy import Table, Column, Integer, ForeignKey

from blog_project.models.database import Base


articles_tags_table = Table(
    "blog_articles_tags_association_table",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("blog_articles.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("blog_tags.id"), primary_key=True),
)
