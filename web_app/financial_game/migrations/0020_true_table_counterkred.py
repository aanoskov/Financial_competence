# Generated by Django 4.0.4 on 2022-05-23 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_game', '0019_alter_table_own_funds_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='true_table',
            name='counterkred',
            field=models.IntegerField(default=-1, verbose_name='счетчик до окончания выплат по кредиту'),
        ),
    ]
