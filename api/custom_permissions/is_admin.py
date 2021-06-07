from rest_framework import permissions


class IsAdminRoleOrSuperuser(permissions.BasePermission):
    """Проверка на наличие роли 'admin' или прав суперпользователя"""

    def has_permission(self, request, view) -> bool:
        user = request.user
        if user.is_anonymous:
            return False
        return user.has_api_administrate_permission
