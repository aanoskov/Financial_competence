from .models import table, user
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput

class userForm(ModelForm):
    class Meta:
        model = user
        fields = ['name']


class tableForm(ModelForm):
    class Meta:
        model = table
        fields = ['earnings','count','price',
        'current_costs','cost_price','salary','salary_taxes',
        'third_party','ads','rent_pay','other','earning_taxes','fin_res',
        'investments','equip','research','tech','education','hospitality','other_invest',
        'funding','grants','own_funds','funds_receipt','funds_refund','sponsor_invest','cash_flow','cash_balance_end','show_res']

    
