from combojsonapi.permission import PermissionMixin, PermissionForGet, PermissionUser


class BaseAllowGetAllPermission(PermissionMixin):
    ALL_FIELDS = []

    def get(
        self,
        *args,
        many=True,
        user_permission: PermissionUser = None,
        **kwargs,
    ) -> PermissionForGet:
        """
        Allow all the declared columns
        """
        self.permission_for_get.allow_columns = (self.ALL_FIELDS, 10)
        return self.permission_for_get
