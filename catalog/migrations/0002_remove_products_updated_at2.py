# Generated by Django 5.0.2 on 2024-02-25 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='updated_at2',
        ),
    ]