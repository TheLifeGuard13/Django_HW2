from django.conf import settings
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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Владелец')
    is_published = models.BooleanField(null=True, blank=True, default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

        permissions = [
            ('set_published', 'Can publish products'),
            ('change_description', 'Can change description'),
            ('change_category', 'Can change category'),
        ]


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Version(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(null=True, blank=True, verbose_name='Номер версии')
    version_name = models.CharField(null=True, blank=True, max_length=100, verbose_name='Название версии')
    is_actual = models.BooleanField(default=False, verbose_name='Текущая версия')

    def __str__(self):
        return f'{self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
