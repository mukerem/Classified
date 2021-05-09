from django import forms
from django.forms import ChoiceField
from django.core.validators import RegexValidator


class HouseFilter(forms.Form):
    region_list = [
    'Addis Ababa', 'Afar', 'Amhara', 'Benishangul-Gumuz', 
    'Dire Dawa', 'Gambela', 'Harari', 'Oromia', 'Sidama', 'Somali', 
    'SNNP', 'Tigray'
    ]
    region_choice = [(i, i) for i in region_list]

    region_choice.insert(0, (None, '--------------'))


    location = forms.ChoiceField(
        required=False,
        widget=forms.Select(),
        choices=region_choice,
    )

    min_price = forms.FloatField(
        widget=forms.NumberInput,
        label="Min",
        required=False,
        min_value=0,
    )
    max_price = forms.FloatField(
        widget=forms.NumberInput,
        label="Max",
        required=False,
        min_value=0,
    )
    
    house_type = forms.ChoiceField(
        required=False,
        widget=forms.Select(),
        choices=((None, '--------'), ('Sell', 'Sell'), ('Rent', 'Rent')),
        label="For"
    )