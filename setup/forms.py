from django import forms

from .models import *

class NewBaseForm(forms.ModelForm):

    class Meta:
        model = BaseModel
        exclude = ['soul', 'max_hp', 'max_mp']
        labels = {
            "dex": "Dexterity",
        }
        
