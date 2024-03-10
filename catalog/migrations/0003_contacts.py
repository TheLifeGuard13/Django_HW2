# Generated by Django 5.0.2 on 2024-03-09 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_products_updated_at2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'контакт',
                'verbose_name_plural': 'контакты',
            },
        ),
    ]
