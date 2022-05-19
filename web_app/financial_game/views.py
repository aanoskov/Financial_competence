import imp
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import userForm
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
                error = 'Такой игрок уже существует'
            else:
                person = User.objects.create_user(username)
                login(request, person)
            return redirect('game')
        else:
            error = 'Форма не валидна'

    form = userForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request,'financial_game/nickname.html', data)
    
def table_input(request):
    return render(request,'financial_game/table-input.html')
