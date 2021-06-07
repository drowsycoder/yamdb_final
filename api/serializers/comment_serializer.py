from rest_framework import serializers

from api.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели комментария к отзыву (Comment)."""

    author = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field='username')
    review = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field='score')

    class Meta:
        model = Comment
        fields = '__all__'
