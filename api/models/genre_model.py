from django.db import models


class Genre(models.Model):
    """Модель жанра, к которому относится произведение."""
    name = models.CharField('жанр', max_length=200, unique=True)
    slug = models.SlugField('slug', unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'
        indexes = [models.Index(fields=['name']), ]

    def __str__(self):
        return self.name
