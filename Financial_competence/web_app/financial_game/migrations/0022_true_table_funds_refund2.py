# Generated by Django 4.0.4 on 2022-05-24 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_game', '0021_true_table_funds_refund'),
    ]

    operations = [
        migrations.AddField(
            model_name='true_table',
            name='funds_refund2',
            field=models.FloatField(default=0, verbose_name='Дополнительная переменная, в которой хранится процент'),
        ),
    ]
