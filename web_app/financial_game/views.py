import imp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request,'financial_game/main.html')
    #return HttpResponse("<h4>МЫ ТУТ</h4>")

def game(request):
    return render(request,'financial_game/game.html')

def nickname(request):
    return render(request,'financial_game/nickname.html')
    
def table_input(request):
    return render(request,'financial_game/table-input.html')
