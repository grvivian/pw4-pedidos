#python
#Django
from django import forms
#Project
from .models import Cliente

class ClienteForm(forms.ModelForm):
  class Meta:
    model = Cliente
    fields = [
      'nome',
      'email',
      'data_nascimento',
      'endereco',
      'numero',
      'complemento',
      'bairro',
      'cidade',
      'uf',
      'telefone',
      'celular',
      'rg',
      'cpf',
    ]
    
    def save(self, *args, **kwargs):
      cliente = super(ClienteForm, self).save(commit=False,*args, **kwargs)
      return cliente
