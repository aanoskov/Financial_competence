# Generated by Django 3.1.6 on 2022-05-22 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('financial_game', '0011_true_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='true_table',
            name='salary',
            field=models.FloatField(default=10000, verbose_name='З/п 1-го работника'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Имя игрока'),
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('binaries', models.CharField(default='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0', max_length=43, verbose_name='')),
                ('values', models.CharField(default='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0', max_length=300, verbose_name='')),
                ('blue_card_text', models.CharField(default='', max_length=300, verbose_name='')),
                ('green_card_text', models.CharField(default='', max_length=300, verbose_name='')),
                ('player', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Админ-класс',
                'verbose_name_plural': 'Админ-таблицы',
            },
        ),
    ]
