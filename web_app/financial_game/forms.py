from .models import table, user
from django.forms import ModelForm, TextInput

class userForm(ModelForm):
    class Meta:
        model = user
        fields = ['name']


class tableForm(ModelForm):
    class Meta:
        model = table
        fields = ['month_num','cash_balance_begin','earnings','count','price',
        'current_costs','cost_price','salary','salary_taxes',
        'third_party','ads','rent_pay','other','earning_taxes','fin_res',
        'investments','equip','research','tech','education','hospitality','other_invest',
        'funding','grants','own_funds','funds_receipt','funds_refund','sponsor_invest','cash_flow','cash_balance_end']

    
