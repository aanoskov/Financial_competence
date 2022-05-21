from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

class green_card(models.Model):
    text = models.CharField('Описание', max_length=250)
    card_type = models.CharField('Тип карты', max_length=50)
    count_1 = models.IntegerField('Кол-во товара в этом месяце')
    price_1 = models.IntegerField('Цена 1 товара в этом месяце')
    earnings = models.IntegerField('Выручка')
    discount = models.IntegerField('Процент скидки')
    count_2 = models.IntegerField('Кол-во товара в следующем месяце')
    price_2 = models.IntegerField('Цена 1 товара в следующем месяце')
    percent = models.IntegerField('Процент онлайн магазина')

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "Зеленая карта"
        verbose_name_plural = "Зеленые карты"


class blue_card(models.Model):
    text = models.CharField('Описание', max_length=250)
    card_type = models.CharField('Тип карты', max_length=50)
    salary_percent = models.PositiveIntegerField('Процент премии сотрудникам', default=10)
    salary_num = models.PositiveIntegerField('Премия программистам', default=50000)
    fines = models.PositiveIntegerField('Штраф', default=1000)
    online_shop = models.PositiveIntegerField('Цена онлайн-магазина', default=50000)
    ads_percent = models.PositiveIntegerField('Проценты на SMM', default=2)
    equip = models.PositiveIntegerField('Цена доп. оборудования', default=30000)
    registration = models.PositiveIntegerField('Цена регистрации компании', default=5000)
    fired_percent = models.PositiveIntegerField('Процент от оклада сотруднику, выполняющему обязательства другого', default=50)
    detector_percent = models.PositiveIntegerField('Процент, на кот. выросла цена датчиков', default=15)
    price_percent = models.PositiveIntegerField('Процент, на кот. выросла цена продукта', default=10)
    education = models.PositiveIntegerField('Стоимость обучения сотрудника', default=12000)
    hospitality_1 = models.PositiveIntegerField('Стоимость стенда', default=5000)
    hospitality_2 = models.PositiveIntegerField('Стоимость флаеров', default=1000)
    hospitality_3 = models.PositiveIntegerField('Стоимость места на выставке', default=15000)
    
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
    cash_balance_begin = models.FloatField('Остаток денежных средств на начало',default=10000)
    earnings = models.FloatField('Выручка',default=0)
    count = models.IntegerField('Количество продукта',default=0)
    price = models.FloatField('Цена',default=0)
    #Current expenses
    current_costs = models.FloatField('Текущие расходы всего',default=0)
    cost_price = models.FloatField('Себестоимость продукции',default=700)
    salary = models.FloatField('Зарплата сотрудников',default=30000)
    salary_taxes = models.FloatField('Начисления на заработную плату сотрудников',default=0)
    third_party = models.FloatField('Услуги сторонних организаций',default=0)
    ads = models.FloatField('Расходы на рекламу',default=0)
    rent_pay = models.FloatField('Аренда',default=10000)
    other = models.FloatField('Другие расходы',default=0)
    earning_taxes = models.FloatField('Общая SUM налогов (6% *Итого Доходов)',default=0)
    fin_res = models.FloatField('Финансовый результат (прибыль/убыток)',default=0)
    # Investment expenses
    investments = models.FloatField('Инвестиционные расходы всего',default=0)
    equip = models.FloatField('Закупка оборудования',default=0)
    research = models.FloatField('Проведение научных исследований',default=0)
    tech = models.FloatField('Приобретение технологий',default=0)
    education = models.FloatField('Обучение сотрудников',default=0)
    hospitality = models.FloatField('Представительские расходы',default=0)
    other_invest = models.FloatField('Другие расходы',default=0)
    #sponsor
    funding = models.FloatField('Финансирование',default=0)
    grants = models.FloatField('Гранты',default=0)
    own_funds = models.FloatField('Собственные средства основателей',default=0)
    funds_receipt = models.FloatField('Заёмные средства (поступления)',default=0)
    funds_refund  = models.FloatField('Заёмные средства (возврат)',default=0)
    sponsor_invest = models.FloatField('Инвестиции',default=0)
    cash_flow = models.FloatField('Денежный поток',default=0)
    cash_balance_end = models.FloatField('Остаток денежных средств на конец',default=0)

    player = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.month_num)

    class Meta:
        verbose_name = "Таблица хода"
        verbose_name_plural = "Таблицы хода"
