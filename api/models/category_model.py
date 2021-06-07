from django.db import models


class Category(models.Model):
    """Модель категории, к которой относится произведение."""
    name = models.CharField('категория', max_length=200, unique=True)
    slug = models.SlugField('slug', unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        indexes = [models.Index(fields=['name']), ]

    def __str__(self):
        return self.name
