from sqladmin import Admin

from admin.access_token import AccessTokenAdmin
from admin.user import UserAdmin


def register_admin_views(admin: Admin):
    admin.add_view(AccessTokenAdmin)
    admin.add_view(UserAdmin)
