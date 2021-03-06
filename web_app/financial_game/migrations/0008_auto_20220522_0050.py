# Generated by Django 3.1.6 on 2022-05-21 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_game', '0007_auto_20220521_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='greencard',
            old_name='count_1',
            new_name='count_prod',
        ),
        migrations.RenameField(
            model_name='greencard',
            old_name='percent',
            new_name='percents',
        ),
        migrations.RenameField(
            model_name='greencard',
            old_name='price_1',
            new_name='price_prod',
        ),
        migrations.RemoveField(
            model_name='greencard',
            name='count_2',
        ),
        migrations.RemoveField(
            model_name='greencard',
            name='price_2',
        ),
        migrations.AddField(
            model_name='greencard',
            name='count_online',
            field=models.IntegerField(default=1, verbose_name='Кол-во товара в этом месяце'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='greencard',
            name='count_opt',
            field=models.IntegerField(default=1, verbose_name='Кол-во товара в этом месяце'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='greencard',
            name='count_opt_1',
            field=models.IntegerField(default=1, verbose_name='Кол-во товара в этом месяце'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='greencard',
            name='count_opt_2',
            field=models.IntegerField(default=1, verbose_name='Кол-во товара в следующем месяце'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='greencard',
            name='earnings_opt',
            field=models.IntegerField(default=1, verbose_name='Выручка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='greencard',
            name='price_earn',
            field=models.IntegerField(default=1, verbose_name='Цена 1 товара в этом месяце'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='greencard',
            name='price_online',
            field=models.IntegerField(default=1, verbose_name='Цена 1 товара в этом месяце'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='greencard',
            name='price_opt_1',
            field=models.IntegerField(default=1, verbose_name='Цена 1 товара в этом месяце'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='greencard',
            name='price_opt_2',
            field=models.IntegerField(default=1, verbose_name='Цена 1 товара в следующем месяце'),
            preserve_default=False,
        ),
    ]
