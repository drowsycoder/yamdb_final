from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from api.models import EmailAuth

User = get_user_model()
RANDOM_STRING_LENGTH = settings.YAMBD_API_V1['RANDOM_STRING_LENGTH']


class EmailAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAuth
        fields = ('email',)


class EmailCodePairSerializer(TokenObtainPairSerializer):
    """Сериализатор токена.

    1. Проверяет, что email и confirmation code указаны верно и есть в БД.
    2. Если п.1 верен, удаляет эту связку и создает нового пользователя.
    User.username создается на основе email. Берётся часть перед @.
    3. Генерируется сам токе.
    """

    email = serializers.EmailField()
    confirmation_code = serializers.CharField(
        max_length=RANDOM_STRING_LENGTH, min_length=RANDOM_STRING_LENGTH)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False

    def check_conf_code(self, email: str, confirmation_code: str) -> True:
        """Проверяет, что email и confirmation code в БД.

        Если нет, то вызывает исключение ValidationError с описанием.
        """
        try:
            email_code = EmailAuth.objects.get(
                email=email, confirmation_code=confirmation_code)
        except EmailAuth.DoesNotExist:
            raise serializers.ValidationError(
                'Didn\'t find such email and confirmation code combination. '
                'Please get email notification with confirmation code and '
                'post email and code to get token')
        email_code.delete()
        return True

    def validate(self, attrs):
        email = attrs['email']
        confirmation_code = attrs['confirmation_code']
        if self.check_conf_code(email, confirmation_code):
            username = email.split('@')[0]
            self.user, _ = User.objects.get_or_create(
                email=attrs.get('email'), username=username
            )
            token = self.get_token(self.user)
            data = {'token': str(token.access_token)}
            return data
        raise serializers.ValidationError(
            'Something gone wrong')
