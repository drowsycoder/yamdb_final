from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.custom_permissions import IsAdminRoleOrSuperuser
from api.models import User
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """CRUD для модели User.

    Админ и суперюзер могут выполнять все операции и искать по username.
    Пользователь может смотреть и редактировать свои учётные денные.
    """

    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminRoleOrSuperuser]
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'username',
    ]

    @action(
        methods=['GET', 'PATCH'],
        detail=False,
        permission_classes=[IsAuthenticated],
    )
    def me(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data)
        if request.method == 'PATCH':
            serializer = UserSerializer(
                user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
