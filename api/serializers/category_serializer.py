from rest_framework import serializers

from api.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели категории произведения (Category)."""

    class Meta:
        model = Category
        exclude = ['id']
