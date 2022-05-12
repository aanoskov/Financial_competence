import random
from column import Column

# {'color': 'green', 'description': string, 'products': (10, 2500)}
# {'color': 'blue', 'products': (10, 2500)

class Status:
    def __init__(self):
        self.green_card=None
        self.blue_card=None
        self.green_card_type=["products","sale","earnings","opt_1","opt_2","online"]
        self.blue_card_type=["bonus","fine","online_shop","ads","equip","fired", "detector","education","hospitality" ]
        self.column=Column()#add params
        self.cash_balance=10000

    
    def calculate(self):
        self.column.next_step(self.green_card, self.blue_card)

    def get_cards(self):
        #green card
        card_ind=random.randint(0,len(self.green_card_type))
        _green_card={'color': 'green'}
        if self.green_card_type[card_ind]=="products":
            count = random.randint(0,100)
            if count !=0:
                price= random.randint(1000,5000)
                text="in this month you sale "+ str(count) + " by price "+ str(price)
            else:
                price=0
                text= "nothing"
            _green_card["products"]=(count,price)
            _green_card["description"]=text

        elif self.green_card_type[card_ind]=="earnings":
            count = random.randint(1,100)
            price= random.randint(1000,5000)
            _green_card["earnings"]=(count*price,price)
            _green_card["description"]="in this month you earns" + str(count*price) + " by price "+ str(price)

        elif self.green_card_type[card_ind]=="sale":
            count = random.randint(1,100)
            price= random.randint(1000,5000)
            discount=random.randint(5,50)
            _green_card["sale"]= (count,price,discount)
            _green_card["description"]="in this month you sale" + str(count) + " by price "+ str(price) + "with discount " + str(discount)

        elif self.green_card_type[card_ind]=="opt_1":
            count = random.randint(1,100)
            price = random.randint(1000,5000)
            _green_card["opt_1"]=(count,count*price)
        
        elif self.green_card_type[card_ind]=="opt_2":
            count_1 = random.randint(1,100)
            price_1 = random.randint(1000,5000)
            count_2 = random.randint(1,100)
            price_2 = random.randint(1000,5000)
            _green_card["opt_2"]=[(count_1, price_1), (count_2, price_2)]

        elif self.green_card_type[card_ind]=="online":
            count = random.randint(1,100)
            price = random.randint(1000,5000)
            percent = random.randint(1,10)
            _green_card["online"]=(count,price,percent)

        self.green_card= _green_card

        #blue card
        blue_ind=random.randint(0,len(self.blue_card_type))
        _blue_card={'color': 'blue'}

        if self.blue_card_type[blue_ind]=="bonus":
            percent = random.randint(1,30)
            _blue_card["bonus"]=percent

        elif self.blue_card_type[blue_ind]=="fine":
            count = random.randint(1,3000)
            _blue_card["fine"]=count

        elif self.blue_card_type[blue_ind]=="online_shop":
            price = random.randint(5000,50000)
            _blue_card["online_shop"]=price

        elif self.blue_card_type[blue_ind]=="ads":
            percent = random.randint(1,10)
            _blue_card["ads"] = percent

        elif self.blue_card_type[blue_ind]=="equip":
            count = random.randint(5000,50000)
            _blue_card["equip"] = count

        elif self.blue_card_type[blue_ind]=="fired":
            percent = random.randint(20,50)
            _blue_card["fired"] = percent

        elif self.blue_card_type[blue_ind]=="detector":
            percent_1 = random.randint(1,20)
            percent_2 = random.randint(1, percent_1)
            _blue_card["detector"] = (percent_1,percent_2)
        
        elif self.blue_card_type[blue_ind]=="education":
            price = random.randint(5000,20000)
            _blue_card["education"] = price

        elif self.blue_card_type[blue_ind]=="hospitality":
            price_1 = random.randint(1000,6000)
            price_2 = random.randint(500,2000)
            price_3 = random.randint(5000,20000)
            _blue_card["hospitality"] = [price_1, price_2, price_3]

        self.blue_card= _blue_card
        self.calculate()
        return self.green_card, self.blue_card

    def check(self,player_response):
        mistakes=[]
        # earnings
        if(player_response["earnings"]!=self.column.earnings):
            mistakes.append("earnings")
        if(player_response["price"]!=self.column.price):
            mistakes.append("price")
        if(player_response["count"]!=self.column.count):
            mistakes.append("count")

        #Current expenses
        if(player_response["current_costs"]!=self.column.current_costs):
            mistakes.append("current_costs")
        if(player_response["cost_price"]!=self.column.cost_price):
            mistakes.append("cost_price")
        if(player_response["salary"]!=self.column.salary):
            mistakes.append("salary")
        if(player_response["salary_taxes"]!=self.column.salary_taxes):
            mistakes.append("salary_taxes")
        if(player_response["third_party"]!=self.column.third_party):
            mistakes.append("third_party")
        if(player_response["ads"]!=self.column.ads):
            mistakes.append("ads")
        if(player_response["rent_pay"]!=self.column.rent_pay):
            mistakes.append("rent_pay")
        if(player_response["other"]!=self.column.other):
            mistakes.append("other")
        if(player_response["earning_taxes"]!=self.column.earning_taxes):
            mistakes.append("earning_taxes")
        if(player_response["fin_res"]!=self.column.fin_res):
            mistakes.append("fin_res")

        # Investment expenses

        if(player_response["investments"]!=self.column.investments):
            mistakes.append("investments")
        if(player_response["equip"]!=self.column.equip):
            mistakes.append("equip")
        if(player_response["research"]!=self.column.research):
            mistakes.append("research")
        if(player_response["tech"]!=self.column.tech):
            mistakes.append("tech")
        if(player_response["education"]!=self.column.education):
            mistakes.append("education")
        if(player_response["hospitality"]!=self.column.hospitality):
            mistakes.append("hospitality")

        # calculate finance
        cash_flow=self.column.fin_res + self.column.investments + player_response["financing"]

        if(player_response["cash_flow"]!=cash_flow):
            mistakes.append("cash_flow")

        self.cash_balance+=cash_flow

        if(player_response["cash_balance_end"]!=self.cash_balance):
            mistakes.append("cash_balance_end")

        return mistakes



