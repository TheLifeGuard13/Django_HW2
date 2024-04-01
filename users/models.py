from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, null=True, blank=True, verbose_name='телефон')
    avatar = models.ImageField(upload_to='users/', null=True, blank=True, verbose_name='аватар')
    country = models.CharField(max_length=50, null=True, blank=True, verbose_name='страна')
    auth_token = models.CharField(max_length=30, default='', blank=True, null=True, verbose_name='ключ')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
