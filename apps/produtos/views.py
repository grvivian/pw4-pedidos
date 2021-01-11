from django.shortcuts import render

# python

#django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import  DetailView
#project
from .models import Produto
from .forms import ProdutoForm

class ProdutoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  template_name = 'produtos/produto_form.html'
  model = Produto
  form_class = ProdutoForm
  success_message = 'Produto adicionado com sucesso!'
  #success_url = reverse_lazy('pedidos_home')

class ProdutoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  template_name = 'produtos/produto_form.html'
  model = Produto
  form_class = ProdutoForm
  success_message = 'Produto atualizado com sucesso!'
  #success_url = reverse_lazy('pedidos_home')

class ProdutoListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
  model = Produto
  template_name = 'produtos/produtos_list.html'

class ProdutoDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
  model = Produto
  template_name = 'produtos/produto_detail.html'

class ProdutoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
  template_name = 'produtos/produto_delete.html'
  model = Produto
  success_url = reverse_lazy('produto__list')
  success_message = 'Produto Excluido com Sucesso!'
