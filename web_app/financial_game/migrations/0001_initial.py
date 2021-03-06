# Generated by Django 3.1.5 on 2022-05-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blue_card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250, verbose_name='Текст')),
                ('card_type', models.CharField(max_length=50, verbose_name='Тип карты')),
                ('salary_percent', models.IntegerField()),
                ('count', models.IntegerField()),
                ('price_1', models.IntegerField()),
                ('price_2', models.IntegerField()),
                ('price_3', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='green_card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250, verbose_name='Текст')),
                ('card_type', models.CharField(max_length=50, verbose_name='Тип карты')),
                ('count_1', models.IntegerField()),
                ('price_1', models.IntegerField()),
                ('earnings', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('count_2', models.IntegerField()),
                ('price_2', models.IntegerField()),
                ('percent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_num', models.IntegerField(verbose_name='Номер месяца')),
                ('earnings', models.IntegerField(verbose_name='Выручка')),
                ('count', models.IntegerField(verbose_name='Количество продукта')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('current_costs', models.IntegerField(verbose_name='Текущие расходы всего')),
                ('cost_price', models.IntegerField(verbose_name='Себестоимость продукции')),
                ('salary', models.IntegerField(verbose_name='Зарплата сотрудников')),
                ('salary_taxes', models.IntegerField(verbose_name='Начисления на заработную плату сотрудников')),
                ('third_party', models.IntegerField(verbose_name='Услуги сторонних организаций')),
                ('ads', models.IntegerField(verbose_name='Расходы на рекламу')),
                ('rent_pay', models.IntegerField(verbose_name='Аренда')),
                ('other', models.IntegerField(verbose_name='Другие расходы')),
                ('earning_taxes', models.IntegerField(verbose_name='Общая SUM налогов (6% *Итого Доходов)')),
                ('fin_res', models.IntegerField(verbose_name='Финансовый результат (прибыль/убыток)')),
                ('investments', models.IntegerField(verbose_name='Инвестиционные расходы всего')),
                ('equip', models.IntegerField(verbose_name='Закупка оборудования')),
                ('research', models.IntegerField(verbose_name='Проведение научных исследований')),
                ('tech', models.IntegerField(verbose_name='Приобретение технологий')),
                ('education', models.IntegerField(verbose_name='Обучение сотрудников')),
                ('hospitality', models.IntegerField(verbose_name='Представительские расходы')),
                ('funding', models.IntegerField(verbose_name='Финансирование')),
                ('own_funds', models.IntegerField(verbose_name='Собственные средства основателей')),
                ('funds_receipt', models.IntegerField(verbose_name='Заёмные средства (поступления)')),
                ('funds_refund', models.IntegerField(verbose_name='Заёмные средства (возврат)')),
                ('sponsor_invest', models.IntegerField(verbose_name='Инвестиции')),
                ('cash_flow', models.IntegerField(verbose_name='Денежный поток')),
                ('cash_balance_end', models.IntegerField(verbose_name='Остаток денежных средств на конец')),
            ],
        ),
    ]
