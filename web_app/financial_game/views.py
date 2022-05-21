import imp
from django.shortcuts import redirect, render
from django.http import HttpResponse
from numpy import append
from .forms import userForm, tableForm
from .models import user, table
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def main(request):
    return render(request,'financial_game/main.html')
    #return HttpResponse("<h4>МЫ ТУТ</h4>")

def game(request):
    return render(request,'financial_game/game.html')

def nickname(request):

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
                persons_table=table(player= User.objects.get(id=person_id))
                persons_table.save()
                return redirect('table_input')
        else:
            error = 'Форма не валидна'

    form = userForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request,'financial_game/nickname.html', data)
    
def table_input(request):
    error=''
    data={}
    user_id = None
    if request.user.is_authenticated:
        user_id = request.user.id
    else:
        user_id = 1
    current_table= table.objects.get(player=user_id) # table of the current player
    month_num=current_table.month_num
    cash_balance_begin=current_table.cash_balance_begin
    if current_table.month_num > 12:
        #call method of calculating result and return raiting page
        return redirect('result')
    else: #we random 2 cards do all this

        if request.method == 'POST':
            form = tableForm(request.POST,instance=current_table) # take new values of the table from form
            if form.is_valid(): 
                form.save() # save table updates
                #here we need check 
                # if check is ok:
                #   current_table= table.objects.get(player=user_id)
                #   current_table.month_num +=1
                #   current_table.cash_balance_begin = current_table.cash_balance_end
                #   return redirect('table_input')
                # elif we have mistakes,
                #  return red mistakes
                current_table= table.objects.get(player=user_id) # return to updated table
                current_table.month_num +=1 #change number of month
                current_table.save()
                return redirect('table_input')
            else:
                error = 'Форма не валидна'

        form = tableForm(instance=current_table)
        data = {
            'form': form,
            'error': error,
            'month_num':month_num,
            'cash_balance_begin':cash_balance_begin
        }

    return render(request,'financial_game/table-input.html', data)

def result(request):
    user_id = None
    player=None
    if request.user.is_authenticated:
        user_id = request.user.id
        player = request.user.username
    else:
        user_id = 1
    
    current_table = table.objects.get(player=user_id)
    player_result =current_table.result
    data = {
        'player': player,
        'result': player_result,
    }
    
    return render(request,'financial_game/results.html',data)

def rating(request):
    players=table.objects.order_by('result')
    player = {}
    rating=[]
    for one in players:
        player['result']=one.result
        user = User.objects.get(id=one.player.id)
        player['username'] = user.username
        rating.append(player)

    
    
    return render(request,'financial_game/rating.html',{'rating':rating})
