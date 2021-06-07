from rest_framework import filters, mixins, viewsets

from api.custom_permissions import BasicAccessPermission


class CustomAPIViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    """Базовый суперкласс представления для работы с CRUD.

    Используется для взаимодействия с жанром и категорией произведения.
    """
    permission_classes = [BasicAccessPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name', ]
    lookup_field = 'slug'
