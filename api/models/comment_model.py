from django.db import models

from .review_model import Review
from .user_model import User


class Comment(models.Model):
    """Модель комментария к отзыву."""

    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='отзыв')
    text = models.TextField('комментарий')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='автор')
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        indexes = [
            models.Index(fields=['author']),
            models.Index(fields=['pub_date']),
        ]
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return self.text
