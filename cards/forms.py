# cards/forms.py

from django import forms
from .models import CardSet


# class CardCheckForm(forms.Form):
#     card_id = forms.IntegerField(required=True)
#     solved = forms.BooleanField(required=False)


class CardSetForm(forms.ModelForm):
    class Meta:  #metadata about the model
        model = CardSet
        fields = ['name', 'description']

    # Optionally, you can customize the form widget attributes here
    widgets = {
        'date_created': forms.DateInput(attrs={'type': 'date'}),
    }
