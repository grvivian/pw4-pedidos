from django.shortcuts import render

# python

#django
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#project
from .models import Pedido, Item
from .forms import PedidoForm, ItemForm

class PedidoCriadoListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
  queryset = Pedido.objects.filter(status=Pedido.CRIADO)
  template_name = 'pedidos/pedido_list.html'
  paginate_by = 10

  def get_context_data(self):
    context = super().get_context_data()
    context["CRIADO"] = True
    return context

class PedidoFechadoListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
  queryset = Pedido.objects.filter(status=Pedido.FECHADO)
  template_name = 'pedidos/pedido_list.html'
  paginate_by = 10

  def get_context_data(self):
    context = super().get_context_data()
    context["FECHADO"] = True
    return context

class PedidoEnviadoListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
  queryset = Pedido.objects.filter(status=Pedido.ENVIADO)
  template_name = 'pedidos/pedido_list.html'
  paginate_by = 10

  def get_context_data(self):
    context = super().get_context_data()
    context["ENVIADO"] = True
    return context

class PodeModificarMixin(object):
  def dispatch(self, request, *args, **kwargs):
    self.object = self.get_object(self.queryset)
    if self.object.status == Pedido.CRIADO:
      return super().dispatch(request, *args, **kwargs)
    messages.error(request, "Esse pedido não pode mais ser alterado")
    return redirect(self.object.get_absolute_url())

class PedidoCreateView(LoginRequiredMixin, SuccessMessageMixin, PodeModificarMixin, CreateView):
  template_name = 'pedidos/pedido_form.html'
  model = Pedido
  form_class = PedidoForm
  success_message = 'Pedido adicionado com sucesso!'
  #success_url = reverse_lazy('pedidos_home')

class PedidoUpdateView(LoginRequiredMixin, SuccessMessageMixin, PodeModificarMixin, UpdateView):
  template_name = 'pedidos/pedido_form.html'
  model = Pedido
  form_class = PedidoForm
  success_message = 'Pedido atualizado com sucesso!'

class PedidoDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
  model = Pedido
  template_name = 'pedidos/pedido_detail.html'

class PedidoDeleteView(LoginRequiredMixin, SuccessMessageMixin, PodeModificarMixin, DeleteView):
  template_name = 'pedidos/pedido_delete.html'
  model = Pedido
  success_message = 'Item Excluido com Sucesso!'
  success_url = reverse_lazy('item__list')

class FecharPedidoView(View):

  def get(self, request, *args, **kwargs):
    pedido = get_object_or_404(Pedido, id=self.kwargs['pk'])
    return redirect(pedido.get_absolute_url())

  def post(self, request, *args, **kwargs):
    pedido = get_object_or_404(Pedido, id=self.kwargs['pk'])
    pedido.status = Pedido.FECHADO
    pedido.save()
    messages.success(self.request, "Pedido finalizado com sucesso")
    return redirect(pedido.get_absolute_url())

class EnviarPedidoView(View):

  def get(self, request, *args, **kwargs):
    pedido = get_object_or_404(Pedido, id=self.kwargs['pk'])
    return redirect(pedido.get_absolute_url())

  def post(self, request, *args, **kwargs):
    pedido = get_object_or_404(Pedido, id=self.kwargs['pk'])
    pedido.status = Pedido.ENVIADO
    pedido.save()
    messages.success(self.request, "Pedido marcado como enviado")
    return redirect(pedido.get_absolute_url())

# Itens
class ItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  template_name = 'pedidos/pedido_form.html'
  model = Item
  form_class = ItemForm
  success_message = 'Item adicionado com sucesso!'

  def dispatch(self, request, *args, **kwargs):
    self.pedido = Pedido.objects.get(id=self.kwargs["pedido"])
    if self.pedido.status == Pedido.CRIADO:
      return super().dispatch(request, *args, **kwargs)
    messages.error(request, "Esse pedido não pode mais ser alterado")
    return redirect(self.pedido.get_absolute_url())

  def form_valid(self, form):
    item = form.save(commit=False)
    item.pedido = self.pedido
    item.valor_base = item.produto.valor
    item.subtotal = item.valor_base * item.quantidade
    item.save()
    item.pedido.update_total()
    messages.success(self.request, self.success_message)
    return HttpResponseRedirect(item.pedido.get_absolute_url())

class PodeModificarPedidoItemMixin(object):
  def dispatch(self, request, *args, **kwargs):
    self.pedido = self.get_object(self.queryset).pedido
    if self.pedido.status == Pedido.CRIADO:
      return super().dispatch(request, *args, **kwargs)
    messages.error(request, "Esse pedido não pode mais ser alterado")
    return redirect(self.pedido.get_absolute_url())

class ItemUpdateView(LoginRequiredMixin, SuccessMessageMixin, PodeModificarPedidoItemMixin, UpdateView):
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

class ItemDeleteView(LoginRequiredMixin, SuccessMessageMixin, PodeModificarPedidoItemMixin, DeleteView):
  template_name = 'pedidos/pedido_delete.html'
  model = Item
  success_message = 'Item Excluido com Sucesso!'
  success_url = reverse_lazy('pedido__list')
