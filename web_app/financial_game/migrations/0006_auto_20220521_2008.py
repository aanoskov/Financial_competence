# Generated by Django 3.1.5 on 2022-05-21 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_game', '0005_auto_20220520_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='ads',
            field=models.FloatField(default=0, verbose_name='Расходы на рекламу'),
        ),
        migrations.AlterField(
            model_name='table',
            name='cash_balance_begin',
            field=models.FloatField(default=10000, verbose_name='Остаток денежных средств на начало'),
        ),
        migrations.AlterField(
            model_name='table',
            name='cash_balance_end',
            field=models.FloatField(default=0, verbose_name='Остаток денежных средств на конец'),
        ),
        migrations.AlterField(
            model_name='table',
            name='cash_flow',
            field=models.FloatField(default=0, verbose_name='Денежный поток'),
        ),
        migrations.AlterField(
            model_name='table',
            name='cost_price',
            field=models.FloatField(default=700, verbose_name='Себестоимость продукции'),
        ),
        migrations.AlterField(
            model_name='table',
            name='current_costs',
            field=models.FloatField(default=0, verbose_name='Текущие расходы всего'),
        ),
        migrations.AlterField(
            model_name='table',
            name='earning_taxes',
            field=models.FloatField(default=0, verbose_name='Общая SUM налогов (6% *Итого Доходов)'),
        ),
        migrations.AlterField(
            model_name='table',
            name='earnings',
            field=models.FloatField(default=0, verbose_name='Выручка'),
        ),
        migrations.AlterField(
            model_name='table',
            name='education',
            field=models.FloatField(default=0, verbose_name='Обучение сотрудников'),
        ),
        migrations.AlterField(
            model_name='table',
            name='equip',
            field=models.FloatField(default=0, verbose_name='Закупка оборудования'),
        ),
        migrations.AlterField(
            model_name='table',
            name='fin_res',
            field=models.FloatField(default=0, verbose_name='Финансовый результат (прибыль/убыток)'),
        ),
        migrations.AlterField(
            model_name='table',
            name='funding',
            field=models.FloatField(default=0, verbose_name='Финансирование'),
        ),
        migrations.AlterField(
            model_name='table',
            name='funds_receipt',
            field=models.FloatField(default=0, verbose_name='Заёмные средства (поступления)'),
        ),
        migrations.AlterField(
            model_name='table',
            name='funds_refund',
            field=models.FloatField(default=0, verbose_name='Заёмные средства (возврат)'),
        ),
        migrations.AlterField(
            model_name='table',
            name='grants',
            field=models.FloatField(default=0, verbose_name='Гранты'),
        ),
        migrations.AlterField(
            model_name='table',
            name='hospitality',
            field=models.FloatField(default=0, verbose_name='Представительские расходы'),
        ),
        migrations.AlterField(
            model_name='table',
            name='investments',
            field=models.FloatField(default=0, verbose_name='Инвестиционные расходы всего'),
        ),
        migrations.AlterField(
            model_name='table',
            name='other',
            field=models.FloatField(default=0, verbose_name='Другие расходы'),
        ),
        migrations.AlterField(
            model_name='table',
            name='other_invest',
            field=models.FloatField(default=0, verbose_name='Другие расходы'),
        ),
        migrations.AlterField(
            model_name='table',
            name='own_funds',
            field=models.FloatField(default=0, verbose_name='Собственные средства основателей'),
        ),
        migrations.AlterField(
            model_name='table',
            name='price',
            field=models.FloatField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='table',
            name='rent_pay',
            field=models.FloatField(default=10000, verbose_name='Аренда'),
        ),
        migrations.AlterField(
            model_name='table',
            name='research',
            field=models.FloatField(default=0, verbose_name='Проведение научных исследований'),
        ),
        migrations.AlterField(
            model_name='table',
            name='salary',
            field=models.FloatField(default=30000, verbose_name='Зарплата сотрудников'),
        ),
        migrations.AlterField(
            model_name='table',
            name='salary_taxes',
            field=models.FloatField(default=0, verbose_name='Начисления на заработную плату сотрудников'),
        ),
        migrations.AlterField(
            model_name='table',
            name='sponsor_invest',
            field=models.FloatField(default=0, verbose_name='Инвестиции'),
        ),
        migrations.AlterField(
            model_name='table',
            name='tech',
            field=models.FloatField(default=0, verbose_name='Приобретение технологий'),
        ),
        migrations.AlterField(
            model_name='table',
            name='third_party',
            field=models.FloatField(default=0, verbose_name='Услуги сторонних организаций'),
        ),
    ]
