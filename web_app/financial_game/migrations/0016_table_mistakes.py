# Generated by Django 3.1.5 on 2022-05-23 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_game', '0015_auto_20220523_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='mistakes',
            field=models.IntegerField(default=0, verbose_name='Ошибки игрока'),
        ),
    ]
