# Generated by Django 3.1.6 on 2022-05-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_game', '0012_auto_20220522_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='true_table',
            name='cost_price',
            field=models.FloatField(default=0, verbose_name='Себестоимость'),
        ),
        migrations.AlterField(
            model_name='true_table',
            name='cost_price_per_one_detector',
            field=models.FloatField(default=500, verbose_name='Цена детектора'),
        ),
        migrations.AlterField(
            model_name='true_table',
            name='cost_price_per_one_maket',
            field=models.FloatField(default=200, verbose_name='Цена макета'),
        ),
        migrations.AlterField(
            model_name='true_table',
            name='salary',
            field=models.FloatField(default=10000, verbose_name='З/п работников'),
        ),
    ]
