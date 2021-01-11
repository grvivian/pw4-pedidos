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
from .models import Cliente
from ..pedidos.models import Pedido
from .forms import ClienteForm

class ClienteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  template_name = 'clientes/cliente_form.html'
  model = Cliente
  form_class = ClienteForm
  success_message = 'Cliente adicionado com sucesso!'
  #success_url = reverse_lazy('pedidos_home')

class ClienteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  template_name = 'clientes/cliente_form.html'
  model = Cliente
  form_class = ClienteForm
  success_message = 'Cliente atualizado com sucesso!'
  #success_url = reverse_lazy('pedidos_home')

class ClienteListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
  model = Cliente
  template_name = 'clientes/clientes_list.html'

class ClienteDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
  model = Cliente
  template_name = 'clientes/cliente_detail.html'

  def get_context_data(self, object):
    context = super().get_context_data()
    context["pedidos"] = self.object.pedido_set.all()
    return context

class ClienteDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
  template_name = 'clientes/cliente_delete.html'
  model = Cliente
  success_url = reverse_lazy('cliente__list')
  success_message = 'Cliente Excluido com Sucesso!'
