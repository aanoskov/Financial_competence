from tabnanny import verbose
from django.db import models

class green_card(models.Model):
    text = models.CharField('Текст', max_length=250)
    card_type = models.CharField('Тип карты', max_length=50)
    count_1 = models.IntegerField('Кол-во 1 товара в этом месяце')
    price_1 = models.IntegerField('Цена 1 товара в этом месяце')
    earnings = models.IntegerField('выручка')
    discount = models.IntegerField('процент скидки')
    count_2 = models.IntegerField('Кол-во 1 товара в следующем месяце')
    price_2 = models.IntegerField('Цена 1 товара в следующем месяце')
    percent = models.IntegerField('процент онлайн магазина')

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "Зеленая карта"
        verbose_name_plural = "Зеленые карты"


class blue_card(models.Model):
    text = models.CharField('Текст', max_length=250)
    card_type = models.CharField('Тип карты', max_length=50)
    salary_percent = models.IntegerField('процент премии сотрудникам')
    count = models.IntegerField('количество')
    price_1 = models.IntegerField('цена 1')
    price_2 = models.IntegerField('цена 2')
    price_3 = models.IntegerField('цена 3')

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "Голубая карта"
        verbose_name_plural = "Голубые карты"

class table(models.Model):
    month_num = models.IntegerField('Номер месяца')
    cash_balance_begin = models.IntegerField('Остаток денежных средств на начало')
    earnings = models.IntegerField('Выручка')
    count = models.IntegerField('Количество продукта')
    price = models.IntegerField('Цена')
    #Current expenses
    current_costs = models.IntegerField('Текущие расходы всего')
    cost_price = models.IntegerField('Себестоимость продукции')
    salary = models.IntegerField('Зарплата сотрудников')
    salary_taxes = models.IntegerField('Начисления на заработную плату сотрудников')
    third_party = models.IntegerField('Услуги сторонних организаций')
    ads = models.IntegerField('Расходы на рекламу')
    rent_pay = models.IntegerField('Аренда')
    other = models.IntegerField('Другие расходы')
    earning_taxes = models.IntegerField('Общая SUM налогов (6% *Итого Доходов)')
    fin_res = models.IntegerField('Финансовый результат (прибыль/убыток)')
    # Investment expenses
    investments = models.IntegerField('Инвестиционные расходы всего')
    equip = models.IntegerField('Закупка оборудования')
    research = models.IntegerField('Проведение научных исследований')
    tech = models.IntegerField('Приобретение технологий')
    education = models.IntegerField('Обучение сотрудников')
    hospitality = models.IntegerField('Представительские расходы')
    #sponsor
    funding = models.IntegerField('Финансирование')
    own_funds = models.IntegerField('Собственные средства основателей')
    funds_receipt = models.IntegerField('Заёмные средства (поступления)')
    funds_refund  = models.IntegerField('Заёмные средства (возврат)')
    sponsor_invest = models.IntegerField('Инвестиции')
    cash_flow = models.IntegerField('Денежный поток')
    cash_balance_end = models.IntegerField('Остаток денежных средств на конец')

    def __str__(self):
        return str(self.month_num)

    class Meta:
        verbose_name = "Таблица хода"
        verbose_name_plural = "Таблицы хода"



class user(models.Model):
    name = models.CharField('Имя игрока', max_length=50)
    game_move = models.OneToOneField(table,on_delete=models.CASCADE)
    result = models.IntegerField('Результат')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"