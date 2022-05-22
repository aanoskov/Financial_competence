from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('nickname',views.nickname,name='nickname'),
    path('table_input',views.table_input,name='table_input'),
    path('result',views.result,name='result'),
    path('rating',views.rating,name='rating')
]