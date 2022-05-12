# {'color': 'green', 'description': string, 'products': (10, 2500)}
# {'color': 'blue', 'products': (10, 2500)

class Column:
    def __init__(self, _cost_price, _salary, _employees, _third_party, _rent_pay):
        # default values
        self.def_salary = _salary * _employees
        self.def_employees = _employees

        # dohody
        self.earnings = 0
        self.price = 0
        self.count = 0

        # tekuschie rashody
        self.current_costs = 0
        self.cost_price_per_one = _cost_price # array of prices [detector, maket]
        self.cost_price = 0
        self.employees = _employees
        self.salary = _salary * _employees
        self.salary_taxes = 0
        self.need_in_third_party = True
        self.third_party_per_one = _third_party
        self.third_party = 0
        self.ads = 0
        self.rent_pay = _rent_pay
        self.other = 0
        self.earning_taxes = 0
        self.new_provider = 1 # additional percents for price
        self.fin_res = 0

        # investicii
        self.investments = 0
        self.equip = 0
        self.research = 0
        self.tech = 0
        self.education = 0
        self.hospitality = 0

        # additional fields
        self.next_month = (0, 0)
        self.online_shop = False

    def update(self):
        self.earnings = 0
        self.price = 0
        self.count = 0
        self.salary  = self.def_salary
        self.current_costs, self.cost_price, self.salary_taxes, self.third_party = 0, 0, 0, 0
        self.ads, self.other, self.earning_taxes, self.fin_res = 0, 0, 0, 0
        self.investments, self.equip, self.research, self.tech, self.education, self.hospitality = 0, 0, 0, 0, 0, 0
        return

    def next_step(self, green_card, blue_card):
        self.update()
    # green card(earnings)
        # from the last month (count * price)
        if self.next_month[0] != 0:
            self.earnings += self.next_month[0] * self.next_month[1]
            self.next_month = (0, 0)
        # count * price
        if 'products' in green_card:
            self.count = green_card['products'][0]
            self.earnings += self.count * green_card['products'][1]
        # count * price * (1 - discount)
        elif 'sale' in green_card:
            self.earnings += green_card['sale'][0] * green_card['sale'][1] * (1 - green_card['sale'][2]/100)
        # total earnings, price
        elif 'earnings' in green_card:
            self.count = green_card['earnings'][0] / green_card['earnings'][1]
            self.earnings += green_card['earnings'][0]

        # TODO :
        # growth/reducion of sales, tuple (bool, percents)
        # elif 'prev_grow' in green_card:
        #     if green_card['prev_grow'][0]:
        #         # self.count = round(self.count * (1 + green_card['prev_grow'][1])/100)
        #         self.earnings += self.prev_earnings
        #     else:
        #         # self.count = round(self.count * (1 - green_card['prev_grow'][1])/100)
        #     self.earnings += self.count * self.
        
        #opt_1_months (count, earnings)
        elif 'opt_1' in green_card:
            self.count = green_card['opt_1'][0]
            self.earnings = green_card['opt_2'][1]

        # opt_2_months [(count_1, price_1), (count_2, price_2)]
        elif 'opt_2' in green_card:
            self.count = green_card['opt'][0][0]
            self.earnings += self.count * green_card['opt'][0][1]
            self.next_month = green_card['opt'][1]
        # online, tuple (count, price, percents)
        elif 'online' in green_card:
            self.count = green_card['online'][0]
            if self.online_shop:
                self.earnings += self.count * green_card['online'][1]
            else:
                self.earnings += self.count * green_card['online'][1] * (1 - green_card['online'][2]/100)

    # blue card
        # bonus (percents)
        if 'bonus'in blue_card:
            self.salary = (1 + blue_card['bonus']/100) * self.salary

        # fines (count)
        elif 'fine' in blue_card:
            self.other = blue_card['fine']

        # online shop (price)
        elif 'online_shop' in blue_card:
            self.tech = blue_card['online_shop']
            self.online_shop = True

        # advertising (SMM), percents
        elif 'ads' in blue_card:
            self.ads = self.earnings * blue_card['ads'] / 100

        # equipment (count)
        elif 'equip' in blue_card:
            self.equip = blue_card['equip']
            self.need_in_third_party = False

        # one employee is left, percents (additional salary to second employee)
        elif 'fired' in blue_card:
            self.employees -= 1
            self.salary = self.salary * blue_card['fired'] / self.employees

        # detector price, percents for (detector, price)
        elif 'detector' in blue_card:
            self.cost_price_per_one[0] *= blue_card['detector'][0] / 100
            # TODO : question about card no. 9

        # employee education (price)
        elif 'education' in blue_card:
            self.education += blue_card['education']

        # hospitality [price_1, price_2, price_3] (array)
        elif 'hospitality' in blue_card:
            self.hospitality += sum(blue_card['hospitality'])

    # basic costs
        self.cost_price = sum(self.cost_price_per_one) * self.count
        self.salary_taxes = self.salary * 0.302
        if self.need_in_third_party:
            self.third_party = self.third_party_per_one * self.count
        else:
            self.third_party = 0
        self.earnings *= self.new_provider

        self.current_costs = self.cost_price + self.salary + self.salary_taxes + self.third_party + self.ads + self.rent_pay + self.other
        self.earning_taxes = self.earnings * 0.06
        self.fin_res = self.earnings - self.current_costs - self.earning_taxes

        self.investments = self.equip + self.research + self.tech + self.education + self.hospitality
