from django.shortcuts import render

# python

#django
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#project
from .models import Pedido, Item
from .forms import PedidoForm, ItemForm

class PedidoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  template_name = 'pedidos/pedido_form.html'
  model = Pedido
  form_class = PedidoForm
  success_message = 'Pedido adicionado com sucesso!'
  #success_url = reverse_lazy('pedidos_home')

class PedidoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  template_name = 'pedidos/pedido_form.html'
  model = Pedido
  form_class = PedidoForm
  success_message = 'Pedido atualizado com sucesso!'

class PedidoListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
  model = Pedido
  template_name = 'pedidos/pedido_list.html'

  def get_context_data(self):
    context = super().get_context_data()
    context["CRIADOS"] = context["object_list"].filter(status=Pedido.CRIADO)
    context["FECHADOS"] = context["object_list"].filter(status=Pedido.FECHADO)
    context["ENVIADOS"] = context["object_list"].filter(status=Pedido.ENVIADO)
    return context

class PedidoDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
  model = Pedido
  template_name = 'pedidos/pedido_detail.html'

class PedidoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
  template_name = 'pedidos/pedido_delete.html'
  model = Pedido
  success_message = 'Item Excluido com Sucesso!'
  success_url = reverse_lazy('item__list')


# Itens
class ItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  template_name = 'pedidos/pedido_form.html'
  model = Item
  form_class = ItemForm
  success_message = 'Item adicionado com sucesso!'

  def form_valid(self, form):
    item = form.save(commit=False)
    item.pedido = Pedido.objects.get(id=self.kwargs["pedido"])
    item.valor_base = item.produto.valor
    item.subtotal = item.valor_base * item.quantidade
    item.save()
    item.pedido.update_total()
    messages.success(self.request, self.success_message)
    return HttpResponseRedirect(item.pedido.get_absolute_url())

class ItemUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  template_name = 'pedidos/pedido_form.html'
  model = Item
  form_class = ItemForm
  success_message = 'Pedido atualizado com sucesso!'

  def form_valid(self, form):
    item = form.save(commit=False)

    item.subtotal = item.valor_base * item.quantidade
    item.save()
    item.pedido.update_total()
    messages.success(self.request, self.success_message)
    return HttpResponseRedirect(item.pedido.get_absolute_url())

class ItemDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
  template_name = 'pedidos/pedido_delete.html'
  model = Item
  success_message = 'Item Excluido com Sucesso!'
  success_url = reverse_lazy('pedido__list')
