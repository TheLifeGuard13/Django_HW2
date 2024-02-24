from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    preview = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Категория')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена за покупку')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True, verbose_name='Дата последнего изменения')
    manufactured_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата производства продукта')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
