# from .create import create
# from .update import update_user
# from .delete import delete

# from . import create

__all__ = (
    "create",
    "update_user",
    "delete",
    "USER_MAGIC_ID",
)

from .create import create
from .update import update_user
from .delete import delete

USER_MAGIC_ID = 42
