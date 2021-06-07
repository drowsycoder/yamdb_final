from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель User под проект api Yamdb.

    Поле email используется вместо username.
    Новые поля: bio, role.
    """

    class Role(models.TextChoices):
        USER = 'user', ('user')
        MODERATOR = 'moderator', ('moderator')
        ADMIN = 'admin', ('admin')

    bio = models.TextField('о себе', blank=True, null=True)
    role = models.CharField(
        'роль в API', max_length=9, choices=Role.choices, default=Role.USER
    )
    email = models.EmailField('адрес электронной почты', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        indexes = [
            models.Index(
                fields=['email'], name='user_email_idx'),
            models.Index(
                fields=['username'], name='user_username_idx'),
        ]
        ordering = ['role', '-email']

    @property
    def has_api_administrate_permission(self):
        return self.role == self.Role.ADMIN or self.is_superuser

    @property
    def has_api_moderate_permission(self):
        return self.role in [self.Role.MODERATOR,
                             self.Role.ADMIN] or self.is_superuser
