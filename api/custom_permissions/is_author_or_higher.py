from rest_framework import permissions


class IsAuthorOrHigherOrReadOnly(permissions.BasePermission):
    """Проверка прав доступа пользователя.

    Изменять объекты могут их авторы или пользователи имеющие роли

    'admin', 'moderator' и superuser."""

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (request.method in permissions.SAFE_METHODS
                or user.has_api_moderate_permission
                or obj.author == user)
