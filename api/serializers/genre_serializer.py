from rest_framework import serializers

from api.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для модели жанра произведения (Genre)."""

    class Meta:
        model = Genre
        exclude = ['id']
