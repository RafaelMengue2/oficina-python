from django import forms
from .models import Car
from .models import Peca

class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        exclude = ['id']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['carname', 'model', 'placa', 'dono', 'defeito']
