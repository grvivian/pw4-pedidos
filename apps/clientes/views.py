from django.shortcuts import render

# python

#django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
#project
from .models import Cliente
from .forms import ClienteForm

class ClienteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  template_name = 'clientes/cliente_form.html'
  model = Cliente
  form_class = ClienteForm
  success_message = 'Cliente adicionado com cucesso!'
  #success_url = reverse_lazy('pedidos_home')

class ClienteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  template_name = 'clientes/cliente_form.html'
  model = Cliente
  form_class = ClienteForm
  success_message = 'Cliente atualizado com cucesso!'
  #success_url = reverse_lazy('pedidos_home')
