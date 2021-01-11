#python
#Django
from django import forms
#Project
from .models import Produto

class ProdutoForm(forms.ModelForm):
  class Meta:
    model = Produto
    fields = [
      'nome',
      'valor',
      'categoria',
      'unidade',
    ]
    
    def save(self, *args, **kwargs):
      produto = super(ProdutoForm, self).save(commit=False,*args, **kwargs)
      return produto
