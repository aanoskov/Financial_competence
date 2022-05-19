from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

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

class user(models.Model):
    name = models.CharField('Имя игрока', max_length=50)
    #game_move = models.OneToOneField(table,on_delete=models.CASCADE)
    result = models.IntegerField('Результат',default=0)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"


class table(models.Model):
    month_num = models.IntegerField('Номер месяца',default=1)
    cash_balance_begin = models.IntegerField('Остаток денежных средств на начало',default=10000)
    earnings = models.IntegerField('Выручка',default=0)
    count = models.IntegerField('Количество продукта',default=0)
    price = models.IntegerField('Цена',default=0)
    #Current expenses
    current_costs = models.IntegerField('Текущие расходы всего',default=0)
    cost_price = models.IntegerField('Себестоимость продукции',default=700)
    salary = models.IntegerField('Зарплата сотрудников',default=30000)
    salary_taxes = models.IntegerField('Начисления на заработную плату сотрудников',default=0)
    third_party = models.IntegerField('Услуги сторонних организаций',default=0)
    ads = models.IntegerField('Расходы на рекламу',default=0)
    rent_pay = models.IntegerField('Аренда',default=10000)
    other = models.IntegerField('Другие расходы',default=0)
    earning_taxes = models.IntegerField('Общая SUM налогов (6% *Итого Доходов)',default=0)
    fin_res = models.IntegerField('Финансовый результат (прибыль/убыток)',default=0)
    # Investment expenses
    investments = models.IntegerField('Инвестиционные расходы всего',default=0)
    equip = models.IntegerField('Закупка оборудования',default=0)
    research = models.IntegerField('Проведение научных исследований',default=0)
    tech = models.IntegerField('Приобретение технологий',default=0)
    education = models.IntegerField('Обучение сотрудников',default=0)
    hospitality = models.IntegerField('Представительские расходы',default=0)
    #sponsor
    funding = models.IntegerField('Финансирование',default=0)
    own_funds = models.IntegerField('Собственные средства основателей',default=0)
    funds_receipt = models.IntegerField('Заёмные средства (поступления)',default=0)
    funds_refund  = models.IntegerField('Заёмные средства (возврат)',default=0)
    sponsor_invest = models.IntegerField('Инвестиции',default=0)
    cash_flow = models.IntegerField('Денежный поток',default=0)
    cash_balance_end = models.IntegerField('Остаток денежных средств на конец',default=0)

    player = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.month_num)

    class Meta:
        verbose_name = "Таблица хода"
        verbose_name_plural = "Таблицы хода"
