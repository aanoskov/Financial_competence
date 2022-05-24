import imp
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import userForm, tableForm
from .models import BlueCard, GreenCard, user, table, true_table, Support
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from random import randint
from numpy import append
import copy

# Create your views here.
def main(request):
    return render(request,'financial_game/main.html')
    #return HttpResponse("<h4>МЫ ТУТ</h4>")

def get_random_cards():
    green_card = GreenCard.objects.all()
    blue_card = BlueCard.objects.all()
    green_rand, blue_rand = randint(0, len(green_card)-1), randint(0, len(blue_card)-1)
    return green_card[green_rand], blue_card[blue_rand]

def nickname(request):
    logout(request)
    error=''
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            username = request.POST.get("name")
            if User.objects.filter(username=username).exists():
                error = 'Такой игрок уже существует, придумайте другое имя'
            else:
                person = User()
                person.username=username
                person.save()
                login(request, person)
                person_id = request.user.id
                persons_table=table(player = User.objects.get(id=person_id))
                true_persons_table = true_table(player = User.objects.get(id=person_id))
                sup = Support(player = User.objects.get(id=person_id))
                persons_table.save()
                true_persons_table.save()
                sup.save()

                # green_card, blue_card = get_random_cards()

                # return render(request, 'financial_game/table_input.html', {'blue_card': blue_card, 'green_card': green_card, 'form': persons_table})
                return redirect('table_input') # add cards to html
        else:
            error = 'Форма не валидна'

    form = userForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request,'financial_game/nickname.html', data)

def update_true_table(user_id):
    true_current_table = true_table.objects.get(player=user_id)
    true_current_table.earnings = 0
    true_current_table.price = 0
    true_current_table.count = 0
    true_current_table.salary  = true_current_table.def_salary
    true_current_table.current_costs, true_current_table.cost_price, true_current_table.salary_taxes, true_current_table.third_party = 0, 0, 0, 0
    true_current_table.ads, true_current_table.other, true_current_table.earning_taxes, true_current_table.fin_res = 0, 0, 0, 0
    true_current_table.investments, true_current_table.equip, true_current_table.research, true_current_table.tech, true_current_table.education, true_current_table.hospitality = 0, 0, 0, 0, 0, 0
    true_current_table.save()

#calculating true values for table
def calc_true_table(green_card, blue_card, user_id):
    true_current_table = true_table.objects.get(player=user_id)

    if true_current_table.next_month_count != 0:
        true_current_table.earnings += true_current_table.next_month_count * true_current_table.next_month_price
    if green_card.card_type == 'products':
        true_current_table.count = green_card.count_prod
        true_current_table.price = green_card.price_prod
        true_current_table.earnings += (green_card.count_prod * green_card.price_prod)
    elif green_card.card_type == 'sale':
        true_current_table.count = green_card.count_prod
        true_current_table.price = green_card.price_prod * (1 - green_card.discount/100)
        true_current_table.earnings += (green_card.count_prod * green_card.price_prod * (1 - green_card.discount/100))
    elif green_card.card_type == 'earnings':
        true_current_table.count = green_card.earnings / green_card.price_earn
        true_current_table.price = green_card.price_earn
        true_current_table.earnings = green_card.earnings
    elif green_card.card_type == 'opt_1':
        true_current_table.count = green_card.count_opt
        true_current_table.price = green_card.earnings_opt / green_card.count_opt
        true_current_table.earnings = green_card.earnings_opt 
    elif green_card.card_type == 'opt_2':
        true_current_table.count = green_card.count_opt_1
        true_current_table.price = green_card.price_opt_1
        true_current_table.earnings += (green_card.count_opt_1 * green_card.price_opt_1)
        true_current_table.next_month_count = green_card.count_opt_2
        true_current_table.next_month_price = green_card.price_opt_2
    elif green_card.card_type == 'online':
        true_current_table.count = green_card.count_online
        true_current_table.price = green_card.price_online
        true_current_table.earnings += (green_card.count_online * green_card.price_online)
        if not true_current_table.online_shop:
            true_current_table.other += green_card.count_online * green_card.price_online * green_card.percents/100
            true_current_table.earnings += true_current_table.other

    if blue_card.card_type == 'bonus':
        true_current_table.salary = (1 + blue_card.salary_percent/100) * true_current_table.def_salary * true_current_table.employees
    elif blue_card.card_type == 'fines':
        true_current_table.other += blue_card.fines
    elif blue_card.card_type == 'online_shop':
        true_current_table.tech += blue_card.online_shop
        true_current_table.online_shop = True
    elif blue_card.card_type == 'ads':
        true_current_table.ads += true_current_table.earnings * blue_card.ads / 100
    elif blue_card.card_type == 'equip':
        true_current_table.equip += blue_card.equip
        true_current_table.need_in_third_party = False
    elif blue_card.card_type == 'fired':
        true_current_table.employees -= (1 - blue_card.fired_percent/100)
        true_current_table.salary = true_current_table.def_salary * true_current_table.employees
    elif blue_card.card_type == 'detector':
        true_current_table.cost_price_per_one_detector = (1 + blue_card.detector_percent/100)
        true_current_table.new_provider = 1 + blue_card.price_percent/100
    elif blue_card.card_type == 'education':
        true_current_table.education += blue_card.education
    elif blue_card.card_type == 'hospitality':
        true_current_table.hospitality += blue_card.hospitality_1 + blue_card.hospitality_2 + blue_card.hospitality_3
    # basic_costs
    true_current_table.cost_price = (true_current_table.cost_price_per_one_detector+
                                    true_current_table.cost_price_per_one_maket) * true_current_table.count
    true_current_table.salary_taxes = true_current_table.salary * 0.302
    if true_current_table.need_in_third_party:
        true_current_table.third_party = true_current_table.third_party_per_one * true_current_table.count
    true_current_table.earnings *= true_current_table.new_provider

    true_current_table.current_costs = (true_current_table.cost_price +
                                        true_current_table.salary +
                                        true_current_table.salary_taxes +
                                        true_current_table.third_party +
                                        true_current_table.ads +
                                        true_current_table.rent_pay +
                                        true_current_table.other)
    true_current_table.earning_taxes = true_current_table.earnings * 0.06
    true_current_table.fin_res = true_current_table.earnings - true_current_table.current_costs - true_current_table.earning_taxes

    true_current_table.investments = (true_current_table.equip +
                                        true_current_table.research +
                                        true_current_table.tech + 
                                        true_current_table.education +
                                        true_current_table.hospitality)
    true_current_table.save()


def table_input(request):
    error=''
    data = {}
    user_id = None
    if request.user.is_authenticated:
        user_id = request.user.id
    else:
        user_id = 1
    current_table= table.objects.get(player=user_id) # table of the current player
    true_current_table = true_table.objects.get(player=user_id)
    cur_sup = Support.objects.get(player=user_id)
    month_num=current_table.month_num
    cash_balance_begin=current_table.cash_balance_begin
    if current_table.month_num > 12:
        #current_table.
        #current_table.result = (current_table.fin_res_sum - current_table.own_funds_sum)/(current_table.own_funds_sum+1)
        cur_sup.delete()
        return redirect('result')
    else:
        binaries = [0 for i in range(22)]
        errors = [0 for i in range(22)]
        if request.method != 'POST':
            green_card, blue_card = get_random_cards()
            update_true_table(user_id)
            calc_true_table(green_card, blue_card, user_id)
            cur_sup.green_card_text = green_card.text
            cur_sup.blue_card_text = blue_card.text
            cur_sup.save()
        if request.method == 'POST':
            form = tableForm(request.POST,instance=current_table) # take new values of the table from form
            if form.is_valid(): 
                form.save() # save table updates
                current_table = table.objects.get(player=user_id) # table of the current player
                # binaries = [0 for i in range(22)]
                # comparing true and user's values
                if current_table.earnings in range(int(true_current_table.earnings - 10), int(true_current_table.earnings + 10)):
                    true_current_table.earnings = current_table.earnings
                    binaries[0] = 1
                if current_table.count in range(int(true_current_table.count - 10), int(true_current_table.count + 10)):
                    true_current_table.count = current_table.count
                    binaries[1] = 1
                if current_table.price in range(int(true_current_table.price - 10), int(true_current_table.price + 10)):
                    true_current_table.price = current_table.price
                    binaries[2] = 1
                if current_table.current_costs in range(int(true_current_table.current_costs - 10), int(true_current_table.current_costs + 10)):
                    true_current_table.current_costs = current_table.current_costs
                    binaries[3] = 1
                if current_table.cost_price in range(int(true_current_table.cost_price - 10), int(true_current_table.cost_price + 10)):
                    true_current_table.cost_price = current_table.cost_price
                    binaries[4] = 1
                if current_table.salary in range(int(true_current_table.salary - 10), int(true_current_table.salary + 10)):
                    true_current_table.salary = current_table.salary
                    binaries[5] = 1
                if current_table.salary_taxes in range(int(true_current_table.salary_taxes - 10), int(true_current_table.salary_taxes + 10)):
                    true_current_table.salary_taxes = current_table.salary_taxes
                    binaries[6] = 1
                if current_table.third_party in range(int(true_current_table.third_party - 10), int(true_current_table.third_party + 10)):
                    true_current_table.third_party = current_table.third_party
                    binaries[7] = 1
                if current_table.ads in range(int(true_current_table.ads - 10), int(true_current_table.ads + 10)):
                    true_current_table.ads = current_table.ads
                    binaries[8] = 1
                if current_table.rent_pay in range(int(true_current_table.rent_pay - 10), int(true_current_table.rent_pay + 10)):
                    true_current_table.rent_pay = current_table.rent_pay
                    binaries[9] = 1
                if current_table.other in range(int(true_current_table.other - 10), int(true_current_table.other + 10)):
                    true_current_table.other = current_table.other
                    binaries[10] = 1 
                if current_table.earning_taxes in range(int(true_current_table.earning_taxes - 10), int(true_current_table.earning_taxes + 10)):
                    true_current_table.earning_taxes = current_table.earning_taxes
                    binaries[11] = 1
                if current_table.fin_res in range(int(true_current_table.fin_res - 10), int(true_current_table.fin_res + 10)):
                    true_current_table.fin_res = current_table.fin_res
                    binaries[12] = 1
                    #
                if current_table.investments in range(int(true_current_table.investments - 10), int(true_current_table.investments + 10)):
                    true_current_table.investments = current_table.investments
                    binaries[13] = 1
                if current_table.equip in range(int(true_current_table.equip - 10), int(true_current_table.equip + 10)) :
                    true_current_table.equip = current_table.equip
                    binaries[14] = 1
                if current_table.research in range(int(true_current_table.research - 10), int(true_current_table.research + 10)) :
                    true_current_table.research =  current_table.research
                    binaries[15] = 1
                if current_table.tech in range(int(true_current_table.tech - 10), int(true_current_table.tech + 10)) :
                    true_current_table.tech = current_table.tech
                    binaries[16] = 1
                if current_table.education in range(int(true_current_table.education - 10), int(true_current_table.education + 10)):
                    true_current_table.education = current_table.education
                    binaries[17] = 1
                if current_table.hospitality in range(int(true_current_table.hospitality - 10), int(true_current_table.hospitality + 10)) :
                    true_current_table.hospitality = current_table.hospitality
                    binaries[18] = 1
                
                ##
                
                
                if current_table.funds_receipt !=0:
                    true_current_table.funds_refund2 = round(current_table.funds_receipt / 120,1)
                    true_current_table.counterkred = 4

                if (true_current_table.counterkred < 4 ) and (true_current_table.counterkred>0):
                    true_current_table.funds_refund = true_current_table.funds_refund2

                if (true_current_table.counterkred < 0):
                    true_current_table.funds_refund2=0
                    true_current_table.funds_refund=0
                
                
                if true_current_table.counterkred==0:
                    true_current_table.funds_refund=true_current_table.funds_refund2*120

                

                true_fundings = (current_table.grants +
                                current_table.own_funds +
                                current_table.funds_receipt - 
                                current_table.funds_refund +
                                current_table.sponsor_invest)
                if current_table.funding in range(int(true_fundings - 10), int(true_fundings + 10)) :
                    binaries[19] = 1
                true_current_table.cash_flow = (true_current_table.fin_res -
                                true_current_table.investments +
                                current_table.funding)
                true_current_table.cash_balance_end = true_current_table.cash_flow + current_table.cash_balance_begin
                true_current_table.save()
                if current_table.cash_flow in range(int(true_current_table.cash_flow - 10), int(true_current_table.cash_flow + 10)):
                    binaries[20] = 1
                if (true_current_table.cash_balance_end) > 0 and current_table.cash_balance_end in range(int(true_current_table.cash_balance_end - 10), int(true_current_table.cash_balance_end + 10)):
                    binaries[21] = 1
                if 0 in binaries:
                    #binaries = ["{% static 'financial_game/img/yes.svg' %}" if binaries[i]==1 else "{% static 'financial_game/img/no.svg' %}" for i in range(len(binaries))]
                    mistakes = 0
                    for i in range(22):
                        if binaries[i] == 0:
                            mistakes +=1  
                    current_table.mistakes += mistakes  
                    current_table.save()
                    if current_table.show_res:
                        data = {
                            'green_card': cur_sup.green_card_text,
                            'blue_card': cur_sup.blue_card_text,
                            'form': form,
                            'error': error,
                            'month_num':month_num,
                            'cash_balance_begin':cash_balance_begin,
                            'binaries': binaries,
                            'true_current_table': true_current_table

                        }
                    else:
                        data = {
                            'green_card': cur_sup.green_card_text,
                            'blue_card': cur_sup.blue_card_text,
                            'form': form,
                            'error': error,
                            'month_num': month_num,
                            'cash_balance_begin': cash_balance_begin,
                            'binaries': binaries,
                        }
                    return render(request,'financial_game/table_input.html', data)

                

                #here we need check 
                # if check is ok:
                #   current_table= table.objects.get(player=user_id)
                #   current_table.month_num +=1
                #   current_table.cash_balance_begin = current_table.cash_balance_end
                #   return redirect('table_input')
                # elif we have mistakes,
                #  return red mistakes               
                current_table.own_funds_sum += current_table.own_funds
                current_table.fin_res_sum += current_table.fin_res
                current_table.cash_balance_begin=current_table.cash_balance_end
                #крутим счетчик кредита 
                
                

                true_current_table.counterkred -=1
                true_current_table.save()
                current_table.month_num +=1 #change number of month
                current_table.save()
                return redirect('table_input')
            else:
                error = 'Форма не валидна'

        form = tableForm(instance=current_table)
        binaries = ["{% static 'financial_game/img/yes.svg' %}" if binaries[i]==1 else "{% static 'financial_game/img/no.svg' %}" for i in range(len(binaries))]
        # green_card = GreenCard(instance=green_card)
        # blue_card = BlueCard(instance=blue_card)
        data = {
            'green_card': green_card,
            'blue_card': blue_card,
            'form': form,
            'error': error, 
            'month_num':month_num,
            'cash_balance_begin':cash_balance_begin,
            'binaries': binaries,
        }

    return render(request,'financial_game/table_input.html', data)

def result(request):
    user_id = None
    player=None
    if request.user.is_authenticated:
        user_id = request.user.id
        player = request.user.username
    else:
        user_id = 1
    
    current_table = table.objects.get(player=user_id)
    current_table.result = (current_table.fin_res_sum - current_table.own_funds_sum)/(current_table.own_funds_sum+1)
    player_result =round(current_table.result,3)
    player_mistakes =current_table.mistakes
    data = {	        
        'player': player,
        'result': player_result,
        'mistakes': player_mistakes,
    }
    return render(request,'financial_game/results.html',data)

def rating(request):
    logout(request)
    players=table.objects.order_by('result')
    player = {}
    rating=[]
    for one in players:
        player['result']=one.result
        user = User.objects.get(id=one.player.id)
        player['username'] = user.username
        player['mistakes'] = one.mistakes
        rating.append(copy.copy(player))



    return render(request,'financial_game/rating.html',{'rating':rating})

def rules(request):
    return render(request,'financial_game/rules.html')
