# Generated by Django 5.0.2 on 2024-03-24 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.IntegerField(blank=True, null=True, verbose_name='Номер версии')),
                ('version_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название версии')),
                ('is_actual', models.BooleanField(default=False, verbose_name='Текущая версия')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.SET, to='catalog.products', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'контакт',
                'verbose_name_plural': 'контакты',
            },
        ),
    ]