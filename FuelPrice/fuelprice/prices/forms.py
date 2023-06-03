from django import forms
from .models import FuelPrice

class FuelPriceForm(forms.ModelForm):
    class Meta:
        model = FuelPrice
        fields = ['station', 'fuel_type', 'price']
