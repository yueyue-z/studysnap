# cards/forms.py

from django import forms
from .models import CardSet



class CardSetForm(forms.ModelForm):
    class Meta:  #metadata about the model
        model = CardSet
        fields = ['name', 'description']

    # Optionally, you can customize the form widget attributes here
    widgets = {
        'date_created': forms.DateInput(attrs={'type': 'date'}),
    }
