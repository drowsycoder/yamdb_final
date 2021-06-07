from django.contrib.auth import get_user_model
from rest_framework import serializers, validators

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор класса User.

    Роль по умолчанию: user
    Проверяет email и username на уникальность.
    """

    role = serializers.ChoiceField(choices=User.Role.choices, default='user')
    email = serializers.EmailField(
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'bio',
            'email',
            'role',
        )
