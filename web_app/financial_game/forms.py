from .models import table, user
from django.forms import ModelForm, TextInput

class userForm(ModelForm):
    class Meta:
        model = user
        fields = ['name']

        widgets = {
            "name": TextInput(attrs={
                'class': "input-name",
                'autocomplete': "off",
                'id': "name",
                'name': "text"
            })
        }
    
