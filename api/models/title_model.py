from django.db import models

from api.validators import year_validator

from .category_model import Category
from .genre_model import Genre


class Title(models.Model):
    """Модель произведения (фильма, книги, песни)."""
    name = models.CharField('название произведения', max_length=100)
    year = models.SmallIntegerField('год', blank=True, null=True,
                                    validators=[year_validator], )
    description = models.TextField(
        'описание',
        max_length=1000,
        blank=True,
        null=True)
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='жанры',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='категория',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'произведение'
        verbose_name_plural = 'произведения'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['year']),
        ]

    def __str__(self):
        return self.name
