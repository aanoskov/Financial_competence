
class Card:
    def __init__(self, attr_map):
        self.color = attr_map['color']
        self.profit = 0
        self.desc = attr_map['description']

        # attr_map[sale] = (amount, price, discount)
        
        # attr_map[earnings] = (sum of earnings, cost price)
      
        # attr_map[prev_grow] = (growth/reduce (true/false), percents)
        if 'prev_grow' in attr_map:
            self.prev_profit = true
            if attr_map['prev_grow'][0]:
                self.percents = 1 + attr_map['prev_grow'][1]
            else:
                self.percents = 1 - attr_map['prev_grow'][1]

# {'color': 'green', 'description': string, 'products': (10, 2500)}
# {'color': 'blue', 'products': (10, 2500)

class Column:
    def __init__(self, _cost_price, _salary, _employees, _third_party, _rent_pay):
        # dohody
        self.earnings = 0
        self.price = 0
        self.count = 0

        # tekuschie rashody
        self.current_costs = 0
        self.cost_price_per_one = _cost_price
        self.cost_price = 0
        self.employees = _employees
        self.salary = _salary * _employees
        self.salary_taxes = self.salary * 0.302
        self.need_in_third_party = True
        self.third_party_per_one = _third_party
        self.third_party = 0
        self.ads = 0
        self.rent_pay = _rent_pay
        self.other = 0
        self.earning_taxes = 0 

        # investicii
        self.equip = 0
        self.research = 0
        self.tech = 0
        self.education = 0
        self.hospitality = 0
        
        # finansirovanie
        self.grants = 0
        self.owner_money = 0
        self.took_in = 0
        self.took_out = 0
        # self.investments = 0

        # additional fields
        self.next_month = (0, 0)
        self.online_shop = False

    def next_step(self, green_card, blue_card): # not for USA
    # green card(earnings)
        # from the last month (count * cost)
        if self.next_month[0] != 0:
            self.earnings += self.next_month[0] * self.next_month[1]
            self.next_month = (0, 0)
        # count * price
        if 'products' in green_card:
            self.count = green_card['products'][0]
            self.earnings += self.count * green_card['products'][1]
        # count * price * (1 - discount)
        elif 'sale' in green_card:
            self.earnings += green_card['sale'][0] * green_card['sale'][1] * (1 - green_card['sale'][2])
        # total earnings - total price
        elif 'earnings' in green_card:
            self.earnings += green_card['earnings'][0] - green_card['earnings'][1]
        # growth/reducion of sales, tuple (bool, percents)
        elif 'prev_grow' in green_card:
            if green_card['prev_grow'][0]:
                self.count = round(self.count * (1 + green_card['prev_grow'][1])/100)
            else:
                self.count = round(self.count * (1 - green_card['prev_grow'][1]))
            self.earnings += self.count * green_card['profit'][1]
        # opt [(count_1, price_1), (count_2, price_2)]
        elif 'opt' in green_card:
            self.count = green_card['opt'][0][0]
            self.earnings += self.count * green_card['opt'][0][1]
            self.next_month = green_card['opt'][1]
        # online, tuple (count, cost, percents)
        elif 'online' in green_card:
            self.count = green_card['online'][0]
            if self.online_shop:
                self.earnings += self.count * green_card['online'][1]
            else:
                self.earnings += self.count * green_card['online'][1] * (1 - green_card['online'][2]/100)

    # basic costs
        self.cost_price = self.cost_price_per_one * self.count
        if self.need_in_third_party:
            self.third_party = self.third_party_per_one * self.count
        else:
            self.third_party = 0
        self.earning_taxes = self.earnings * 0.06

    # blue card
        # bonus (percents)
        if 'bonus'in blue_card:
            self.salary = (1 + blue_card['bonus']/100) * self.salary
            self.salary_taxes = self.salary * 0.302

        # fines (count)
        elif 'fine' in blue_card:
            self.other = blue_card['fine']
        
        # online shop (price)
        elif 'online_shop' in blue_card:
            self.tech = blue_card['online_shop']
        
        # advertising (SMM), percents
        elif 'ads' in blue_card:
            self.ads = self.earnings * blue_card['ads'] / 100
        
        # equipment (count)
        elif 'equip' in blue_card:
            self.equip = blue_card['equip']
            self.need_in_third_party = False

        # 
        elif 'fired' in blue_card:
            self.employees -= 1
            self.

    def update(self):
        