import imp
from django.shortcuts import redirect, render
from django.http import HttpResponse
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

    if request.method == 'POST':
        form = tableForm(request.POST)
        if form.is_valid():
            user_id = None
            if request.user.is_authenticated:
                user_id = request.user.id
            else:
                user_id = 1
            form.save()
            # tab=table(player=User.objects.get(id=user_id))
            # tab.save()
        else:
            error = 'Форма не валидна'

    form = tableForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request,'financial_game/table-input.html', data)
