from unicodedata import name
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('nickname',views.nickname,name='nickname'),
    path('table_input',views.table_input,name='table_input'),
    path('result',views.result,name='result'),
    path('rating',views.rating,name='rating'),
    path('rules',views.rules,name='rules'),
    path('style', TemplateView.as_view(
        template_name='style.css',
        content_type='text/css')
    )
]
