from django_filters.rest_framework import CharFilter, FilterSet, NumberFilter

from .models import Title


class TitleFilter(FilterSet):
    """Фильтр для представления модели произведения.

    Предполагает фильтрацию по полям названия, категории, жанра и года.
    """
    name = CharFilter(field_name='name', lookup_expr='icontains')
    category = CharFilter(field_name='category__slug', lookup_expr='iexact')
    genre = CharFilter(field_name='genre__slug', lookup_expr='iexact')
    year = NumberFilter(field_name='year', lookup_expr='exact')

    class Meta:
        model = Title
        fields = ['name', 'category', 'genre', 'year']
