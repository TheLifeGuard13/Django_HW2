from django.db import models


class Blog(models.Model):

    header = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, null=True, blank=True, verbose_name='Читабельная ссылка')
    description = models.TextField(null=True, blank=True, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blogs/', null=True, blank=True, verbose_name='Изображение')
    created_at = models.DateField(null=True, blank=True, auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Активно')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return f'{self.header}'

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
