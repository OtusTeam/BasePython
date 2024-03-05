from sqlalchemy import String

from sqlalchemy.orm import Mapped, mapped_column

from models.db import db
from models.mixins.created_at_mixin import CreatedAtMixin


class Product(CreatedAtMixin, db.Model):
    name: Mapped[str] = mapped_column(String(32), unique=True)
