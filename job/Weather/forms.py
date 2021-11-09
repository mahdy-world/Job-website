from django import forms
from .models import WeatherCity


class WeatherForm(forms.ModelForm):
    class Meta:
        model = WeatherCity
        fields = ['name']


