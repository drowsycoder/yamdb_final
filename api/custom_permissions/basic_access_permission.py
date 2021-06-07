from rest_framework import permissions

from .is_author_or_higher import IsAuthorOrHigherOrReadOnly


class BasicAccessPermission(permissions.BasePermission):
    """Базовый класс разрешений для работы с CRUD.

    Используется для взаимодействия с произведением, его жанром и категорией.
    """

    def has_permission(self, request, view):
        return view.action in ['list', 'retrieve'] or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return IsAuthorOrHigherOrReadOnly
