# Generated by Django 5.0.2 on 2024-03-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_version_version_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='version_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер версии'),
        ),
    ]
