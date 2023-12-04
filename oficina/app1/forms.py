from django import forms
from .models import Car, Peca, Servico, Cliente

class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        exclude = ['id']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['carname', 'model', 'placa', 'dono', 'defeito']

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['car', 'peca', 'data_servico', 'observacoes']
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'endereco', 'numero']
