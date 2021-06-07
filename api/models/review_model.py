from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .title_model import Title
from .user_model import User


class Review(models.Model):
    """Модель отзыва на произведение."""

    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name='reviews',
                              verbose_name='произведение')
    text = models.TextField('отзыв')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='reviews',
                               verbose_name='автор')
    score = models.PositiveSmallIntegerField(
        'оценка',
        validators=[
            MinValueValidator(1, message='оценка не может быть меньше 1'),
            MaxValueValidator(10, message='оценка не может быть больше 10')
        ]
    )
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        constraints = [models.UniqueConstraint(fields=['author', 'title'],
                                               name='unique_review')]
        indexes = [
            models.Index(fields=['pub_date']),
            models.Index(fields=['score']),
        ]
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        return self.text
