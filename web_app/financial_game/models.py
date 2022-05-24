from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

class GreenCard(models.Model):
    card_type_choises = [('products', 'Выпуск продукции 1 мес'),
                         ('sale', 'Распродажа'),
                         ('earnings', 'Выручка'),
                         ('opt_1', 'Оптовый контракт 1 мес'),
                         ('opt_2', 'Оптовый контракт 2 мес'),
                         ('online', 'Онлайн заказы')]
    text = models.CharField('Описание', max_length=250)
    card_type = models.CharField('Тип карты', max_length=15, choices=card_type_choises,)
    # products
    count_prod = models.IntegerField('Кол-во товара в этом месяце', default=0)
    price_prod = models.IntegerField('Цена 1 товара в этом месяце', default=0)
    #sale
    discount = models.IntegerField('Процент скидки', default=0)
    # earnings
    earnings = models.IntegerField('Выручка', default=0)
    price_earn = models.IntegerField('Цена 1 товара в этом месяце', default=0)
    # opt 1 month
    count_opt = models.IntegerField('Кол-во товара в этом месяце', default=0)
    earnings_opt = models.IntegerField('Выручка', default=0)
    #opt 2 months
    count_opt_1 = models.IntegerField('Кол-во товара в этом месяце', default=0)
    price_opt_1 = models.IntegerField('Цена 1 товара в этом месяце', default=0)
    count_opt_2 = models.IntegerField('Кол-во товара в следующем месяце', default=0)
    price_opt_2 = models.IntegerField('Цена 1 товара в следующем месяце', default=0)
    # online
    count_online = models.IntegerField('Кол-во товара в этом месяце', default=0)
    price_online = models.IntegerField('Цена 1 товара в этом месяце', default=0)
    percents = models.IntegerField('Процент онлайн магазина', default=0)
    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "Зеленая карта"
        verbose_name_plural = "Зеленые карты"


class BlueCard(models.Model):
    card_type_choises = [('bonus', 'Бонус к зарплате'),
                         ('fines', 'Штрафы (налоги, регистрация)'),
                         ('online_shop', 'Покупка онлайн-магазина'),
                         ('ads', 'Траты на рекламу (СММ)'),
                         ('equip', 'Закупка оборудования'),
                         ('fired', 'Уволился 1 программист'),
                         ('detector', 'Повышение цен на компоненты'),
                         ('education', 'Доп. обучение сотрудников'),
                         ('hospitality', 'Выставка')]
    text = models.CharField('Описание', max_length=250)
    card_type = models.CharField('Тип карты', max_length=15, choices=card_type_choises)
    salary_percent = models.PositiveIntegerField('Процент премии сотрудникам', default=0)
    # salary_num = models.PositiveIntegerField('Премия программистам', default=0)
    fines = models.PositiveIntegerField('Штраф', default=0) # or registration
    online_shop = models.PositiveIntegerField('Цена онлайн-магазина', default=0)
    ads = models.PositiveIntegerField('Проценты на SMM', default=0)
    equip = models.PositiveIntegerField('Цена доп. оборудования', default=0)
    # registration = models.PositiveIntegerField('Цена регистрации компании', default=5000)
    fired_percent = models.PositiveIntegerField('Процент от оклада сотруднику, выполняющему обязательства другого', default=0)
    detector_percent = models.PositiveIntegerField('Процент, на кот. выросла цена датчиков', default=0)
    price_percent = models.PositiveIntegerField('Процент, на кот. выросла цена продукта', default=0)
    education = models.PositiveIntegerField('Стоимость обучения сотрудника', default=0)
    hospitality_1 = models.PositiveIntegerField('Стоимость стенда', default=0)
    hospitality_2 = models.PositiveIntegerField('Стоимость флаеров', default=0)
    hospitality_3 = models.PositiveIntegerField('Стоимость места на выставке', default=0)
    
    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "Голубая карта"
        verbose_name_plural = "Голубые карты"

class user(models.Model):
    name = models.CharField('Имя игрока', max_length=20)
    #game_move = models.OneToOneField(table,on_delete=models.CASCADE)
    result = models.IntegerField('Результат',default=0)
    mistakes = models.IntegerField('Количество ошибок',default=0)

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
    # financing
    funding = models.FloatField('Финансирование',default=0)
    grants = models.FloatField('Гранты',default=0)
    own_funds = models.FloatField('Собственные средства основателей',default=0)
    funds_receipt = models.FloatField('Заёмные средства (поступления)',default=0)
    funds_refund  = models.FloatField('Заёмные средства (возврат)',default=0)
    sponsor_invest = models.FloatField('Инвестиции',default=0)
    cash_flow = models.FloatField('Денежный поток',default=0)
    cash_balance_end = models.FloatField('Остаток денежных средств на конец',default=0)
    own_funds_sum = models.FloatField('Сумма собственных средств основателей ',default=0)
    fin_res_sum = models.FloatField('Сумма финансового результата',default=0)

    player = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    result = models.FloatField('Результат игры',default=0)
    mistakes = models.IntegerField('Ошибки игрока',default=0)
    show_res = models.BooleanField('Показать результат', default=0)
    def __str__(self):
        return str(self.month_num)

    class Meta:
        verbose_name = "Таблица хода"
        verbose_name_plural = "Таблицы хода"


class true_table(models.Model):
    # default values
    def_salary = models.FloatField('', default=10000, editable=False) 
    def_employees = models.FloatField('', default=3, editable=False)
    # earnings
    earnings = models.FloatField('Выручка', default=0)
    price = models.FloatField('Цена', default=0)
    count = models.IntegerField('Кол-во товара', default=0)
    # current payments
    current_costs = models.FloatField('Текущ. расходы', default=0)
    cost_price_per_one_detector = models.FloatField('Цена детектора', default=500)
    cost_price_per_one_maket = models.FloatField('Цена макета', default=200) 
    cost_price = models.FloatField('Себестоимость', default=0) 
    employees = models.IntegerField('Кол-во работников', default=3) 
    salary = models.FloatField('З/п работников', default=30000) 
    salary_taxes = models.FloatField('Налог на зп', default=0) 
    need_in_third_party = models.BooleanField('Нужда в сторонней организации', default=True)
    third_party_per_one = models.FloatField('Стор. орг. на 1 товар', default=200) 
    third_party = models.FloatField('Итог стор. орг.', default=0) 
    ads = models.FloatField('Реклама', default=0) 
    rent_pay = models.FloatField('Аренда', default=10000) 
    other = models.FloatField('Другие расходы', default=0) 
    earning_taxes = models.FloatField('Налог на прибыль', default=0) 
    new_provider = models.FloatField('Новый поставщик', default=1)  # additional percents for price
    fin_res = models.FloatField('Фин. рез.', default=0) 
    # investments
    investments = models.FloatField('Инвестиции', default=0) 
    equip = models.FloatField('Оборудование', default=0) 
    research = models.FloatField('Исследования', default=0) 
    tech = models.FloatField('Технологии', default=0) 
    education = models.FloatField('Обучение сотрудников', default=0) 
    hospitality = models.FloatField('Представительские расходы', default=0)
    cash_balance_end = models.FloatField('Остаток денежных средств на конец',default=0)
    cash_flow = models.FloatField('Денежный поток',default=0)
    funds_refund = models.FloatField('Выплата банку',default=0)
    #добавляем счетчик, процент по кредиту
    counterkred = models.IntegerField('счетчик до окончания выплат по кредиту',default=-1)
    funds_refund2 = models.FloatField('Дополнительная переменная, в которой хранится процент',default=0)
    investflag = models.BooleanField('Флаг привлечения инвестиций',default=False)
    grants = models.FloatField('Дополнительная переменная, для хранения суммы гранта',default=0)
    # additional fields
    next_month_count = models.IntegerField('Кол-во в след. мес.', default=0)
    next_month_price = models.FloatField('Цена в след. мес.', default=0) 
    online_shop = models.BooleanField('', default=False)

    player = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def update(self):
        self.earnings = 0
        self.price = 0
        self.count = 0
        self.salary = self.def_salary
        self.current_costs, self.cost_price, self.salary_taxes, self.third_party = 0, 0, 0, 0
        self.ads, self.other, self.earning_taxes, self.fin_res = 0, 0, 0, 0
        self.investments, self.equip, self.research, self.tech, self.education, self.hospitality = 0, 0, 0, 0, 0, 0
        return

    def __str__(self):
        return str(self.player)

    class Meta:
        verbose_name = "Итсинная таблица хода"
        verbose_name_plural = "Итсинные таблицы хода"


class Support(models.Model):
    binaries = models.CharField('', max_length=43 ,default='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
    values = models.CharField('', max_length = 300, default='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
    blue_card_text = models.CharField('', max_length=300, default='')
    green_card_text = models.CharField('', max_length=300, default='')

    player = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.player)

    class Meta:
        verbose_name = "Админ-класс"
        verbose_name_plural = "Админ-таблицы"
