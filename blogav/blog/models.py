from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Краткое содержание')
    content = models.TextField(verbose_name='Полное содержание')
    created_data = models.DateTimeField(default=timezone.now, verbose_name='Время создания')
    published_date = models.DateTimeField(blank=True, db_index=True, null=True,
                                          verbose_name='Время публикации')
    is_commentable = models.BooleanField(default=True, verbose_name='Разрешены комментарии')
    author = models.ForeignKey('auth.User')

    class Meta():
        ordering = ['-published_date']
        verbose_name = 'Статья блога'
        verbose_name_plural = 'Статьи блога'

    def __str__(self):
        return self.title

    def publish(self):
        self.pablished_date = timezone.now()
        self.save()
