from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.utils.crypto import get_random_string

YAMBD_API_V1 = settings.YAMBD_API_V1
SUBJECT = YAMBD_API_V1['SUBJECT']
CONFIRMATION_CODE_TITLE = YAMBD_API_V1['CONFIRMATION_CODE_TITLE']
RANDOM_STRING_LENGTH = YAMBD_API_V1['RANDOM_STRING_LENGTH']


class EmailAuth(models.Model):
    """Временная таблица для хранения email, confirmation code и даты запроса.

    Отправляет сообщение с confirmation code на указанный email.
    Эти данные требуются для генерации JWT токена.
    """

    email = models.EmailField(
        'адрес электронной почты', unique=True)
    confirmation_code = models.CharField(
        'код подтверждения', max_length=RANDOM_STRING_LENGTH)
    added = models.DateTimeField(
        'дата запроса', auto_now_add=True
    )

    class Meta:
        verbose_name = 'запрос кода подтверждения'
        verbose_name_plural = 'запросы кода подтверждения'
        indexes = [
            models.Index(
                fields=['email', 'confirmation_code'], name='email_code_idx'),
        ]

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.confirmation_code = get_random_string(RANDOM_STRING_LENGTH)
        message = f'{CONFIRMATION_CODE_TITLE}: {self.confirmation_code}'
        try:
            send_mail(
                SUBJECT, message, from_email=None, recipient_list=[self.email]
            )
        except SMTPException:
            return None

        super().save(*args, **kwargs)
