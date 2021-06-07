from rest_framework import serializers

from . import CategorySerializer, GenreSerializer
from api.models import Category, Genre, Title


class CustomTitleSerializer(serializers.ModelSerializer):
    """Базовый суперкласс сериализатора для модели произведения (Title)."""

    class Meta:
        model = Title
        fields = '__all__'


class TitleGetSerializer(CustomTitleSerializer):
    """Сериализатор для модели произведения (Title).

    Используется для list и retrieve.
    """
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.IntegerField(read_only=True, required=False)


class TitlePostSerializer(CustomTitleSerializer):
    """Сериализатор для модели произведения (Title).

    Используется для create, update и partial_update.
    """
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True,
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
    )
