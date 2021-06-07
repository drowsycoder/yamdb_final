from api.models import Genre
from api.serializers import GenreSerializer

from .customapiviewset import CustomAPIViewSet


class GenreViewSet(CustomAPIViewSet):
    """Представление для взаимодействия (CRUD) с жанром произведения."""
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
