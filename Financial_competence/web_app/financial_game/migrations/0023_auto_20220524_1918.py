# Generated by Django 3.1.7 on 2022-05-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_game', '0022_true_table_funds_refund2'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='show_res',
            field=models.BooleanField(default=0, verbose_name='Показать результат'),
        ),
        migrations.AlterField(
            model_name='bluecard',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='greencard',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='support',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='table',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='true_table',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
